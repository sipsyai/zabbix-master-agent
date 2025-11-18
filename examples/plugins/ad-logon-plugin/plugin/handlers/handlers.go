package handlers

import (
	"context"
	"encoding/json"
	"strconv"
	"strings"
	"time"

	"ad-logon-plugin/plugin/eventlog"

	"golang.zabbix.com/sdk/errs"
)

// HandlerFunc is the signature for metric handlers
type HandlerFunc func(ctx context.Context, params map[string]string, extraParams ...string) (interface{}, error)

// Logger interface for plugin logging
type Logger interface {
	Infof(format string, args ...interface{})
	Debugf(format string, args ...interface{})
	Warningf(format string, args ...interface{})
	Errf(format string, args ...interface{})
}

// Handler manages all metric handlers
type Handler struct {
	cache        *Cache
	maxEvents    int
	defaultHours int
	logger       Logger
}

// NewHandler creates a new handler
func NewHandler(cache *Cache, maxEvents, defaultHours int) *Handler {
	return &Handler{
		cache:        cache,
		maxEvents:    maxEvents,
		defaultHours: defaultHours,
	}
}

// SetLogger sets the logger for the handler
func (h *Handler) SetLogger(logger Logger) {
	h.logger = logger
}

// log logs a message if logger is available
func (h *Handler) log(level string, format string, args ...interface{}) {
	if h.logger == nil {
		return
	}

	switch level {
	case "info":
		h.logger.Infof(format, args...)
	case "debug":
		h.logger.Debugf(format, args...)
	case "warning":
		h.logger.Warningf(format, args...)
	case "error":
		h.logger.Errf(format, args...)
	}
}

// HandleLogonQuery is the main handler for ad.logon metric
func (h *Handler) HandleLogonQuery(ctx context.Context, params map[string]string, extraParams ...string) (interface{}, error) {
	// Extract parameters
	logType := params["type"]
	hoursStr := params["hours"]
	computer := params["computer"]

	// Parse hours
	hours, err := strconv.Atoi(hoursStr)
	if err != nil {
		hours = h.defaultHours
	}

	h.log("info", "processing logon query: type=%s, hours=%d, computer=%s", logType, hours, computer)

	// Route to appropriate handler
	switch strings.ToLower(logType) {
	case "failure":
		return h.handleLogonFailure(ctx, hours, computer)
	case "dc_activity":
		return h.handleDCActivity(ctx, hours, computer)
	case "server_activity":
		return h.handleServerActivity(ctx, hours, computer)
	case "workstation_activity":
		return h.handleWorkstationActivity(ctx, hours, computer)
	case "user_activity":
		return h.handleUserActivity(ctx, hours, computer)
	case "recent_users":
		return h.handleRecentUsers(ctx, hours, computer)
	case "last_logon":
		return h.handleLastLogon(ctx, hours, computer)
	case "multiple_computers":
		return h.handleMultipleComputers(ctx, hours, computer)
	case "radius":
		return h.handleRADIUSLogon(ctx, hours, computer)
	default:
		return nil, errs.Errorf("unknown logon type: %s", logType)
	}
}

// handleLogonFailure handles logon failure queries
func (h *Handler) handleLogonFailure(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying logon failures: hours=%d, computer=%s", hours, computer)

	// Build query
	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDFailedLogon).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	// Read events
	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read logon failure events")
	}

	// Process events
	logonEvents := make([]eventlog.LogonEvent, 0, len(events))
	for _, evt := range events {
		logonEvent := h.processLogonEvent(evt, "failure")
		logonEvents = append(logonEvents, logonEvent)
	}

	summary := eventlog.LogonSummary{
		Count:     len(logonEvents),
		StartTime: startTime.Format(time.RFC3339),
		EndTime:   time.Now().Format(time.RFC3339),
		Events:    logonEvents,
	}

	// Convert to JSON
	return h.toJSON(summary)
}

// handleDCActivity handles domain controller logon activity
func (h *Handler) handleDCActivity(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying DC activity: hours=%d, computer=%s", hours, computer)

	return h.handleLogonActivity(ctx, hours, computer, "dc_activity")
}

// handleServerActivity handles member server logon activity
func (h *Handler) handleServerActivity(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying server activity: hours=%d, computer=%s", hours, computer)

	return h.handleLogonActivity(ctx, hours, computer, "server_activity")
}

// handleWorkstationActivity handles workstation logon activity
func (h *Handler) handleWorkstationActivity(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying workstation activity: hours=%d, computer=%s", hours, computer)

	return h.handleLogonActivity(ctx, hours, computer, "workstation_activity")
}

// handleLogonActivity is a generic handler for logon activities
func (h *Handler) handleLogonActivity(ctx context.Context, hours int, computer, activityType string) (interface{}, error) {
	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDSuccessfulLogon).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	// Read events
	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read logon activity events")
	}

	// Process and filter events based on activity type
	logonEvents := make([]eventlog.LogonEvent, 0)
	for _, evt := range events {
		// Filter based on logon type and computer role
		if h.shouldIncludeEvent(evt, activityType) {
			logonEvent := h.processLogonEvent(evt, "success")
			logonEvents = append(logonEvents, logonEvent)
		}
	}

	summary := eventlog.LogonSummary{
		Count:     len(logonEvents),
		StartTime: startTime.Format(time.RFC3339),
		EndTime:   time.Now().Format(time.RFC3339),
		Events:    logonEvents,
	}

	return h.toJSON(summary)
}

// handleUserActivity handles user-specific logon activity
func (h *Handler) handleUserActivity(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying user activity: hours=%d, computer=%s", hours, computer)

	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDSuccessfulLogon, eventlog.EventIDFailedLogon).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read user activity events")
	}

	// Group by user
	userMap := make(map[string][]eventlog.LogonEvent)
	for _, evt := range events {
		status := "success"
		if evt.System.EventID == eventlog.EventIDFailedLogon {
			status = "failure"
		}
		logonEvent := h.processLogonEvent(evt, status)
		userKey := logonEvent.Domain + "\\" + logonEvent.User
		userMap[userKey] = append(userMap[userKey], logonEvent)
	}

	// Flatten for output
	allEvents := make([]eventlog.LogonEvent, 0)
	for _, events := range userMap {
		allEvents = append(allEvents, events...)
	}

	summary := eventlog.LogonSummary{
		Count:       len(allEvents),
		StartTime:   startTime.Format(time.RFC3339),
		EndTime:     time.Now().Format(time.RFC3339),
		Events:      allEvents,
		UniqueUsers: len(userMap),
	}

	return h.toJSON(summary)
}

// handleRecentUsers handles recent user logon queries
func (h *Handler) handleRecentUsers(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying recent users: hours=%d, computer=%s", hours, computer)

	// Similar to user activity but only successful logons
	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDSuccessfulLogon).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read recent user events")
	}

	logonEvents := make([]eventlog.LogonEvent, 0, len(events))
	for _, evt := range events {
		logonEvent := h.processLogonEvent(evt, "success")
		logonEvents = append(logonEvents, logonEvent)
	}

	summary := eventlog.LogonSummary{
		Count:     len(logonEvents),
		StartTime: startTime.Format(time.RFC3339),
		EndTime:   time.Now().Format(time.RFC3339),
		Events:    logonEvents,
	}

	return h.toJSON(summary)
}

// handleLastLogon handles last logon on workstations
func (h *Handler) handleLastLogon(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying last logon: hours=%d, computer=%s", hours, computer)

	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDSuccessfulLogon).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read last logon events")
	}

	// Group by computer and keep only last logon per computer
	computerMap := make(map[string]eventlog.LogonEvent)
	for _, evt := range events {
		logonEvent := h.processLogonEvent(evt, "success")
		computerKey := logonEvent.Computer

		// Keep the most recent logon for each computer
		if existing, ok := computerMap[computerKey]; !ok {
			computerMap[computerKey] = logonEvent
		} else {
			if logonEvent.Timestamp > existing.Timestamp {
				computerMap[computerKey] = logonEvent
			}
		}
	}

	// Flatten for output
	lastLogons := make([]eventlog.LogonEvent, 0, len(computerMap))
	for _, event := range computerMap {
		lastLogons = append(lastLogons, event)
	}

	summary := eventlog.LogonSummary{
		Count:       len(lastLogons),
		StartTime:   startTime.Format(time.RFC3339),
		EndTime:     time.Now().Format(time.RFC3339),
		Events:      lastLogons,
		UniqueHosts: len(computerMap),
	}

	return h.toJSON(summary)
}

// handleMultipleComputers handles users logged into multiple computers
func (h *Handler) handleMultipleComputers(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying multiple computers: hours=%d", hours)

	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDSuccessfulLogon).
		WithStartTime(startTime)

	query := qb.Build()

	events, err := h.readEvents(ctx, eventlog.SecurityChannel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read multiple computer events")
	}

	// Group by user and track unique computers
	userComputerMap := make(map[string]map[string]bool)
	userEventsMap := make(map[string][]eventlog.LogonEvent)

	for _, evt := range events {
		logonEvent := h.processLogonEvent(evt, "success")
		userKey := logonEvent.Domain + "\\" + logonEvent.User

		if _, ok := userComputerMap[userKey]; !ok {
			userComputerMap[userKey] = make(map[string]bool)
		}
		userComputerMap[userKey][logonEvent.Computer] = true
		userEventsMap[userKey] = append(userEventsMap[userKey], logonEvent)
	}

	// Filter users with multiple computers
	multipleComputerEvents := make([]eventlog.LogonEvent, 0)
	for userKey, computers := range userComputerMap {
		if len(computers) > 1 {
			multipleComputerEvents = append(multipleComputerEvents, userEventsMap[userKey]...)
		}
	}

	summary := eventlog.LogonSummary{
		Count:     len(multipleComputerEvents),
		StartTime: startTime.Format(time.RFC3339),
		EndTime:   time.Now().Format(time.RFC3339),
		Events:    multipleComputerEvents,
	}

	return h.toJSON(summary)
}

// handleRADIUSLogon handles RADIUS/NPS logon events
func (h *Handler) handleRADIUSLogon(ctx context.Context, hours int, computer string) (interface{}, error) {
	h.log("debug", "querying RADIUS logon: hours=%d, computer=%s", hours, computer)

	startTime := time.Now().Add(-time.Duration(hours) * time.Hour)
	qb := eventlog.NewQueryBuilder().
		WithEventIDs(eventlog.EventIDNPSUserGranted, eventlog.EventIDNPSUserDenied).
		WithStartTime(startTime)

	if computer != "" {
		qb.WithComputer(computer)
	}

	query := qb.Build()

	// RADIUS events are in System log or NPS log
	events, err := h.readEvents(ctx, eventlog.SystemChannel, query)
	if err != nil {
		// Try Security channel as fallback
		events, err = h.readEvents(ctx, eventlog.SecurityChannel, query)
		if err != nil {
			return nil, errs.Wrap(err, "failed to read RADIUS events")
		}
	}

	logonEvents := make([]eventlog.LogonEvent, 0, len(events))
	for _, evt := range events {
		status := "success"
		if evt.System.EventID == eventlog.EventIDNPSUserDenied {
			status = "failure"
		}
		logonEvent := h.processLogonEvent(evt, status)
		logonEvents = append(logonEvents, logonEvent)
	}

	summary := eventlog.LogonSummary{
		Count:     len(logonEvents),
		StartTime: startTime.Format(time.RFC3339),
		EndTime:   time.Now().Format(time.RFC3339),
		Events:    logonEvents,
	}

	return h.toJSON(summary)
}

// readEvents reads events from the specified channel
func (h *Handler) readEvents(ctx context.Context, channel, query string) ([]eventlog.Event, error) {
	reader, err := eventlog.NewReader(channel, query)
	if err != nil {
		return nil, errs.Wrap(err, "failed to create event reader")
	}
	defer reader.Close()

	err = reader.Open()
	if err != nil {
		return nil, errs.Wrap(err, "failed to open event log")
	}

	events, err := reader.Read(h.maxEvents)
	if err != nil {
		return nil, errs.Wrap(err, "failed to read events")
	}

	h.log("debug", "read %d events from %s", len(events), channel)
	return events, nil
}

// processLogonEvent converts an Event to LogonEvent
func (h *Handler) processLogonEvent(evt eventlog.Event, status string) eventlog.LogonEvent {
	timestamp, _ := evt.GetTimestamp()

	logonEvent := eventlog.LogonEvent{
		Timestamp:    timestamp.Format(time.RFC3339),
		EventID:      evt.System.EventID,
		Computer:     evt.System.Computer,
		Status:       status,
	}

	// Extract data based on event ID
	switch evt.System.EventID {
	case eventlog.EventIDSuccessfulLogon, eventlog.EventIDFailedLogon:
		logonEvent.User = evt.GetDataValue("TargetUserName")
		logonEvent.Domain = evt.GetDataValue("TargetDomainName")
		logonTypeStr := evt.GetDataValue("LogonType")
		if logonType, err := strconv.Atoi(logonTypeStr); err == nil {
			logonEvent.LogonType = logonType
			logonEvent.LogonTypeName = eventlog.LogonTypeName(logonType)
		}
		logonEvent.SourceIP = evt.GetDataValue("IpAddress")
		logonEvent.WorkstationName = evt.GetDataValue("WorkstationName")
		logonEvent.ProcessName = evt.GetDataValue("ProcessName")
		logonEvent.AuthPackage = evt.GetDataValue("AuthenticationPackageName")

		if status == "failure" {
			failStatus := evt.GetDataValue("Status")
			logonEvent.FailureReason = eventlog.FailureReason(failStatus)
		}

	case eventlog.EventIDKerberosTicketGranted, eventlog.EventIDKerberosServiceTicket:
		logonEvent.User = evt.GetDataValue("TargetUserName")
		logonEvent.Domain = evt.GetDataValue("TargetDomainName")
		logonEvent.SourceIP = evt.GetDataValue("IpAddress")

	case eventlog.EventIDNTLMAuth:
		logonEvent.User = evt.GetDataValue("TargetUserName")
		logonEvent.Domain = evt.GetDataValue("TargetDomainName")
		logonEvent.WorkstationName = evt.GetDataValue("Workstation")

	case eventlog.EventIDNPSUserGranted, eventlog.EventIDNPSUserDenied:
		logonEvent.User = evt.GetDataValue("UserName")
		logonEvent.SourceIP = evt.GetDataValue("ClientIPAddress")
	}

	return logonEvent
}

// shouldIncludeEvent determines if an event should be included based on activity type
func (h *Handler) shouldIncludeEvent(evt eventlog.Event, activityType string) bool {
	// This is a simplified filter - in production, you might want to check
	// computer roles against AD or use naming conventions
	computer := strings.ToLower(evt.System.Computer)

	switch activityType {
	case "dc_activity":
		// Domain controllers typically have "DC" in their name
		return strings.Contains(computer, "dc")
	case "server_activity":
		// Member servers typically have "SRV" or "SERVER" in their name
		return strings.Contains(computer, "srv") || strings.Contains(computer, "server")
	case "workstation_activity":
		// Workstations typically have "WS", "PC", or "DESKTOP" in their name
		return strings.Contains(computer, "ws") || strings.Contains(computer, "pc") ||
			strings.Contains(computer, "desktop")
	default:
		return true
	}
}

// toJSON converts data to JSON string
func (h *Handler) toJSON(data interface{}) (string, error) {
	jsonBytes, err := json.Marshal(data)
	if err != nil {
		return "", errs.Wrap(err, "failed to marshal JSON")
	}
	return string(jsonBytes), nil
}
