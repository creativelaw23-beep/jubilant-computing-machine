# jubilant-computing-machine

An interactive Constitution Quiz Application with comprehensive dependency management and security auditing infrastructure.

## 📋 Overview

This repository contains an interactive educational application for testing knowledge about the structure of the Russian Constitution (Конституция РФ). The project is configured with best-in-class dependency management practices, automated security scanning, and comprehensive audit tooling.

## 🎓 Constitution Quiz Application

### Features

- **Interactive Quiz**: Multiple choice questions about Russian Constitution structure
- **Difficulty Levels**: Easy, Medium, and Hard difficulty modes
- **Random Questions**: Get a random selection of questions
- **Detailed Feedback**: Explanations for each answer
- **Score Tracking**: See your performance metrics
- **Education Information**: Learn about Constitution structure

### Getting Started

#### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only built-in Python modules)

#### Installation

```bash
# Clone the repository
git clone <repository-url>
cd jubilant-computing-machine

# No package installation needed - no external dependencies!
```

#### Running the Quiz

```bash
# Method 1: Using main.py
python main.py

# Method 2: Using the quiz module directly
python -m src.quiz.app
```

### Usage

The application provides an interactive menu with the following options:

1. **Start Full Quiz** - Answer all 12 questions
2. **Difficulty-Based Quiz** - Choose between Easy, Medium, or Hard
3. **Random Questions** - Select how many questions you want
4. **Constitution Info** - Learn about the Constitution structure
5. **Exit** - Close the application

### Quiz Structure

The quiz includes 12 questions covering:
- Constitution adoption date and process
- Constitution structure and chapters
- Government branches and organs
- Federal structure
- Rights and freedoms
- Constitutional amendments

### Question Difficulty Distribution

- **Easy (3 questions)**: Basic facts about Constitution
- **Medium (4 questions)**: Structure of government
- **Hard (5 questions)**: Complex concepts and specific details

### Example Output

```
======================================================================
                    ИНТЕРАКТИВНАЯ ВИКТОРИНА
              Проверка знаний о Конституции РФ
======================================================================

📚 ГЛАВНОЕ МЕНЮ
--------------------------------------------------
1️⃣  Начать викторину (все вопросы)
2️⃣  Викторина по уровню сложности
3️⃣  Случайные вопросы (N вопросов)
4️⃣  Справка о Конституции
5️⃣  Выход
--------------------------------------------------
```

## 🔒 Security & Dependency Management

### Automated Tools Configured

- **Dependabot**: Automated dependency updates (see `.github/dependabot.yml`)
- **GitHub Actions**: Automated security audits on every push and weekly schedule (see `.github/workflows/dependency-audit.yml`)
- **Manual Audit Script**: Cross-platform dependency auditing tool (see `scripts/audit-dependencies.sh`)

### Documentation

- **[DEPENDENCY_AUDIT.md](DEPENDENCY_AUDIT.md)**: Complete guide to dependency management best practices
- **[DEPENDENCY_CHECKLIST.md](DEPENDENCY_CHECKLIST.md)**: Quick reference checklist for daily/weekly/monthly maintenance

## 🚀 Quick Start

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
├── src/
│   └── quiz/
│       ├── __init__.py             # Quiz package initialization
│       ├── app.py                  # Main quiz application
│       └── questions.py            # Quiz questions and data
├── scripts/
│   └── audit-dependencies.sh       # Manual audit script
├── main.py                         # Application entry point
├── requirements.txt                # Python dependencies (empty for this project)
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
