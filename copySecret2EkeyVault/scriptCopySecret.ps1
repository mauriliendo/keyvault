Param(
    [Parameter(Mandatory)]
    [string]$sourceKvName,
    [Parameter(Mandatory)]
    [string]$destKvName
)
Connect-AzAccount
$secretNames = (Get-AzKeyVaultSecret -VaultName $sourceKvName).Name
$secretNames.foreach{
    Set-AzKeyVaultSecret -VaultName $destKvName -Name $_ `
        -SecretValue (Get-AzKeyVaultSecret -VaultName $sourceKvName -Name $_).SecretValue
}