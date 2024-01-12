# sing-box-subconverter-offline

A command-line tool encapsulates the functionality of [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe) project


### Build

```bash
git clone https://github.com/GUI-for-Cores/sing-box-subconverter-offline.git

cd sing-box-subconverter-offline
git submodule update --init --recursive

cd singbox_subscribe
git apply ../print-header.patch
cd ..

pip install -r ./requirements.txt -r ./singbox_subscribe/requirements.txt
pyinstaller --noconfirm --onefile --console -i "NONE" -p ./singbox_subscribe ./sing-box-subconverter.py
```

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
