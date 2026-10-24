# Adopt Halyard on an existing codebase

The first scan of an existing codebase often reports many findings that your team has already reviewed and accepted. A baseline file records those findings so that `halyard scan` reports only new ones. You can then run Halyard in CI without the scan failing on findings you've already accepted.

This page assumes you've installed Halyard and run a scan. If you haven't, see [Getting started with Halyard](getting-started.md).

## How a baseline works

The baseline file, `halyard-baseline.json` in your project root by default, lists a fingerprint for each accepted finding. A fingerprint is a hash of the finding's rule ID, file path, and matched text.

When a baseline file exists, `halyard scan` loads it and suppresses every finding whose fingerprint is in it. The summary line counts new and baselined findings separately, for example `12 findings (3 new, 9 baselined)`. The scan fails only on new findings at or above `min_severity`.

If you point Halyard at a baseline file that doesn't exist, for example because of a typo in the path, the scan prints a warning and continues without a baseline, so the missing file doesn't fail CI by itself but your accepted findings are no longer suppressed.

Because the file path is part of the fingerprint, moving a baselined secret to another file creates a new finding.

## Create a baseline

1. Run a scan and review the findings. Remove or rotate any secret you don't want to accept.
2. In your project root, run:

   ```
   halyard baseline create
   ```

   Halyard writes every current finding to `halyard-baseline.json`.

3. Commit `halyard-baseline.json` to your repository so that CI and your teammates use the same baseline.

To keep the baseline somewhere else, set `baseline` in `halyard.yml`. See [Configure Halyard](configuration.md).

## Run Halyard in CI

Add `halyard scan` to your CI job. The scan exits with `1` if it finds a new finding at or above `min_severity`, and with `0` otherwise. The job fails only on findings that aren't in the baseline.

## Accept new findings

When your team reviews a new finding and decides to accept it, add it to the baseline:

```
halyard baseline update
```

Commit the updated `halyard-baseline.json`.

## Review every finding

To see all findings, including baselined ones, run:

```
halyard scan --no-baseline
```
