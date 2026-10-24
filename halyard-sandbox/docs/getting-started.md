# Getting started with Halyard

Halyard scans your source code for hardcoded secrets such as API keys, tokens, and private keys.

## Prerequisites

- Python 3.9 or later
- pip

## Install Halyard

```
pip install halyard
```

## Run your first scan

1. Open a terminal in your project root.
2. Run:

   ```
   halyard scan --path .
   ```

3. Review the findings. Each finding shows the file, line number, secret type, and severity.

## Verify the install

```
halyard version
```

You should see `halyard 1.4.0`.

## Next steps

- [Configure Halyard](configuration.md)
- [Adopt Halyard on an existing codebase](adopt-existing-codebase.md)
- [CLI reference](cli-reference.md)
