# Configure Halyard

You can configure Halyard with a `halyard.yml` file in your project root, or with CLI flags. CLI flags override the file.

## Create a config file

```yaml
timeout: 30
max_depth: 8
format: text
min_severity: medium
exclude:
  - node_modules/**
  - .git/**
  - "*.min.js"
baseline: halyard-baseline.json
```

## Settings

| Setting | Default | Description |
|---|---|---|
| `timeout` | `30` | Seconds before a single file scan is abandoned |
| `max_depth` | `8` | How many directory levels deep to scan |
| `format` | `text` | Output format: `text`, `json`, or `sarif` |
| `min_severity` | `medium` | Lowest severity reported: `low`, `medium`, `high`, `critical` |
| `exclude` | see above | Glob patterns to skip |
| `baseline` | `halyard-baseline.json` | Path to the baseline file of accepted findings. See [Adopt Halyard on an existing codebase](adopt-existing-codebase.md) |
