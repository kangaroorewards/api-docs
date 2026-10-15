# Kangaroo Rewards API documentation

[Docs](https://api.kangaroorewards.com/docs)

## SDK release process

This repository is the source of truth for the OpenAPI specification. API
specification changes and releases feed the Kangaroo SDK release pipeline.
Follow the [Kangaroo SDK Release Pipeline Runbook](https://github.com/kangaroorewards/Kangaroo-App-SDK/blob/main/docs/release_pipeline_runbook.md)
for the required release sequence, automated spec-pin update, and downstream
SDK and Flutter publication steps.

Generate HTML

```
aglio --theme-full-width --theme-template triple -i api.apib -o docs.html
```

Generate HTML in specific folder
```
aglio --theme-full-width --theme-template triple -i api.apib -o business.html
```