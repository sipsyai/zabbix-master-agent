package eventlog

// Windows Event Log channels
const (
	SecurityChannel = "Security"
	SystemChannel   = "System"
	NetlogonChannel = "Microsoft-Windows-Netlogon/Operational"
)

// Event IDs for logon activities
const (
	// Logon Events
	EventIDSuccessfulLogon        = 4624
	EventIDFailedLogon            = 4625
	EventIDLogoff                 = 4634
	EventIDAccountLockedOut       = 4740

	// Kerberos Events
	EventIDKerberosTicketGranted  = 4768
	EventIDKerberosServiceTicket  = 4769
	EventIDKerberosTicketRenewal  = 4770
	EventIDKerberosPreAuthFailed  = 4771

	// NTLM Events
	EventIDNTLMAuth               = 4776

	// Netlogon Events
	EventIDDCNotReachable         = 5719
	EventIDDCReachable            = 5723

	// RADIUS Events (NPS)
	EventIDNPSUserGranted         = 6272
	EventIDNPSUserDenied          = 6273
)

// Logon Types
const (
	LogonTypeInteractive          = 2  // Interactive logon
	LogonTypeNetwork              = 3  // Network logon
	LogonTypeBatch                = 4  // Batch logon
	LogonTypeService              = 5  // Service logon
	LogonTypeUnlock               = 7  // Workstation unlock
	LogonTypeNetworkCleartext     = 8  // Network logon with cleartext password
	LogonTypeNewCredentials       = 9  // RunAs with different credentials
	LogonTypeRemoteInteractive    = 10 // Remote Desktop/Terminal Services
	LogonTypeCachedInteractive    = 11 // Cached domain credentials
)

// LogonType returns human-readable logon type name
func LogonTypeName(logonType int) string {
	switch logonType {
	case LogonTypeInteractive:
		return "Interactive"
	case LogonTypeNetwork:
		return "Network"
	case LogonTypeBatch:
		return "Batch"
	case LogonTypeService:
		return "Service"
	case LogonTypeUnlock:
		return "Unlock"
	case LogonTypeNetworkCleartext:
		return "NetworkCleartext"
	case LogonTypeNewCredentials:
		return "NewCredentials"
	case LogonTypeRemoteInteractive:
		return "RemoteInteractive"
	case LogonTypeCachedInteractive:
		return "CachedInteractive"
	default:
		return "Unknown"
	}
}

// Failure Status Codes
const (
	StatusAccountDisabled         = "0xC0000072"
	StatusAccountExpired          = "0xC0000193"
	StatusAccountLockedOut        = "0xC0000234"
	StatusAccountRestriction      = "0xC000006E"
	StatusBadPassword             = "0xC000006A"
	StatusLogonHoursRestriction   = "0xC000006F"
	StatusLogonTypeNotGranted     = "0xC000015B"
	StatusPasswordExpired         = "0xC0000071"
	StatusPasswordMustChange      = "0xC0000224"
	StatusUnknownUser             = "0xC0000064"
	StatusWorkstationRestriction  = "0xC0000070"
)

// FailureReason returns human-readable failure reason
func FailureReason(status string) string {
	switch status {
	case StatusAccountDisabled:
		return "Account disabled"
	case StatusAccountExpired:
		return "Account expired"
	case StatusAccountLockedOut:
		return "Account locked out"
	case StatusAccountRestriction:
		return "Account restriction"
	case StatusBadPassword, StatusUnknownUser:
		return "Unknown user name or bad password"
	case StatusLogonHoursRestriction:
		return "Logon hours restriction"
	case StatusLogonTypeNotGranted:
		return "Logon type not granted"
	case StatusPasswordExpired:
		return "Password expired"
	case StatusPasswordMustChange:
		return "Password must change"
	case StatusWorkstationRestriction:
		return "Workstation restriction"
	default:
		return "Unknown failure reason"
	}
}

// Computer role determination helpers
type ComputerRole int

const (
	RoleUnknown ComputerRole = iota
	RoleDomainController
	RoleMemberServer
	RoleWorkstation
)

// LogonEvent represents a processed logon event
type LogonEvent struct {
	Timestamp    string `json:"timestamp"`
	EventID      int    `json:"event_id"`
	Computer     string `json:"computer"`
	User         string `json:"user"`
	Domain       string `json:"domain"`
	LogonType    int    `json:"logon_type"`
	LogonTypeName string `json:"logon_type_name"`
	SourceIP     string `json:"source_ip"`
	WorkstationName string `json:"workstation_name"`
	Status       string `json:"status"`
	FailureReason string `json:"failure_reason,omitempty"`
	ProcessName  string `json:"process_name,omitempty"`
	AuthPackage  string `json:"auth_package,omitempty"`
}

// LogonSummary represents aggregated logon statistics
type LogonSummary struct {
	Count        int          `json:"count"`
	StartTime    string       `json:"start_time"`
	EndTime      string       `json:"end_time"`
	Events       []LogonEvent `json:"events"`
	UniqueUsers  int          `json:"unique_users,omitempty"`
	UniqueHosts  int          `json:"unique_hosts,omitempty"`
}
