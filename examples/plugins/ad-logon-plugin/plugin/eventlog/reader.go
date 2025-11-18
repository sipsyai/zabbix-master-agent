package eventlog

import (
	"encoding/xml"
	"fmt"
	"syscall"
	"time"
	"unsafe"

	"golang.org/x/sys/windows"
)

var (
	wevtapi                   = windows.NewLazySystemDLL("wevtapi.dll")
	procEvtQuery              = wevtapi.NewProc("EvtQuery")
	procEvtNext               = wevtapi.NewProc("EvtNext")
	procEvtRender             = wevtapi.NewProc("EvtRender")
	procEvtClose              = wevtapi.NewProc("EvtClose")
	procEvtCreateRenderContext = wevtapi.NewProc("EvtCreateRenderContext")
)

const (
	// EvtQuery flags
	EvtQueryChannelPath      = 0x1
	EvtQueryForwardDirection = 0x100

	// EvtRender flags
	EvtRenderEventXml = 1
)

// Event represents a Windows Event Log entry
type Event struct {
	XMLName       xml.Name `xml:"Event"`
	System        System   `xml:"System"`
	EventData     EventData `xml:"EventData"`
	UserData      UserData  `xml:"UserData"`
}

type System struct {
	Provider      Provider  `xml:"Provider"`
	EventID       int       `xml:"EventID"`
	Version       int       `xml:"Version"`
	Level         int       `xml:"Level"`
	Task          int       `xml:"Task"`
	Opcode        int       `xml:"Opcode"`
	Keywords      string    `xml:"Keywords"`
	TimeCreated   TimeCreated `xml:"TimeCreated"`
	EventRecordID int64     `xml:"EventRecordID"`
	Correlation   Correlation `xml:"Correlation"`
	Execution     Execution `xml:"Execution"`
	Channel       string    `xml:"Channel"`
	Computer      string    `xml:"Computer"`
	Security      Security  `xml:"Security"`
}

type Provider struct {
	Name string `xml:"Name,attr"`
	Guid string `xml:"Guid,attr"`
}

type TimeCreated struct {
	SystemTime string `xml:"SystemTime,attr"`
}

type Correlation struct {
	ActivityID string `xml:"ActivityID,attr"`
}

type Execution struct {
	ProcessID int `xml:"ProcessID,attr"`
	ThreadID  int `xml:"ThreadID,attr"`
}

type Security struct {
	UserID string `xml:"UserID,attr"`
}

type EventData struct {
	Data []Data `xml:"Data"`
}

type Data struct {
	Name  string `xml:"Name,attr"`
	Value string `xml:",chardata"`
}

type UserData struct {
	Data string `xml:",innerxml"`
}

// Reader manages Windows Event Log reading
type Reader struct {
	channel string
	query   string
	handle  uintptr
}

// NewReader creates a new event log reader
func NewReader(channel, query string) (*Reader, error) {
	return &Reader{
		channel: channel,
		query:   query,
	}, nil
}

// Open opens the event log for reading
func (r *Reader) Open() error {
	channelPtr, err := syscall.UTF16PtrFromString(r.channel)
	if err != nil {
		return fmt.Errorf("failed to convert channel name: %w", err)
	}

	queryPtr, err := syscall.UTF16PtrFromString(r.query)
	if err != nil {
		return fmt.Errorf("failed to convert query: %w", err)
	}

	ret, _, err := procEvtQuery.Call(
		0, // Session
		uintptr(unsafe.Pointer(channelPtr)),
		uintptr(unsafe.Pointer(queryPtr)),
		uintptr(EvtQueryChannelPath|EvtQueryForwardDirection),
	)

	if ret == 0 {
		return fmt.Errorf("EvtQuery failed: %w", err)
	}

	r.handle = ret
	return nil
}

// Read reads events from the log
func (r *Reader) Read(maxEvents int) ([]Event, error) {
	if r.handle == 0 {
		return nil, fmt.Errorf("reader not opened")
	}

	events := make([]Event, 0, maxEvents)
	eventHandles := make([]uintptr, maxEvents)
	var returned uint32

	ret, _, err := procEvtNext.Call(
		r.handle,
		uintptr(maxEvents),
		uintptr(unsafe.Pointer(&eventHandles[0])),
		uintptr(0), // Timeout (infinite)
		uintptr(0), // Reserved
		uintptr(unsafe.Pointer(&returned)),
	)

	if ret == 0 && returned == 0 {
		// ERROR_NO_MORE_ITEMS = 259 (0x103)
		if errno, ok := err.(syscall.Errno); ok && errno == 259 {
			return events, nil
		}
		return nil, fmt.Errorf("EvtNext failed: %w", err)
	}

	// Render each event
	for i := uint32(0); i < returned; i++ {
		event, err := r.renderEvent(eventHandles[i])
		if err != nil {
			// Log error but continue with other events
			continue
		}
		events = append(events, event)

		// Close event handle
		procEvtClose.Call(eventHandles[i])
	}

	return events, nil
}

// renderEvent renders an event handle to Event struct
func (r *Reader) renderEvent(eventHandle uintptr) (Event, error) {
	var bufferSize uint32
	var bufferUsed uint32
	var propertyCount uint32

	// Get required buffer size
	procEvtRender.Call(
		0, // Context
		eventHandle,
		uintptr(EvtRenderEventXml),
		uintptr(bufferSize),
		0, // Buffer
		uintptr(unsafe.Pointer(&bufferUsed)),
		uintptr(unsafe.Pointer(&propertyCount)),
	)

	if bufferUsed == 0 {
		return Event{}, fmt.Errorf("failed to get buffer size")
	}

	// Allocate buffer
	buffer := make([]uint16, bufferUsed/2)
	bufferSize = bufferUsed

	ret, _, err := procEvtRender.Call(
		0, // Context
		eventHandle,
		uintptr(EvtRenderEventXml),
		uintptr(bufferSize),
		uintptr(unsafe.Pointer(&buffer[0])),
		uintptr(unsafe.Pointer(&bufferUsed)),
		uintptr(unsafe.Pointer(&propertyCount)),
	)

	if ret == 0 {
		return Event{}, fmt.Errorf("EvtRender failed: %w", err)
	}

	// Convert UTF16 to string
	xmlString := syscall.UTF16ToString(buffer)

	// Parse XML
	var event Event
	err = xml.Unmarshal([]byte(xmlString), &event)
	if err != nil {
		return Event{}, fmt.Errorf("failed to parse event XML: %w", err)
	}

	return event, nil
}

// Close closes the event log reader
func (r *Reader) Close() error {
	if r.handle != 0 {
		procEvtClose.Call(r.handle)
		r.handle = 0
	}
	return nil
}

// QueryBuilder helps build XPath queries for event log
type QueryBuilder struct {
	eventIDs    []int
	startTime   *time.Time
	endTime     *time.Time
	computer    string
	customFilter string
}

// NewQueryBuilder creates a new query builder
func NewQueryBuilder() *QueryBuilder {
	return &QueryBuilder{}
}

// WithEventIDs adds event IDs to the query
func (qb *QueryBuilder) WithEventIDs(ids ...int) *QueryBuilder {
	qb.eventIDs = append(qb.eventIDs, ids...)
	return qb
}

// WithTimeRange adds time range to the query
func (qb *QueryBuilder) WithTimeRange(start, end time.Time) *QueryBuilder {
	qb.startTime = &start
	qb.endTime = &end
	return qb
}

// WithStartTime adds start time to the query
func (qb *QueryBuilder) WithStartTime(start time.Time) *QueryBuilder {
	qb.startTime = &start
	return qb
}

// WithComputer filters by computer name
func (qb *QueryBuilder) WithComputer(computer string) *QueryBuilder {
	qb.computer = computer
	return qb
}

// WithCustomFilter adds a custom XPath filter
func (qb *QueryBuilder) WithCustomFilter(filter string) *QueryBuilder {
	qb.customFilter = filter
	return qb
}

// Build builds the XPath query
func (qb *QueryBuilder) Build() string {
	query := "*[System["

	// Event IDs
	if len(qb.eventIDs) > 0 {
		query += "("
		for i, id := range qb.eventIDs {
			if i > 0 {
				query += " or "
			}
			query += fmt.Sprintf("EventID=%d", id)
		}
		query += ")"
	}

	// Time range
	if qb.startTime != nil {
		if len(qb.eventIDs) > 0 {
			query += " and "
		}
		timeStr := qb.startTime.UTC().Format("2006-01-02T15:04:05.000Z")
		query += fmt.Sprintf("TimeCreated[@SystemTime>='%s']", timeStr)
	}

	if qb.endTime != nil {
		query += " and "
		timeStr := qb.endTime.UTC().Format("2006-01-02T15:04:05.000Z")
		query += fmt.Sprintf("TimeCreated[@SystemTime<='%s']", timeStr)
	}

	// Computer
	if qb.computer != "" {
		if len(qb.eventIDs) > 0 || qb.startTime != nil {
			query += " and "
		}
		query += fmt.Sprintf("Computer='%s'", qb.computer)
	}

	query += "]]"

	// Custom filter
	if qb.customFilter != "" {
		query = query[:len(query)-1] + " and " + qb.customFilter + "]"
	}

	return query
}

// GetDataValue gets a named data value from event
func (e *Event) GetDataValue(name string) string {
	for _, data := range e.EventData.Data {
		if data.Name == name {
			return data.Value
		}
	}
	return ""
}

// GetTimestamp returns the event timestamp
func (e *Event) GetTimestamp() (time.Time, error) {
	return time.Parse(time.RFC3339Nano, e.System.TimeCreated.SystemTime)
}
