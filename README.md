# sing-box-subconverter-offline

A command-line tool encapsulates the functionality of [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe) project


### Build

- `pip install -r ./requirements.txt -r ./singbox_subscribe/requirements.txt`
- `pyinstaller --noconfirm --onefile --console -i "NONE" -p ./singbox_subscribe ./sing-box-subconverter.py`

### Usage

```bash
subconverter [-h] [--url URL] [--ua UA] [--path PATH] [--out OUT]
options:
  -h, --help   show this help message and exit
  --url URL    subscribe url
  --ua UA      User-Agent
  --path PATH  subscribe file path
  --out OUT    output file path
```
