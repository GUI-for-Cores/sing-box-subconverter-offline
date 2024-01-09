# subconverter-offline
A command-line tool encapsulates the functionality of [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe) project


### Build
- pip install -r ./requirements.txt -r ./singbox_subscribe/requirements.txt
- pyinstaller --noconfirm --onefile --console -i "NONE" -p ./singbox_subscribe ./subconverter.py