import yaml


def clean_ck3_yaml(text: str) -> str:
    """Clean CK3 yaml file as it's strange

    Mainly replace the 0's, eg:
        "key:0 value" with "key:value"
    """
    for i in range(0, 10):
        text = text.replace(f":{i}", ":")
    return text


def read_file_into_string(filename) -> str:
    """Read any file into a string"""
    with open(filename, encoding="utf_8_sig") as f:
        text = f.read()
    return text


def load_yaml(filename: str) -> dict:
    """Load YAML file as a python dict"""
    text = read_file_into_string(filename)
    clean_text = clean_ck3_yaml(text)
    return yaml.safe_load(clean_text)


def load_yaml_from_byte(bytes):
    clean_text = clean_ck3_yaml(bytes)
    return yaml.safe_load(clean_text)