package plugin

import (
	"golang.zabbix.com/sdk/plugin"
)

// pluginConfig represents the plugin configuration
type pluginConfig struct {
	// System options from Zabbix agent
	System plugin.SystemOptions `conf:"optional"`

	// Timeout for event log operations (seconds)
	Timeout int `conf:"optional,range=1:300"`

	// Maximum number of events to retrieve per query
	MaxEvents int `conf:"optional,range=1:10000"`

	// Cache expiry time in seconds
	CacheExpiry int `conf:"optional,range=0:3600"`

	// Default time range in hours for event queries
	DefaultHours int `conf:"optional,range=1:720"`

	// Enable detailed debug logging
	DebugMode bool `conf:"optional"`
}

// defaultConfig returns the default configuration
func defaultConfig() *pluginConfig {
	return &pluginConfig{
		Timeout:      30,
		MaxEvents:    1000,
		CacheExpiry:  300,  // 5 minutes
		DefaultHours: 24,   // Last 24 hours
		DebugMode:    false,
	}
}

// applyDefaults applies default values from global options
func (c *pluginConfig) applyDefaults(global *plugin.GlobalOptions) {
	if c.Timeout == 0 {
		c.Timeout = global.Timeout
	}
	if c.MaxEvents == 0 {
		c.MaxEvents = 1000
	}
	if c.CacheExpiry == 0 {
		c.CacheExpiry = 300
	}
	if c.DefaultHours == 0 {
		c.DefaultHours = 24
	}
}
