# CK3 Translator
This is a simple python 3.9 module to translate all localisation files for Crusder Kings 3 mods

## Setup
Use python 3.9 and setup a virtual environment with the packages in the `requirements.txt` file

Example: 
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
1. Place the localization files into the english localization folder
2. Run app.py using `python app.py`

It will then go through each localization file, and translate it one by one into the following languages:

- french
- spanish
- german
- russian
- korean
- simp_chinese

It takes a while, as the GoogleAPI is limited to one request every 2 seconds.
