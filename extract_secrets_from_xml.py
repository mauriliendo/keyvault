import xml.etree.ElementTree as ET

def extract_secrets_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    secrets = {}

    for section in root.findall('./*'):
        section_name = section.tag
        for element in section.findall('.//add'):
            key = element.get('key')
            value = element.get('value')
            secret_name = f"{section_name}--{key}"
            secrets[secret_name] = value

    return secrets
