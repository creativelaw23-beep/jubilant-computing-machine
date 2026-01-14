#!/bin/bash

# Dependency Audit Script
# Checks for security vulnerabilities, outdated packages, and generates a report

set -e

echo "=================================="
echo "Dependency Audit Script"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Create reports directory
REPORT_DIR="./dependency-audit-reports"
mkdir -p "$REPORT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_FILE="$REPORT_DIR/audit_report_$TIMESTAMP.txt"

echo "Audit report will be saved to: $REPORT_FILE"
echo ""

# Function to log to both console and file
log() {
    echo -e "$1" | tee -a "$REPORT_FILE"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Initialize report
log "Dependency Audit Report"
log "Generated: $(date)"
log "Repository: $(basename $(git rev-parse --show-toplevel))"
log "Branch: $(git branch --show-current)"
log "========================================"
log ""

# Check for Node.js/npm dependencies
if [ -f "package.json" ]; then
    log "${BLUE}[Node.js/npm]${NC} Found package.json"

    if command_exists npm; then
        log "${GREEN}✓${NC} npm is installed"

        # Security audit
        log "\n--- npm Security Audit ---"
        if npm audit --json > "$REPORT_DIR/npm-audit-$TIMESTAMP.json" 2>&1; then
            log "${GREEN}✓${NC} No vulnerabilities found"
        else
            log "${RED}✗${NC} Vulnerabilities detected! Check $REPORT_DIR/npm-audit-$TIMESTAMP.json"
            npm audit | tee -a "$REPORT_FILE"
        fi

        # Outdated packages
        log "\n--- npm Outdated Packages ---"
        npm outdated | tee -a "$REPORT_FILE" || log "All packages are up to date"

        # Unused dependencies
        if command_exists npx; then
            log "\n--- Checking for unused dependencies ---"
            npx depcheck | tee -a "$REPORT_FILE" || log "depcheck not available"
        fi
    else
        log "${YELLOW}⚠${NC} npm not installed, skipping npm audit"
    fi
    log ""
else
    log "${BLUE}[Node.js/npm]${NC} No package.json found, skipping"
    log ""
fi

# Check for Python dependencies
if [ -f "requirements.txt" ] || [ -f "Pipfile" ] || [ -f "pyproject.toml" ]; then
    log "${BLUE}[Python/pip]${NC} Found Python dependency file"

    if command_exists pip; then
        log "${GREEN}✓${NC} pip is installed"

        # Security audit with pip-audit
        log "\n--- pip Security Audit ---"
        if command_exists pip-audit; then
            if pip-audit 2>&1 | tee -a "$REPORT_FILE"; then
                log "${GREEN}✓${NC} No vulnerabilities found"
            else
                log "${RED}✗${NC} Vulnerabilities detected!"
            fi
        else
            log "${YELLOW}⚠${NC} pip-audit not installed. Install with: pip install pip-audit"
        fi

        # Outdated packages
        log "\n--- pip Outdated Packages ---"
        pip list --outdated | tee -a "$REPORT_FILE"

    else
        log "${YELLOW}⚠${NC} pip not installed, skipping pip audit"
    fi
    log ""
else
    log "${BLUE}[Python/pip]${NC} No Python dependency files found, skipping"
    log ""
fi

# Check for Ruby dependencies
if [ -f "Gemfile" ]; then
    log "${BLUE}[Ruby/bundler]${NC} Found Gemfile"

    if command_exists bundle; then
        log "${GREEN}✓${NC} bundler is installed"

        # Security audit
        log "\n--- bundle Security Audit ---"
        if gem list bundler-audit | grep bundler-audit >/dev/null; then
            bundle audit update >/dev/null 2>&1
            if bundle audit check 2>&1 | tee -a "$REPORT_FILE"; then
                log "${GREEN}✓${NC} No vulnerabilities found"
            else
                log "${RED}✗${NC} Vulnerabilities detected!"
            fi
        else
            log "${YELLOW}⚠${NC} bundler-audit not installed. Install with: gem install bundler-audit"
        fi

        # Outdated packages
        log "\n--- bundle Outdated Gems ---"
        bundle outdated | tee -a "$REPORT_FILE"

    else
        log "${YELLOW}⚠${NC} bundler not installed, skipping bundle audit"
    fi
    log ""
else
    log "${BLUE}[Ruby/bundler]${NC} No Gemfile found, skipping"
    log ""
fi

# Check for Rust dependencies
if [ -f "Cargo.toml" ]; then
    log "${BLUE}[Rust/cargo]${NC} Found Cargo.toml"

    if command_exists cargo; then
        log "${GREEN}✓${NC} cargo is installed"

        # Security audit
        log "\n--- cargo Security Audit ---"
        if command_exists cargo-audit; then
            if cargo audit 2>&1 | tee -a "$REPORT_FILE"; then
                log "${GREEN}✓${NC} No vulnerabilities found"
            else
                log "${RED}✗${NC} Vulnerabilities detected!"
            fi
        else
            log "${YELLOW}⚠${NC} cargo-audit not installed. Install with: cargo install cargo-audit"
        fi

        # Outdated packages
        log "\n--- cargo Outdated Crates ---"
        if command_exists cargo-outdated; then
            cargo outdated | tee -a "$REPORT_FILE"
        else
            log "${YELLOW}⚠${NC} cargo-outdated not installed. Install with: cargo install cargo-outdated"
        fi

    else
        log "${YELLOW}⚠${NC} cargo not installed, skipping cargo audit"
    fi
    log ""
else
    log "${BLUE}[Rust/cargo]${NC} No Cargo.toml found, skipping"
    log ""
fi

# Check for Go dependencies
if [ -f "go.mod" ]; then
    log "${BLUE}[Go]${NC} Found go.mod"

    if command_exists go; then
        log "${GREEN}✓${NC} go is installed"

        # Check for outdated packages
        log "\n--- Go Outdated Modules ---"
        go list -u -m all | grep '\[' | tee -a "$REPORT_FILE" || log "All modules are up to date"

        # Vulnerability check
        log "\n--- Go Vulnerability Check ---"
        if command_exists govulncheck; then
            govulncheck ./... | tee -a "$REPORT_FILE"
        else
            log "${YELLOW}⚠${NC} govulncheck not installed. Install with: go install golang.org/x/vuln/cmd/govulncheck@latest"
        fi

    else
        log "${YELLOW}⚠${NC} go not installed, skipping go audit"
    fi
    log ""
else
    log "${BLUE}[Go]${NC} No go.mod found, skipping"
    log ""
fi

# Summary
log "\n========================================"
log "Audit Complete"
log "========================================"
log "\nFull report saved to: $REPORT_FILE"
log ""
log "Recommended actions:"
log "1. Review any detected vulnerabilities above"
log "2. Update critical and high-severity packages immediately"
log "3. Schedule updates for outdated packages"
log "4. Remove any unused dependencies"
log "5. Run full test suite after updates"
log ""
log "For detailed vulnerability information:"
log "- npm: Check $REPORT_DIR/npm-audit-$TIMESTAMP.json"
log "- Use online tools: https://snyk.io/ or https://deps.dev/"
log ""

echo -e "${GREEN}Done!${NC}"
