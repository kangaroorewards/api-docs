# Kangaroo Rewards API documentation

[Docs](https://api.kangaroorewards.com/docs)

## SDK release process

This repository is the source of truth for the OpenAPI specification. API
specification changes and releases feed the Kangaroo SDK release pipeline.
Follow the [Kangaroo SDK Release Pipeline Runbook](https://github.com/kangaroorewards/Kangaroo-App-SDK/blob/main/docs/release_pipeline_runbook.md)
for the required release sequence, automated spec-pin update, and downstream
SDK and Flutter publication steps.

Use a Conventional Commit (`fix: ...` for a correction, `feat: ...` for a new
capability) on `master`, then review and merge the release-please version/changelog
PR. The release workflow explicitly calls the SDK notifier after creating a
release; it does not rely on a release event from `GITHUB_TOKEN`. Manually
published releases also notify the SDK.

To retry a missed notification, run **Notify Kangaroo-App-SDK of a new release**
from Actions on `master`, supplying the existing published tag (for example,
`v0.0.685`). This sends the notification again without recreating the release
or changing its tag. The notifier requires `SDK_REPO_DISPATCH_TOKEN` with
Contents write access to `kangaroorewards/Kangaroo-App-SDK`.

The SDK bot opens a spec-pin PR and explicitly starts the SDK build on its
branch, including Apple validation without publication. Review the API changes
and the validation run for the latest PR commit before merging that PR.

Generate HTML

```
aglio --theme-full-width --theme-template triple -i api.apib -o docs.html
```

Generate HTML in specific folder
```
aglio --theme-full-width --theme-template triple -i api.apib -o business.html
```