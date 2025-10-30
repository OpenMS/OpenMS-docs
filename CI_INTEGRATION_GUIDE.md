# Suggested CI/CD Enhancement: Documentation Linting

This document provides instructions for integrating the `lint_docs.py` script into the existing GitHub Actions workflow.

## Option 1: Add to Existing Workflow (Recommended)

Add a linting step to `.github/workflows/main.yml` before the Sphinx build:

```yaml
# Add this step after "Install dependencies" and before "Run sphinx build"
- name: Lint documentation
  run: python3 lint_docs.py
```

### Complete modified section:
```yaml
# install deps
- name: Install dependencies
  run: pip install -r requirements.txt

# NEW: Lint documentation for consistency
- name: Lint documentation
  run: python3 lint_docs.py

# build docs. "-n" for nitpick link checking
- name: Run sphinx build. No warnings allowed but keep going.
  run: sphinx-build -M html ./docs build -W --keep-going -n
```

## Option 2: Separate Linting Workflow

Create `.github/workflows/lint.yml`:

```yaml
name: Documentation Lint

on:
  pull_request:
    paths:
      - 'docs/**'
      - '*.md'
      - '*.rst'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Lint documentation
        run: python3 lint_docs.py
      
      - name: Comment on PR
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '⚠️ Documentation linting failed. Please run `python3 lint_docs.py` locally and fix the issues.'
            })
```

## Option 3: Pre-commit Hook (Local Development)

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: lint-docs
        name: Lint OpenMS Documentation
        entry: python3 lint_docs.py
        language: system
        pass_filenames: false
        files: \.(md|rst)$
```

Then contributors can install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## Benefits of CI Integration

1. **Automated checks**: Catches style issues before merge
2. **Consistency**: Ensures all contributors follow the same standards
3. **Educational**: Provides immediate feedback to contributors
4. **Maintainability**: Reduces manual review burden

## Linter Exit Codes

- `0`: No errors found
- `1`: Errors found (will fail CI build)

## Current Checks

The linter currently checks for:
- ✅ Trailing whitespace
- ✅ Insecure HTTP links
- ✅ Inconsistent terminology
- ✅ TODO/FIXME comments

## Future Enhancements

Consider adding additional tools:
1. **markdownlint** - Markdown style checking
2. **proselint** - Prose quality checking
3. **codespell** - Spell checking
4. **vale** - Style guide enforcement

## Testing the Linter

Test locally before committing:
```bash
# Run linter
python3 lint_docs.py

# Build documentation
make html

# Both should pass before creating a PR
```

## Recommendation

Start with **Option 1** (adding to existing workflow) as it:
- Requires minimal changes
- Provides immediate feedback
- Doesn't add extra CI complexity
- Can be easily removed if needed

The linter is non-disruptive since it currently passes with no errors on the codebase.
