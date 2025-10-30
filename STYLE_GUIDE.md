# OpenMS Documentation Style Guide

This document supplements the [Contributing Guidelines](.github/CONTRIBUTING.md) with specific style conventions for OpenMS documentation.

## Terminology and Capitalization

### Product and Technology Names

Use proper capitalization for all OpenMS-related products and technologies:

- **OpenMS** - Always capitalize both 'O' and 'MS'. Never use 'openMS', 'Openms', or 'openms' (except in URLs or file paths)
- **pyOpenMS** - Python bindings, with lowercase 'py' prefix
- **TOPP** (The OpenMS Proteomics Pipeline) - Always in all caps
- **TOPPView** - Visualization tool, with camelCase
- **KNIME** - Always in all caps

### File Formats and Technical Terms

- **mzML**, **mzTab** - Lowercase 'mz' followed by format name
- **LC-MS** - Use hyphen, both parts capitalized
- Use {term}\`technical term\` for glossary references

## Links and URLs

- **Always use HTTPS** instead of HTTP where available
- For external links, verify they work before committing
- Use reference-style links for frequently used URLs
- Format: `[Link Text](https://example.com)`

## Code and File References

- Use backticks for code, commands, and file paths: \`filename.txt\`
- Use {path}\`path,to,file\` for OpenMS-specific path references
- Always specify language for code blocks:

\`\`\`python
print("Hello OpenMS")
\`\`\`

## Whitespace and Formatting

- **No trailing whitespace** - Lines should not end with spaces or tabs
- **Line length**: Maximum 120 characters (soft limit)
- **Blank lines**: Use one blank line between sections
- Use UTF-8 encoding for all files

## Images and Figures

- Always provide descriptive alt text: `![Descriptive text](path/to/image.png)`
- Reference figures with anchors: `(Figure_1)=` and `<a href="#figure-1">Figure 1</a>`
- Store images in `docs/_images/` with descriptive subdirectories

## Admonitions

Use appropriate admonition types:

\`\`\`markdown
\`\`\`{note}
Important information for readers
\`\`\`

\`\`\`{warning}
Critical warnings about potential issues
\`\`\`

\`\`\`{tip}
Helpful tips and best practices
\`\`\`
\`\`\`

## Version References

- Reference "latest" for stable releases
- Reference "develop" for development version
- Be explicit about version requirements when necessary

## Common Mistakes to Avoid

1. ❌ `openMS` → ✅ `OpenMS`
2. ❌ `Toppview` → ✅ `TOPPView`
3. ❌ `http://example.com` → ✅ `https://example.com`
4. ❌ Trailing spaces → ✅ Clean line endings
5. ❌ `TODO: fix this` → ✅ Open an issue instead

## Tools

- Use `.editorconfig` file settings in your editor
- Run `make html` to build and check documentation locally
- Check for broken links before committing

## Questions?

Join us on [Discord](https://discord.gg/aJyWqf6uCn) or [GitHub Discussions](https://github.com/OpenMS/OpenMS-docs/discussions).
