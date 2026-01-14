# Dependency Management Checklist

Use this checklist when adding, updating, or reviewing dependencies.

---

## ✅ Before Adding a New Dependency

- [ ] Is this dependency really necessary? Can we use a built-in alternative?
- [ ] Is the package actively maintained? (Check last commit date)
- [ ] Does it have good documentation?
- [ ] Is it widely used? (Check download stats, GitHub stars)
- [ ] What's the package size? (Use `npx package-size` for npm)
- [ ] How many transitive dependencies does it add?
- [ ] Is the license compatible with our project?
- [ ] Are there known security vulnerabilities?
- [ ] Are there better alternatives?

**Tools to check:**
```bash
# Node.js
npx package-size <package-name>
npm info <package-name>

# Python
pip show <package-name>

# Check security
npx snyk test <package-name>
```

---

## ✅ Weekly Maintenance Tasks

- [ ] Run security audit
  - `npm audit` (Node.js)
  - `pip-audit` (Python)
  - `bundle audit` (Ruby)
  - `cargo audit` (Rust)
- [ ] Check for critical security updates
- [ ] Review and merge Dependabot PRs
- [ ] Check CI/CD pipeline status

---

## ✅ Monthly Maintenance Tasks

- [ ] Check for outdated packages
  - `npm outdated` (Node.js)
  - `pip list --outdated` (Python)
  - `bundle outdated` (Ruby)
  - `cargo outdated` (Rust)
- [ ] Review minor version updates
- [ ] Update non-breaking changes
- [ ] Review dependency tree for duplicates
  - `npm dedupe` (Node.js)
- [ ] Check for unused dependencies
  - `npx depcheck` (Node.js)
  - `pip-autoremove` (Python)
- [ ] Review package sizes and bundle impact

---

## ✅ Quarterly Maintenance Tasks

- [ ] Evaluate major version updates
- [ ] Review all dependencies for:
  - Deprecation notices
  - Better alternatives
  - Continued maintenance
- [ ] Audit entire dependency tree
- [ ] Review license compliance
- [ ] Update documentation on dependency decisions
- [ ] Performance benchmarks after updates
- [ ] Full regression testing

---

## ✅ Before Major Release

- [ ] All dependencies up to date with security patches
- [ ] No known high/critical vulnerabilities
- [ ] Lock files committed and up to date
- [ ] Dependency documentation updated
- [ ] License compliance verified
- [ ] CI/CD passing all security checks
- [ ] Changelog updated with dependency changes

---

## ✅ After Adding/Updating Dependencies

- [ ] Run full test suite
- [ ] Test in production-like environment
- [ ] Verify bundle size hasn't increased significantly
- [ ] Update documentation if behavior changed
- [ ] Commit lock files
- [ ] Update changelog if significant

---

## 🚨 Security Vulnerability Response

When a vulnerability is discovered:

1. [ ] Assess severity (Critical/High/Medium/Low)
2. [ ] Check if vulnerability affects your usage
3. [ ] Review available patches/updates
4. [ ] If critical: Update immediately
5. [ ] If high: Update within 24-48 hours
6. [ ] If medium/low: Schedule in next sprint
7. [ ] Test thoroughly after update
8. [ ] Document the issue and resolution
9. [ ] Review similar dependencies

---

## 🔍 Red Flags to Watch For

- ⚠️ Package hasn't been updated in 2+ years
- ⚠️ Multiple unresolved security issues
- ⚠️ Maintainer is unreachable
- ⚠️ Package has < 100 weekly downloads (for npm)
- ⚠️ Package size > 10MB for simple functionality
- ⚠️ Deep dependency tree (10+ levels)
- ⚠️ Deprecated package
- ⚠️ License incompatibility
- ⚠️ No tests in the package
- ⚠️ Poor or no documentation

---

## 📊 Metrics to Track

Keep a log of:
- Total number of direct dependencies
- Total number of transitive dependencies
- Number of security vulnerabilities (by severity)
- Average dependency age
- Bundle size trends
- Dependency update frequency
- Time to resolve security issues

---

## 🛠️ Useful Commands

### Node.js/npm
```bash
npm audit                     # Security audit
npm audit fix                 # Auto-fix vulnerabilities
npm outdated                  # Check outdated packages
npm ls --depth=0              # List direct dependencies
npx depcheck                  # Find unused dependencies
npm dedupe                    # Remove duplicate dependencies
npx npm-check-updates         # Check for updates
npx license-checker           # Check licenses
```

### Python/pip
```bash
pip-audit                     # Security audit
pip list --outdated           # Check outdated packages
pipdeptree                    # Show dependency tree
pip-autoremove <package>      # Remove with dependencies
pip-licenses                  # Check licenses
safety check                  # Alternative security check
```

### Ruby/bundler
```bash
bundle audit                  # Security audit
bundle outdated               # Check outdated gems
bundle clean                  # Remove unused gems
bundle viz                    # Visualize dependencies
```

### Rust/cargo
```bash
cargo audit                   # Security audit
cargo outdated                # Check outdated crates
cargo tree                    # Show dependency tree
cargo upgrade                 # Upgrade dependencies
```

---

## 📝 Decision Log Template

When adding a dependency, document:

**Dependency:** [name]
**Version:** [version]
**Date Added:** [date]
**Added By:** [developer]
**Purpose:** [why it's needed]
**Alternatives Considered:** [list]
**Package Size:** [size]
**Dependencies Added:** [count]
**License:** [license type]
**Security Scan:** ✅ Passed / ⚠️ Issues found
**Review Date:** [when to review again]

---

**Last Updated:** 2026-01-14
