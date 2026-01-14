# Dependency Management Guidelines

## Quick Reference for Adding Dependencies

### Before Adding Any Dependency

Ask yourself these questions:

1. **Is it really needed?**
   - Can I implement this in <1 hour with native code?
   - Am I using this to avoid writing 10 lines of code?

2. **Is it maintained?**
   - Last commit within 6 months?
   - Active issue resolution?
   - Compatible with current language/framework versions?

3. **Is it trustworthy?**
   - Reputable author/organization?
   - Good download statistics?
   - No recent security incidents?

4. **Is it lightweight?**
   - Reasonable dependency tree?
   - Acceptable bundle size impact?

### Red Flags 🚩

- No activity in over 1 year
- Numerous unresolved security issues
- Deprecated or archived repository
- Excessive dependencies (dependency hell)
- Poor documentation
- No tests in repository
- License incompatibility
- Too new (<3 months old for critical functionality)

### Green Flags ✅

- Active maintenance (commits within 3 months)
- Clear documentation
- Comprehensive test coverage
- Used by major projects
- Responsive to security issues
- Semantic versioning
- Compatible license
- Reasonable size and scope

---

## Language-Specific Commands

### Node.js / npm

```bash
# Install dependency
npm install <package-name>

# Install dev dependency
npm install --save-dev <package-name>

# Check for security vulnerabilities
npm audit

# Fix vulnerabilities automatically
npm audit fix

# Check for outdated packages
npm outdated

# Update packages
npx npm-check-updates -u

# Find unused dependencies
npx depcheck
```

### Python / pip

```bash
# Install dependency
pip install <package-name>

# Generate requirements file
pip freeze > requirements.txt

# Check for security vulnerabilities
pip install safety
safety check

# Check for outdated packages
pip list --outdated

# Update package
pip install --upgrade <package-name>

# Audit Python packages
pip install pip-audit
pip-audit
```

### Ruby / bundler

```bash
# Install dependency
bundle add <gem-name>

# Check for security vulnerabilities
bundle audit

# Update dependencies
bundle update

# Check outdated gems
bundle outdated
```

### Go

```bash
# Add dependency
go get <package-name>

# Update dependencies
go get -u

# Security check
go list -json -m all | nancy sleuth

# Tidy dependencies
go mod tidy
```

### Rust / cargo

```bash
# Add dependency
cargo add <crate-name>

# Check for vulnerabilities
cargo install cargo-audit
cargo audit

# Update dependencies
cargo update

# Check outdated
cargo install cargo-outdated
cargo outdated
```

---

## Automated Checks

### GitHub Actions Example

```yaml
name: Dependency Audit

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    # Run weekly on Mondays
    - cron: '0 0 * * 1'

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # Node.js example
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run security audit
        run: npm audit --audit-level=moderate

      - name: Check for outdated packages
        run: npm outdated || true
```

---

## Dependabot Configuration

Create `.github/dependabot.yml`:

```yaml
version: 2
updates:
  # Enable version updates for npm
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    reviewers:
      - "team-reviewers"
    labels:
      - "dependencies"
      - "automated"

  # Group minor and patch updates
    groups:
      development-dependencies:
        dependency-type: "development"
      production-dependencies:
        dependency-type: "production"
```

---

## Dependency Review Checklist

### For Code Reviews

When reviewing a PR that adds dependencies:

- [ ] Is the dependency necessary?
- [ ] Has the repository been checked for activity?
- [ ] Are there security vulnerabilities?
- [ ] Is the license compatible?
- [ ] Is the dependency size reasonable?
- [ ] Are version constraints appropriate?
- [ ] Is the dependency documented in code comments or docs?

### Monthly Audit

- [ ] Run security audit (`npm audit`, `safety check`, etc.)
- [ ] Check for outdated packages
- [ ] Review dependency tree for bloat
- [ ] Verify all dependencies are still used
- [ ] Update lock files
- [ ] Test after updates

---

## Version Pinning Strategy

### Production Dependencies

```json
{
  "dependencies": {
    // Critical security packages - pin exactly
    "jsonwebtoken": "9.0.0",

    // Stable APIs - allow patch updates
    "express": "~4.18.0",

    // Active development - allow minor updates
    "react": "^18.2.0"
  }
}
```

### Development Dependencies

```json
{
  "devDependencies": {
    // Build tools - allow minor updates
    "webpack": "^5.75.0",

    // Testing tools - allow minor updates
    "jest": "^29.3.0"
  }
}
```

---

## When to Remove a Dependency

Remove a dependency when:

1. **No longer used** - Dead code was removed
2. **Abandoned** - No activity in 18+ months
3. **Replaced** - Better alternative found
4. **Bloat** - Functionality is trivial to implement
5. **Security** - Unpatched vulnerabilities
6. **License change** - Incompatible license

---

## Alternatives to Consider

Before adding a dependency, check if native solutions exist:

### JavaScript/Node.js

| Instead of | Use Native |
|------------|-----------|
| `lodash/get` | Optional chaining `?.` |
| `lodash/merge` | Object spread `{...a, ...b}` |
| `moment` | `Intl.DateTimeFormat` or `Date` |
| `axios` | `fetch` API |
| `left-pad` | `String.padStart()` |
| `is-array` | `Array.isArray()` |

### Python

| Instead of | Use Native |
|------------|-----------|
| `dateutil` | `datetime` module |
| `simplejson` | `json` module |
| Custom validators | `dataclasses` with type hints |

---

## Resources

### Security Databases
- [CVE Database](https://cve.mitre.org/)
- [GitHub Advisory Database](https://github.com/advisories)
- [Snyk Vulnerability DB](https://security.snyk.io/)
- [npm Security Advisories](https://www.npmjs.com/advisories)

### Tools
- [Snyk](https://snyk.io/) - Security scanning
- [Socket.dev](https://socket.dev/) - Supply chain security
- [Dependabot](https://github.com/dependabot) - Automated updates
- [Renovate](https://renovatebot.com/) - Advanced update management

### Documentation
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [npm audit docs](https://docs.npmjs.com/cli/v9/commands/npm-audit)
- [Python Safety docs](https://pyup.io/safety/)

---

## Getting Help

If you're unsure about a dependency:

1. Check the dependency's GitHub repository
2. Search for security advisories
3. Ask the team in PR comments
4. Consult the tech lead
5. Document your decision in comments

---

**Remember:** Every dependency is a trade-off between functionality and maintenance burden. Choose wisely.
