# CLI reference

## halyard scan

Scan a directory for hardcoded secrets.

```
halyard scan [--path PATH] [--format FORMAT] [--timeout SECONDS] [--min-severity LEVEL] [--exclude PATTERN]
```

| Flag | Default | Description |
|---|---|---|
| `--path` | `.` | Directory to scan |
| `--format` | `text` | `text`, `json`, or `sarif` |
| `--timeout` | `30` | Seconds per file before the scan is abandoned |
| `--min-severity` | `medium` | Lowest severity reported |
| `--exclude` | none | Glob pattern to skip. Repeat for multiple patterns |

## halyard version

Print the installed Halyard version.

```
halyard version
```
