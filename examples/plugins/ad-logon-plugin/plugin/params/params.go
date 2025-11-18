package params

import (
	"golang.zabbix.com/sdk/metric"
)

const (
	// Parameter names
	LogTypeParameterName = "type"
	HoursParameterName   = "hours"
	ComputerParameterName = "computer"
)

// Params defines the parameters for the ad.logon metric
var Params = []*metric.Param{LogType, Hours, Computer}

// LogType parameter defines the type of logon data to retrieve
var LogType = metric.NewParam(
	LogTypeParameterName,
	"Type of logon data to retrieve (failure, dc_activity, server_activity, workstation_activity, user_activity, recent_users, last_logon, multiple_computers, radius).",
)

// Hours parameter defines how many hours back to query
var Hours = metric.NewParam(
	HoursParameterName,
	"Number of hours to look back (default: 24, max: 720).",
).WithDefault("24")

// Computer parameter filters by computer name
var Computer = metric.NewParam(
	ComputerParameterName,
	"Filter by specific computer name (optional).",
).WithDefault("")
