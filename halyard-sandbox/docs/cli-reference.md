# CLI reference

## halyard scan

Scan a directory for hardcoded secrets.

```
halyard scan [--path PATH] [--format FORMAT] [--timeout SECONDS] [--min-severity LEVEL] [--exclude PATTERN] [--baseline PATH | --no-baseline]
```

| Flag | Default | Description |
|---|---|---|
| `--path` | `.` | Directory to scan |
| `--format` | `text` | `text`, `json`, or `sarif` |
| `--timeout` | `30` | Seconds per file before the scan is abandoned |
| `--min-severity` | `medium` | Lowest severity reported |
| `--exclude` | none | Glob pattern to skip. Repeat for multiple patterns |
| `--baseline` | `halyard-baseline.json` | Baseline file to load. The default is in the project root |
| `--no-baseline` | off | Ignore the baseline file for this run and report every finding |

If a baseline file exists, `halyard scan` suppresses every finding recorded in it and counts those findings separately in the summary line, for example `12 findings (3 new, 9 baselined)`. To set up a baseline, see [Adopt Halyard on an existing codebase](adopt-existing-codebase.md).

If the baseline file given with `--baseline PATH` doesn't exist, Halyard prints `warning: baseline file not found, scanning without a baseline` and scans without a baseline. The missing file doesn't affect the exit code.

`halyard scan` exits with `1` if it reports a new finding at or above `--min-severity`, and with `0` otherwise. Baselined findings never fail the scan.

## halyard baseline create

Scan the project and write every current finding to the baseline file.

```
halyard baseline create
```

## halyard baseline update

Add new findings to the existing baseline file.

```
halyard baseline update
```

## halyard version

Print the installed Halyard version.

```
halyard version
```
