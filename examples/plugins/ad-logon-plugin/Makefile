# Makefile for ADLogon Plugin

PLUGIN_NAME = zabbix-agent2-plugin-adlogon
PLUGIN_VERSION = 1.0.0-beta1

# Go parameters
GOCMD = go
GOBUILD = $(GOCMD) build
GOCLEAN = $(GOCMD) clean
GOTEST = $(GOCMD) test
GOGET = $(GOCMD) get
GOMOD = $(GOCMD) mod
GOFMT = $(GOCMD) fmt

# Build parameters
BINARY_NAME = $(PLUGIN_NAME).exe
BUILD_DIR = build
DIST_DIR = dist

# Build flags
LDFLAGS = -s -w
BUILD_FLAGS = -trimpath -ldflags "$(LDFLAGS)"

# Default target
.PHONY: all
all: clean deps build

# Install dependencies
.PHONY: deps
deps:
	@echo "Installing dependencies..."
	$(GOMOD) download
	$(GOMOD) tidy

# Build the plugin
.PHONY: build
build:
	@echo "Building $(PLUGIN_NAME)..."
	@mkdir -p $(BUILD_DIR)
	$(GOBUILD) $(BUILD_FLAGS) -o $(BUILD_DIR)/$(BINARY_NAME) .
	@echo "Build complete: $(BUILD_DIR)/$(BINARY_NAME)"

# Build for Windows (explicit)
.PHONY: build-windows
build-windows:
	@echo "Building for Windows..."
	@mkdir -p $(BUILD_DIR)
	GOOS=windows GOARCH=amd64 $(GOBUILD) $(BUILD_FLAGS) -o $(BUILD_DIR)/$(BINARY_NAME) .
	@echo "Windows build complete: $(BUILD_DIR)/$(BINARY_NAME)"

# Run tests
.PHONY: test
test:
	@echo "Running tests..."
	$(GOTEST) -v ./...

# Run tests with coverage
.PHONY: test-coverage
test-coverage:
	@echo "Running tests with coverage..."
	$(GOTEST) -v -coverprofile=coverage.out ./...
	$(GOCMD) tool cover -html=coverage.out -o coverage.html
	@echo "Coverage report: coverage.html"

# Format code
.PHONY: format
format:
	@echo "Formatting code..."
	$(GOFMT) ./...

# Lint code (requires golangci-lint)
.PHONY: lint
lint:
	@echo "Linting code..."
	@command -v golangci-lint >/dev/null 2>&1 || { echo "golangci-lint not found. Install it from https://golangci-lint.run/"; exit 1; }
	golangci-lint run

# Clean build artifacts
.PHONY: clean
clean:
	@echo "Cleaning..."
	$(GOCLEAN)
	@rm -rf $(BUILD_DIR)
	@rm -rf $(DIST_DIR)
	@rm -f coverage.out coverage.html

# Create distribution package
.PHONY: dist
dist: clean build
	@echo "Creating distribution package..."
	@mkdir -p $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION)
	@cp $(BUILD_DIR)/$(BINARY_NAME) $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION)/
	@cp adlogon.conf $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION)/ 2>/dev/null || :
	@cp README.md $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION)/ 2>/dev/null || :
	@cp LICENSE $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION)/ 2>/dev/null || :
	@cd $(DIST_DIR) && zip -r $(PLUGIN_NAME)-$(PLUGIN_VERSION).zip $(PLUGIN_NAME)-$(PLUGIN_VERSION)
	@echo "Distribution package: $(DIST_DIR)/$(PLUGIN_NAME)-$(PLUGIN_VERSION).zip"

# Development build (without optimization)
.PHONY: dev
dev:
	@echo "Building development version..."
	@mkdir -p $(BUILD_DIR)
	$(GOBUILD) -o $(BUILD_DIR)/$(BINARY_NAME) .

# Run the plugin (for testing)
.PHONY: run
run: build
	@echo "Running plugin..."
	$(BUILD_DIR)/$(BINARY_NAME)

# Install to Zabbix plugin directory (customize path as needed)
.PHONY: install
install: build
	@echo "Installing plugin..."
	@if [ -z "$(PLUGIN_DIR)" ]; then \
		echo "Error: PLUGIN_DIR not set. Use: make install PLUGIN_DIR=/path/to/plugins"; \
		exit 1; \
	fi
	@mkdir -p $(PLUGIN_DIR)
	@cp $(BUILD_DIR)/$(BINARY_NAME) $(PLUGIN_DIR)/
	@echo "Plugin installed to $(PLUGIN_DIR)/$(BINARY_NAME)"
	@echo "Don't forget to update your Zabbix agent configuration!"

# Help
.PHONY: help
help:
	@echo "ADLogon Plugin - Makefile targets:"
	@echo ""
	@echo "  make all          - Clean, install deps, and build"
	@echo "  make deps         - Install Go dependencies"
	@echo "  make build        - Build the plugin"
	@echo "  make build-windows- Build for Windows explicitly"
	@echo "  make test         - Run tests"
	@echo "  make test-coverage- Run tests with coverage"
	@echo "  make format       - Format Go code"
	@echo "  make lint         - Lint code (requires golangci-lint)"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make dist         - Create distribution package"
	@echo "  make dev          - Build without optimization (for development)"
	@echo "  make run          - Build and run the plugin"
	@echo "  make install      - Install to Zabbix plugin dir (set PLUGIN_DIR)"
	@echo "  make help         - Show this help message"
	@echo ""
	@echo "Example:"
	@echo "  make install PLUGIN_DIR=/etc/zabbix/plugins"
