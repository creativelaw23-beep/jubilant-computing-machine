# jubilant-computing-machine

Bitcoin Price Telegram Alert Application with comprehensive dependency management and security auditing infrastructure.

## 📋 Overview

A Python application that monitors Bitcoin price and sends Telegram notifications 4 times per day. Configured with best-in-class dependency management practices, automated security scanning, and comprehensive audit tooling.

## 🔒 Security & Dependency Management

### Automated Tools Configured

- **Dependabot**: Automated dependency updates (see `.github/dependabot.yml`)
- **GitHub Actions**: Automated security audits on every push and weekly schedule (see `.github/workflows/dependency-audit.yml`)
- **Manual Audit Script**: Cross-platform dependency auditing tool (see `scripts/audit-dependencies.sh`)

### Documentation

- **[DEPENDENCY_AUDIT.md](DEPENDENCY_AUDIT.md)**: Complete guide to dependency management best practices
- **[DEPENDENCY_CHECKLIST.md](DEPENDENCY_CHECKLIST.md)**: Quick reference checklist for daily/weekly/monthly maintenance

## 🚀 Bitcoin Price Monitor Quick Start

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from @BotFather)
- Your Telegram Chat ID

### Installation & Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run setup script (interactive configuration)
python setup.py

# 3. Run the application
python app.py
```

The application will send Bitcoin price notifications at:
- 06:00 UTC
- 12:00 UTC
- 18:00 UTC
- 23:00 UTC

For detailed setup instructions, see [README_APP.md](README_APP.md)

## 🔒 Dependency Management Quick Start

### Running Manual Dependency Audit

```bash
# Make script executable (first time only)
chmod +x scripts/audit-dependencies.sh

# Run audit
./scripts/audit-dependencies.sh
```

This will check for:
- Security vulnerabilities
- Outdated packages
- Unused dependencies
- License compliance issues

Reports are saved to `dependency-audit-reports/` directory.

### Supported Package Managers

The audit infrastructure supports:
- **Node.js** (npm, yarn, pnpm)
- **Python** (pip, pipenv, poetry)
- **Ruby** (bundler)
- **Rust** (cargo)
- **Go** (go modules)

## 📊 Continuous Monitoring

### GitHub Actions Workflows

The repository includes automated workflows that run:
- On every push to main/master/develop branches
- On every pull request
- Every Monday at 8am UTC (scheduled)
- On manual trigger

### Dependabot

Configured to:
- Check for updates weekly
- Create PRs for security patches
- Support multiple package ecosystems
- Auto-label dependency PRs

## 📖 Best Practices

### Before Adding Dependencies

1. ✅ Review the [DEPENDENCY_CHECKLIST.md](DEPENDENCY_CHECKLIST.md)
2. ✅ Evaluate if the dependency is truly needed
3. ✅ Check package size and dependency tree
4. ✅ Verify license compatibility
5. ✅ Scan for known vulnerabilities

### Regular Maintenance

- **Weekly**: Security audit, review Dependabot PRs
- **Monthly**: Check outdated packages, update minor versions
- **Quarterly**: Major version updates, full dependency review

## 🛠️ Useful Commands

### Security Audits
```bash
# Node.js
npm audit

# Python
pip-audit

# Ruby
bundle audit

# Rust
cargo audit

# Go
govulncheck ./...
```

### Check Outdated Packages
```bash
# Node.js
npm outdated

# Python
pip list --outdated

# Ruby
bundle outdated

# Rust
cargo outdated

# Go
go list -u -m all
```

### Check Unused Dependencies
```bash
# Node.js
npx depcheck

# Python
pip-autoremove <package>
```

## 📁 Repository Structure

```
.
├── .github/
│   ├── dependabot.yml              # Dependabot configuration
│   └── workflows/
│       └── dependency-audit.yml    # CI/CD security audit workflow
├── scripts/
│   └── audit-dependencies.sh       # Manual audit script
├── DEPENDENCY_AUDIT.md             # Comprehensive dependency guide
├── DEPENDENCY_CHECKLIST.md         # Quick reference checklist
└── README.md                       # This file
```

## 🔍 Vulnerability Response

When a vulnerability is discovered:

1. **Assess severity** (Critical/High/Medium/Low)
2. **Critical**: Update immediately
3. **High**: Update within 24-48 hours
4. **Medium/Low**: Schedule in next sprint
5. **Test thoroughly** after updates
6. **Document** the issue and resolution

## 📚 Resources

- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [Snyk Vulnerability Database](https://security.snyk.io/)
- [GitHub Advisory Database](https://github.com/advisories)
- [npm Security Best Practices](https://docs.npmjs.com/packages-and-modules/securing-your-code)

## 🤝 Contributing

When contributing to this repository:

1. Follow the dependency checklist before adding new packages
2. Ensure all security audits pass
3. Update documentation if adding new dependencies
4. Include rationale for dependency additions in PRs

## 📝 License

[Add your license here]

---

**Note**: This repository includes comprehensive dependency management infrastructure even before code is added. This ensures security and maintainability from day one of development.
