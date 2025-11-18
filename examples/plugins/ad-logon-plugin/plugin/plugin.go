package plugin

import (
	"context"
	"fmt"
	"sync"
	"time"

	"ad-logon-plugin/plugin/handlers"
	"ad-logon-plugin/plugin/params"

	"golang.zabbix.com/sdk/conf"
	"golang.zabbix.com/sdk/errs"
	"golang.zabbix.com/sdk/metric"
	"golang.zabbix.com/sdk/plugin"
	"golang.zabbix.com/sdk/plugin/container"
)

const (
	// Name is the plugin name
	Name = "ADLogon"

	// pluginName is used in configuration
	pluginName = "ADLogon"

	// Metric keys
	logonMetricKey = "ad.logon"
)

// Plugin interface implementation check
var (
	_ plugin.Configurator = (*ADLogonPlugin)(nil)
	_ plugin.Exporter     = (*ADLogonPlugin)(nil)
	_ plugin.Runner       = (*ADLogonPlugin)(nil)
)

// metricKey type for metric keys
type metricKey string

// adLogonMetric represents a single metric with its handler
type adLogonMetric struct {
	metric  *metric.Metric
	handler handlers.HandlerFunc
}

// ADLogonPlugin is the main plugin structure
type ADLogonPlugin struct {
	plugin.Base
	config  *pluginConfig
	metrics map[metricKey]*adLogonMetric
	mu      sync.RWMutex
	cache   *handlers.Cache
}

// impl is the plugin instance
var impl ADLogonPlugin

// Configure implements the plugin.Configurator interface
func (p *ADLogonPlugin) Configure(global *plugin.GlobalOptions, options interface{}) {
	if options == nil {
		p.config = defaultConfig()
		p.config.applyDefaults(global)
		return
	}

	pConfig := &pluginConfig{}
	err := conf.Unmarshal(options, pConfig)
	if err != nil {
		p.Errf("cannot unmarshal configuration options: %s", err.Error())
		p.config = defaultConfig()
		p.config.applyDefaults(global)
		return
	}

	p.config = pConfig
	p.config.applyDefaults(global)

	if p.config.DebugMode {
		p.Infof("plugin configured: timeout=%d, maxEvents=%d, cacheExpiry=%d, defaultHours=%d",
			p.config.Timeout, p.config.MaxEvents, p.config.CacheExpiry, p.config.DefaultHours)
	}
}

// Validate implements the plugin.Configurator interface
func (p *ADLogonPlugin) Validate(options interface{}) error {
	var opts pluginConfig

	err := conf.Unmarshal(options, &opts)
	if err != nil {
		return errs.Wrap(err, "failed to unmarshal configuration options")
	}

	if opts.Timeout != 0 && (opts.Timeout < 1 || opts.Timeout > 300) {
		return fmt.Errorf("timeout must be between 1 and 300 seconds")
	}

	if opts.MaxEvents != 0 && (opts.MaxEvents < 1 || opts.MaxEvents > 10000) {
		return fmt.Errorf("maxEvents must be between 1 and 10000")
	}

	if opts.CacheExpiry > 3600 {
		return fmt.Errorf("cacheExpiry must be between 0 and 3600 seconds")
	}

	if opts.DefaultHours != 0 && (opts.DefaultHours < 1 || opts.DefaultHours > 720) {
		return fmt.Errorf("defaultHours must be between 1 and 720")
	}

	return nil
}

// Start implements the plugin.Runner interface
func (p *ADLogonPlugin) Start() {
	p.Infof("starting %s plugin", Name)

	// Initialize cache
	p.cache = handlers.NewCache(time.Duration(p.config.CacheExpiry) * time.Second)

	p.Infof("%s plugin started successfully", Name)
}

// Stop implements the plugin.Runner interface
func (p *ADLogonPlugin) Stop() {
	p.Infof("stopping %s plugin", Name)

	// Clear cache
	if p.cache != nil {
		p.cache.Clear()
	}

	p.Infof("%s plugin stopped", Name)
}

// Run implements the main plugin execution loop
func (p *ADLogonPlugin) Run() error {
	// Create a new handler for communication with agent
	h, err := container.NewHandler(Name)
	if err != nil {
		return errs.Wrap(err, "failed to create handler")
	}

	// Setup logging - forward plugin logs to agent
	p.Logger = h

	// Execute the plugin
	// This blocks until termination request from agent
	err = h.Execute()
	if err != nil {
		return errs.Wrap(err, "plugin execution failed")
	}

	return nil
}

// Export implements the plugin.Exporter interface
func (p *ADLogonPlugin) Export(key string, params []string, ctx plugin.ContextProvider) (interface{}, error) {
	if key != logonMetricKey {
		return nil, errs.Errorf("unsupported metric key: %s", key)
	}

	p.mu.RLock()
	m, ok := p.metrics[metricKey(key)]
	p.mu.RUnlock()

	if !ok {
		return nil, errs.Errorf("metric %s not found", key)
	}

	// Parse parameters
	metricParams, extraParams, _, err := m.metric.EvalParams(params, ctx)
	if err != nil {
		return nil, errs.Wrap(err, "failed to parse metric parameters")
	}

	// Create context with timeout
	handlerCtx, cancel := context.WithTimeout(context.Background(),
		time.Duration(p.config.Timeout)*time.Second)
	defer cancel()

	// Call handler
	result, err := m.handler(handlerCtx, metricParams, extraParams...)
	if err != nil {
		return nil, errs.Wrap(err, "handler failed")
	}

	return result, nil
}

// registerMetrics registers all plugin metrics
func registerMetrics() error {
	h := handlers.NewHandler(impl.cache, impl.config.MaxEvents, impl.config.DefaultHours)
	h.SetLogger(&impl)

	impl.metrics = map[metricKey]*adLogonMetric{
		logonMetricKey: {
			metric: metric.New(
				"Returns Active Directory logon events based on specified type and time range.",
				params.Params,
				false, // allowDiscovery
			),
			handler: h.HandleLogonQuery,
		},
	}

	// Create metric set
	metricSet := metric.MetricSet{}
	for k, m := range impl.metrics {
		metricSet[string(k)] = m.metric
	}

	// Register metrics
	err := plugin.RegisterMetrics(&impl, Name, metricSet.List()...)
	if err != nil {
		return errs.Wrap(err, "failed to register metrics")
	}

	return nil
}

// New creates a new plugin instance
func New() (*ADLogonPlugin, error) {
	impl = ADLogonPlugin{
		config: defaultConfig(),
	}

	if err := registerMetrics(); err != nil {
		return nil, errs.Wrap(err, "failed to register metrics")
	}

	return &impl, nil
}
