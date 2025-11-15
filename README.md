# Kangaroo Rewards API Documentation

[![API Documentation](https://img.shields.io/badge/API-Documentation-blue)](https://api.kangaroorewards.com/docs)

Welcome to the Kangaroo Rewards API documentation repository. This repository contains comprehensive documentation for integrating with the Kangaroo Rewards platform using our REST API.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Documentation Structure](#documentation-structure)
- [Generating Documentation](#generating-documentation)
- [API Resources](#api-resources)
- [Contributing](#contributing)
- [Support](#support)

## Overview

The Kangaroo Rewards API uses HTTP methods and a RESTful endpoint structure with OAuth 2.0 authorization. All requests and responses are formatted in JSON, making it easy to integrate with any programming language.

**Official Documentation:** [https://api.kangaroorewards.com/docs](https://api.kangaroorewards.com/docs)

## Prerequisites

Before you begin, ensure you have:

- A Kangaroo Rewards Developer account - [Sign up for free](https://api.kangaroorewards.com/developers)
- Node.js and npm installed (for generating HTML documentation)
- Aglio installed globally: `npm install -g aglio`
- Basic understanding of REST APIs and OAuth 2.0

## Quick Start

1. **Clone this repository:**
   ```bash
   git clone https://github.com/kangaroorewards/api-docs.git
   cd api-docs
   ```

2. **Generate HTML documentation:**
   ```bash
   aglio --theme-full-width --theme-template triple -i api.apib -o docs.html
   ```

3. **View the documentation:**
   Open `docs.html` in your web browser to view the complete API documentation.

## Documentation Structure

```
api-docs/
├── src/                          # Source API Blueprint files
│   ├── app_oauth.apib           # OAuth authentication
│   ├── rest_api.apib            # REST API overview
│   ├── rest_customers.apib      # Customer endpoints
│   ├── rest_transactions.apib   # Transaction endpoints
│   └── ...                      # Other resource endpoints
├── open_api/                     # OpenAPI specifications
│   └── v2/                      # Version 2 specifications
├── api.apib                      # Main API Blueprint file
└── README.md                    # This file
```

## Generating Documentation

### Generate HTML Documentation

Generate a full-width HTML documentation file:

```bash
aglio --theme-full-width --theme-template triple -i api.apib -o docs.html
```

### Generate Documentation in a Specific Folder

Specify a custom output path:

```bash
aglio --theme-full-width --theme-template triple -i api.apib -o path/to/business.html
```

### Watch Mode (Auto-regenerate on changes)

For development, use watch mode to automatically regenerate documentation when files change:

```bash
aglio --theme-full-width --theme-template triple -i api.apib -s
```

This starts a local server at `http://localhost:3000` with live reload.

## API Resources

The Kangaroo Rewards API provides access to the following resources:

- **Authentication** - OAuth 2.0 (Authorization Code & Password Grant flows)
- **Customers** - Manage customer profiles and loyalty accounts
- **Transactions** - Track purchases, rewards, and redemptions
- **Offers** - Create and manage promotional offers
- **Rewards** - Configure reward catalog and redemptions
- **Products** - Manage product catalog
- **Branches** - Handle multi-location businesses
- **Tiers** - Implement tiered loyalty programs
- **Workflows** - Automate marketing and engagement
- **Reviews** - Collect and manage customer feedback

For detailed endpoint documentation, visit [https://api.kangaroorewards.com/docs](https://api.kangaroorewards.com/docs)

## SDKs and Libraries

Official SDKs are available to simplify integration:

- **PHP SDK** - [KangarooRewards-PHP-SDK](https://github.com/kangaroorewards/KangarooRewards-PHP-SDK)
- **OAuth2 Client** - [OAuth2 Kangaroo Rewards](https://github.com/kangaroorewards/oauth2-kangaroo-rewards)
- **Sample App** - [REST API Sample App (PHP)](https://github.com/kangaroorewards/rest-api-sample-app-php)

## Contributing

We welcome contributions to improve our documentation! If you find errors, typos, or areas that need clarification:

1. Fork this repository
2. Create a feature branch (`git checkout -b improve-docs`)
3. Make your changes
4. Test by generating the HTML documentation
5. Commit your changes (`git commit -am 'Improve documentation for X'`)
6. Push to the branch (`git push origin improve-docs`)
7. Create a Pull Request

### Documentation Guidelines

- Use clear, concise language
- Include practical examples for all endpoints
- Follow the existing API Blueprint format
- Test all code examples before submitting
- Keep formatting consistent across files

## Support

- **Developer Portal:** [https://api.kangaroorewards.com/developers](https://api.kangaroorewards.com/developers)
- **Tutorials & Guides:** [API Documentation Wiki](https://github.com/kangaroorewards/api-docs/wiki)
- **Technical Support:** Contact Kangaroo Rewards Support
- **Report Issues:** [GitHub Issues](https://github.com/kangaroorewards/api-docs/issues)

## License

Copyright © Kangaroo Rewards. All rights reserved.