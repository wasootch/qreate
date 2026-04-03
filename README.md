# qreate

A simple command-line QR code generator that renders QR codes directly in your terminal.

## Requirements

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) library

## Installation

Install the dependency:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python qr.py <text>
```

### Examples

Generate a QR code for a URL:

```bash
python qr.py https://example.com
```

Generate a QR code for plain text:

```bash
python qr.py "Hello, World!"
```

Multi-word input (no quotes needed):

```bash
python qr.py Hello World
```

The QR code will be rendered as ASCII art directly in the terminal.

## Optional: Make it globally callable

**macOS / Linux:**

```bash
chmod +x qr.py
ln -s /path/to/qreate/qr.py /usr/local/bin/qr
qr https://example.com
```

**Windows (PowerShell profile):**

```powershell
function qr { python C:\path\to\qreate\src\qr.py @args }
```

## License

Apache License 2.0 — see [LICENSE](LICENSE) for details.
