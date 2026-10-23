# Getting started with Halyard

Halyard scans your source code for hardcoded secrets such as API keys, tokens, and private keys.

## Prerequisites

- Python 3.10 or later. Halyard 1.5 and later don't support Python 3.9; if you're on Python 3.9, use Halyard 1.4.
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
- [CLI reference](cli-reference.md)
