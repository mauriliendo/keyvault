import json

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def upload_to_azure_key_vault(json_secrets, key_vault_url):
    credentials = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=key_vault_url, credential=credentials)

    secrets = json.loads(json_secrets)

    for secret_name, secret_value in secrets.items():
        secret_client.set_secret(secret_name, secret_value)

    print("Secrets uploaded to Azure Key Vault successfully.")
