#!/bin/bash

# Dependency Audit Script
# Automatically detects project type and runs appropriate dependency audits

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Icons
CHECK="✓"
CROSS="✗"
WARNING="⚠"
INFO="ℹ"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Dependency Audit Tool${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to print section header
print_section() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

# Function to print success
print_success() {
    echo -e "${GREEN}${CHECK} $1${NC}"
}

# Function to print error
print_error() {
    echo -e "${RED}${CROSS} $1${NC}"
}

# Function to print warning
print_warning() {
    echo -e "${YELLOW}${WARNING} $1${NC}"
}

# Function to print info
print_info() {
    echo -e "${INFO} $1"
}

# Detect project type
detect_project_type() {
    if [ -f "package.json" ]; then
        echo "nodejs"
    elif [ -f "requirements.txt" ] || [ -f "Pipfile" ] || [ -f "pyproject.toml" ]; then
        echo "python"
    elif [ -f "Gemfile" ]; then
        echo "ruby"
    elif [ -f "Cargo.toml" ]; then
        echo "rust"
    elif [ -f "go.mod" ]; then
        echo "go"
    elif [ -f "pom.xml" ]; then
        echo "java-maven"
    elif [ -f "build.gradle" ]; then
        echo "java-gradle"
    elif [ -f "composer.json" ]; then
        echo "php"
    else
        echo "unknown"
    fi
}

# Node.js audit
audit_nodejs() {
    print_section "Node.js Dependency Audit"

    if ! command_exists npm; then
        print_error "npm not found. Please install Node.js."
        return 1
    fi

    print_info "Checking for security vulnerabilities..."
    if npm audit --audit-level=info; then
        print_success "No security vulnerabilities found"
    else
        print_warning "Security vulnerabilities detected. Run 'npm audit fix' to fix them."
    fi

    echo ""
    print_info "Checking for outdated packages..."
    if npm outdated; then
        print_warning "Some packages are outdated"
    else
        print_success "All packages are up to date"
    fi

    echo ""
    if command_exists npx; then
        print_info "Checking for unused dependencies..."
        if npx depcheck --skip-missing; then
            print_success "No unused dependencies found"
        else
            print_warning "Unused dependencies detected"
        fi
    fi
}

# Python audit
audit_python() {
    print_section "Python Dependency Audit"

    if ! command_exists pip; then
        print_error "pip not found. Please install Python."
        return 1
    fi

    print_info "Checking for security vulnerabilities..."
    if command_exists safety; then
        if safety check; then
            print_success "No security vulnerabilities found"
        else
            print_warning "Security vulnerabilities detected"
        fi
    else
        print_warning "safety not installed. Run: pip install safety"
    fi

    echo ""
    print_info "Checking for outdated packages..."
    pip list --outdated

    echo ""
    if command_exists pip-audit; then
        print_info "Running pip-audit..."
        if pip-audit; then
            print_success "No vulnerabilities found by pip-audit"
        else
            print_warning "Vulnerabilities detected by pip-audit"
        fi
    else
        print_warning "pip-audit not installed. Run: pip install pip-audit"
    fi
}

# Ruby audit
audit_ruby() {
    print_section "Ruby Dependency Audit"

    if ! command_exists bundle; then
        print_error "bundler not found. Please install bundler."
        return 1
    fi

    print_info "Checking for security vulnerabilities..."
    if bundle audit check --update; then
        print_success "No security vulnerabilities found"
    else
        print_warning "Security vulnerabilities detected"
    fi

    echo ""
    print_info "Checking for outdated gems..."
    bundle outdated
}

# Rust audit
audit_rust() {
    print_section "Rust Dependency Audit"

    if ! command_exists cargo; then
        print_error "cargo not found. Please install Rust."
        return 1
    fi

    print_info "Checking for security vulnerabilities..."
    if command_exists cargo-audit; then
        if cargo audit; then
            print_success "No security vulnerabilities found"
        else
            print_warning "Security vulnerabilities detected"
        fi
    else
        print_warning "cargo-audit not installed. Run: cargo install cargo-audit"
    fi

    echo ""
    if command_exists cargo-outdated; then
        print_info "Checking for outdated crates..."
        cargo outdated
    else
        print_warning "cargo-outdated not installed. Run: cargo install cargo-outdated"
    fi
}

# Go audit
audit_go() {
    print_section "Go Dependency Audit"

    if ! command_exists go; then
        print_error "go not found. Please install Go."
        return 1
    fi

    print_info "Checking for security vulnerabilities..."
    if command_exists govulncheck; then
        if govulncheck ./...; then
            print_success "No security vulnerabilities found"
        else
            print_warning "Security vulnerabilities detected"
        fi
    else
        print_warning "govulncheck not installed. Run: go install golang.org/x/vuln/cmd/govulncheck@latest"
    fi

    echo ""
    print_info "Tidying dependencies..."
    go mod tidy
    print_success "Dependencies tidied"
}

# Main execution
PROJECT_TYPE=$(detect_project_type)

print_info "Detected project type: ${PROJECT_TYPE}"
echo ""

case "$PROJECT_TYPE" in
    nodejs)
        audit_nodejs
        ;;
    python)
        audit_python
        ;;
    ruby)
        audit_ruby
        ;;
    rust)
        audit_rust
        ;;
    go)
        audit_go
        ;;
    unknown)
        print_warning "Unable to detect project type."
        print_info "Please ensure you have one of the following files:"
        print_info "  - package.json (Node.js)"
        print_info "  - requirements.txt or pyproject.toml (Python)"
        print_info "  - Gemfile (Ruby)"
        print_info "  - Cargo.toml (Rust)"
        print_info "  - go.mod (Go)"
        exit 1
        ;;
    *)
        print_warning "Project type '${PROJECT_TYPE}' not fully supported yet."
        exit 1
        ;;
esac

echo ""
print_section "Audit Complete"
print_success "Dependency audit finished!"
echo ""
print_info "Next steps:"
print_info "  1. Review any warnings or errors above"
print_info "  2. Update outdated packages carefully"
print_info "  3. Fix security vulnerabilities immediately"
print_info "  4. Remove unused dependencies"
echo ""
