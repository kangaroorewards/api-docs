# Contributing to Kangaroo Rewards API Documentation

Thank you for your interest in improving the Kangaroo Rewards API documentation! This guide will help you contribute effectively.

## Table of Contents

- [Getting Started](#getting-started)
- [Documentation Structure](#documentation-structure)
- [Making Changes](#making-changes)
- [Style Guide](#style-guide)
- [Testing Your Changes](#testing-your-changes)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- Git installed on your machine
- Node.js and npm installed
- Aglio installed globally: `npm install -g aglio`
- A text editor (VS Code, Sublime Text, etc.)
- Basic knowledge of API Blueprint format

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/api-docs.git
   cd api-docs
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/kangaroorewards/api-docs.git
   ```

## Documentation Structure

The documentation is organized as follows:

```
api-docs/
├── src/                      # API Blueprint source files
│   ├── app_oauth.apib       # OAuth authentication
│   ├── rest_api.apib        # REST API overview
│   ├── rest_*.apib          # Individual resource endpoints
├── open_api/                 # OpenAPI specifications
├── api.apib                  # Main include file
├── README.md                 # Project documentation
├── QUICK_REFERENCE.md        # Quick reference guide
├── CHANGELOG.md              # Documentation changelog
└── CONTRIBUTING.md           # This file
```

### File Naming Conventions

- Use lowercase with underscores: `rest_customers.apib`
- Prefix resource files with `rest_`: `rest_offers.apib`
- Authentication files prefix with `app_`: `app_oauth.apib`

## Making Changes

### Types of Contributions

We welcome:

- **Typo fixes** - Grammar, spelling, and punctuation corrections
- **Clarifications** - Making existing content clearer
- **Examples** - Adding code examples and use cases
- **New sections** - Documenting new features or endpoints
- **Improvements** - Enhancing existing documentation structure

### Before Making Changes

1. Check existing issues to avoid duplicate work
2. Create an issue describing the change you want to make
3. Wait for feedback before starting major changes
4. Keep changes focused and minimal

### Making Your Changes

1. Create a feature branch:
   ```bash
   git checkout -b improve/description-of-change
   ```

2. Make your changes to the appropriate `.apib` files

3. Test your changes (see [Testing Your Changes](#testing-your-changes))

4. Commit with a clear message:
   ```bash
   git commit -m "Fix typo in OAuth documentation"
   ```

## Style Guide

### Writing Style

- **Be clear and concise** - Use simple language
- **Be consistent** - Follow existing patterns
- **Be specific** - Use concrete examples
- **Be complete** - Include all necessary information

### Formatting

#### Headers

Use appropriate header levels:
```markdown
# Main Section (h1)
## Subsection (h2)
### Sub-subsection (h3)
```

#### Code Blocks

Use language-specific syntax highlighting:

````markdown
```bash
curl -X GET https://api.kangaroorewards.com/customers
```

```json
{
  "data": {
    "id": "123",
    "email": "user@example.com"
  }
}
```
````

#### Tables

Use tables for structured data:

```markdown
| Parameter | Type | Description |
|-----------|------|-------------|
| id | string | Unique identifier |
| email | string | Email address |
```

#### Notes and Warnings

Use block quotes for important notes:

```markdown
>**Note:** This is an important note

>**Warning:** This is a critical warning
```

### API Blueprint Conventions

#### HTTP Methods

Always specify the HTTP method clearly:

```apib
### Create a customer [POST]
### Retrieve a customer [GET]
### Update a customer [PUT]
### Delete a customer [DELETE]
```

#### Parameters

Document all parameters with type and description:

```apib
**Path Parameters**
|Name|Type|Description|
|-----|----|-----------|
|id|string|Required. The unique ID of the customer|

**Query Parameters**
|Name|Type|Description|
|-----|----|-----------|
|page|integer|Optional. Page number for pagination|
```

#### Request/Response Examples

Include both request and response examples:

```apib
Example Request:
```
POST /customers HTTP/1.1
Host: api.kangaroorewards.com
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json

{"email": "user@example.com"}
```

Response Body:
```json
{
  "data": {
    "id": "123",
    "email": "user@example.com"
  }
}
```
```

### Code Examples

When adding code examples:

1. **Include multiple languages** when possible (PHP, Python, JavaScript, Ruby)
2. **Use realistic data** - Don't use "foo" or "bar"
3. **Include error handling** - Show how to handle failures
4. **Add comments** - Explain non-obvious code
5. **Test examples** - Ensure code actually works

Example:

```python
# Fetch customer with error handling
try:
    response = requests.get(
        f'{base_url}/customers/{customer_id}',
        headers=headers
    )
    response.raise_for_status()
    customer = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

## Testing Your Changes

### Generate HTML Documentation

Before submitting, generate the HTML documentation to verify your changes:

```bash
aglio --theme-full-width --theme-template triple -i api.apib -o docs.html
```

Open `docs.html` in your browser and verify:

- ✓ All formatting is correct
- ✓ Code examples display properly
- ✓ Tables render correctly
- ✓ Links work as expected
- ✓ No syntax errors

### Use Live Server (Optional)

For continuous testing during development:

```bash
aglio --theme-full-width --theme-template triple -i api.apib -s
```

This starts a server at `http://localhost:3000` with live reload.

### Validate API Blueprint

Ensure your API Blueprint syntax is valid:

```bash
# You may need to install drafter
npm install -g drafter

# Validate the blueprint
drafter api.apib
```

## Submitting Changes

### Update Documentation

1. Update `CHANGELOG.md` with your changes under [Unreleased]
2. Ensure README.md is updated if you added new major sections
3. Update QUICK_REFERENCE.md if you documented common operations

### Commit Messages

Write clear, descriptive commit messages:

**Good:**
- "Fix typo in OAuth password grant documentation"
- "Add Python examples for customer creation"
- "Improve error handling section with retry logic"

**Bad:**
- "Fixed stuff"
- "Update docs"
- "Changes"

### Pull Request

1. Push your changes to your fork:
   ```bash
   git push origin improve/description-of-change
   ```

2. Create a Pull Request on GitHub with:
   - **Clear title** - Describe what you changed
   - **Description** - Explain why the change is needed
   - **Screenshots** - Include if you changed rendered output
   - **Testing notes** - Describe how you tested

3. Link to any related issues

4. Wait for review and address feedback

### Pull Request Checklist

Before submitting, ensure:

- [ ] Changes follow the style guide
- [ ] All examples are tested and working
- [ ] HTML documentation renders correctly
- [ ] CHANGELOG.md is updated
- [ ] Commit messages are clear
- [ ] No unrelated changes included
- [ ] Documentation is spell-checked

## Reporting Issues

### Bug Reports

When reporting documentation bugs, include:

- **Location** - Which file and section
- **Current behavior** - What's wrong
- **Expected behavior** - What should it say
- **Screenshots** - If applicable

### Enhancement Requests

When suggesting improvements, include:

- **Problem** - What's unclear or missing
- **Proposed solution** - What should be added
- **Examples** - Show what you mean
- **Use case** - Why is this needed

## Questions?

If you have questions about contributing:

- Review existing documentation
- Check closed issues and PRs
- Open a new issue with the "question" label
- Contact Kangaroo Rewards support

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Other unethical or unprofessional conduct

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.

## Recognition

Contributors will be acknowledged in:
- Git commit history
- Pull request credits
- Release notes (for significant contributions)

Thank you for contributing to make the Kangaroo Rewards API documentation better for everyone!
