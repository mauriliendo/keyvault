from convert_to_json import convert_to_json
from extract_secrets_from_xml import extract_secrets_from_xml
from upload_to_azure_key_vault import upload_to_azure_key_vault

if __name__ == "__main__":
    xml_file_path = "C:\\Users\\mauricio.liendo\\Desktop\\Python\\ShipCompliantConfig.AzureProd.xml"
    json_secrets = convert_to_json(extract_secrets_from_xml(xml_file_path))

    key_vault_url = "https://kv-ship-config-dr.vault.azure.net/"
    upload_to_azure_key_vault(json_secrets, key_vault_url)
