import requests

response = requests.get('http://google.com', {'password': password})
"AWS_ACCESS_KEY_ID": "AKIAUHD5AAQAAAAQAY1Z"
amazonpassword = "amzn.mws.17abcde4-f3a4-c45b-c2dd-2a5e6c7d22ca"
AzureToken: 'Y29weXJpZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Y29eeXJpZ2h0Y29weXJtZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Yw==' #AzureSecret
cosmosDbToken: Y29weXJpZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Y29eeXJpZ2h0Y29weXJtZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Yw==
AzureCosmosPassword: Y29weXJpZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Y29eeXJpZ2h0Y29weXJtZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Yw==
AzureAccountEndpoint=https://<database name>.documents.azure.com:443/;AccountKey=Y29weXJpZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Y29eeXJpZ2h0Y29weXJtZ2h0Y29weXJpZ2h0Y29weXJpZ2h0Yw==

response = requests.get('https://todiaccount56.documents.azure.com:443', {'AccountKey': AzureToken})

#hashicorp:
- text: |
    spring.cloud.vault.token=hvs.JGbZZaCkOSgsZ56uhGlTK2zyC1j2mwhy0VLp4
  apikey: hvs.JGbZZaCkOSgsZ56uhGlTK2zyC1j2mwhy0VLp4

- text: |
     HASHICORP_VAULT_CLIENT_TOKEN="s.Z4bTMtngfLeQ18AqVoBBkUAOD1"
  apikey: s.Z4bTMtngfLeQ18AqVoBBkUAOD1

- text: |
    HASHICORP_VAULT_UNSEAL_KEY_3="C3fk5Q0ANMFlbjQk4E0MKD8xRdNW0YbLA/0pfMSWEouI"
  apikey: C3fk5Q0ANMFlbjQk4E0MKD8xRdNW0YbLA/0pfMSWEouI

- text: |
    UNSEAL_KEY_HASHICORP: BoK4FvGkefnzweuiciDcfrxYco43/45HgtrhtMSWZzOG
  apikey: BoK4FvGkefnzweuiciDcfrxYco43/45HgtrhtMSWZzOG

- text: |
    UNSEAL_KEY_HASHICORP: BoK4FvGkefnzweuiciDcfrxYco43/45HgtrhtMSWZzOG
  apikey: BoK4FvGkefnzweuiciDcfrxYco43/45HgtrhtMSWZzOG

token = "hvs.CAESIAVOUNSKFoTnRYghjutnkl7bYyI0YFINKf1BEInyd63PG1gKImk3cy9IDmJTtLJLOEZ2QYp6bUY5c0MCcLJvS1ouenF9YJkQqNks"

hashicorp_token = "hvs.CAESIJRM-T1q5lEjIWux1Tjx-sVGqAYAww3FZtbp1wpD3Ym3pGh3KHGh9cy5TSjRndGoxaU32NzNscm4MSlRLQXZ0ZGg"

jd_cloud_key = 'snowflake.jdbc.password=B95267B8-8585-1936-94B0-960afa0409da'
jfrog_key = 'AKCp8oiHHT23xDyNaasrn3wwu1oXsHE4vcfcfudiGZU723EpM6KpNM3zEkan6ntKadypWcRuW'

  
#newrelic:
new_relic_secret = 'AAab3ecd78ef81ea312afbcd135efa245545bcd4ee'
- text: |
    "admin_access:NRAA-4780f48c46df5882dbec0fd81c7"
  apikey: NRAA-4780f48c46df5882dbec0fd81c7

- text: |
    "newrelic admin_access:NRAA-4780f48c46df5882dbec0fd81c7"
  apikey: NRAA-4780f48c46df5882dbec0fd81c7

#newrelic1:
- text: 'newrelic.license="8722b5ba69b65e1ebbd98ffed2754c7e10320730'
  apikey: 8722b5ba69b65e1ebbd98ffed2754c7e10320730
- text: 'newrelic license_key: b983cd792c02f2e2cd3c896c826f6b156b44137f'
  apikey: b983cd792c02f2e2cd3c896c826f6b156b44137f
- text: 'newrelic license_key:b983cd792c02f2e2cd3c896c826f6b156b44137f'
  apikey: b983cd792c02f2e2cd3c896c826f6b156b44137f
- text: "new relic license_key: 'b983cd792c02f2e2cd3c896c826f6b156b44137f'"
  apikey: b983cd792c02f2e2cd3c896c826f6b156b44137f
- text: "new_relic license_key='b983cd792c02f2e2cd3c896c826f6b156b44137f'"
  apikey: b983cd792c02f2e2cd3c896c826f6b156b44137f
- text: "new-relic license_key b983cd792c02f2e2cd3c896c826f6b156b44137f'"
  apikey: b983cd792c02f2e2cd3c896c826f6b156b44137f
- text: '& "c:\newrelic\install.cmd" -LicenseKey 5b770a55f62576aeebc63fb31ee3fb73d134ab44 -InstrumentAll'
  apikey: 5b770a55f62576aeebc63fb31ee3fb73d134ab44
- text: 'ENV NEWRELIC_KEY af692bf0c7e064b9f1cd4a207ff5e7431203b6cb'
  apikey: af692bf0c7e064b9f1cd4a207ff5e7431203b6cb
- text: |
    api.newrelic.com/deployments.xml',
             'key' => [
                    'x-api-key' => '67da5cddd6995dfe8bb628434a43b2fa5aabdedf
  apikey: 67da5cddd6995dfe8bb628434a43b2fa5aabdedf
- text: newrelic.license="8722b5ba69b65e1ebbd98ffed2754c7e10320730
  apikey: 8722b5ba69b65e1ebbd98ffed2754c7e10320730

- text: |
    "APIKEY: NRRA-6baa13a5c9e652b3bdfeb7c7cde9056c381a190de9"
  apikey: NRRA-6baa13a5c9e652b3bdfeb7c7cde9056c381a190de9

- text: |
    "new relic APIKEY: NRRA-6baa13a5c9e652b3bdfeb7c7cde9056c381a190de9"
  apikey: NRRA-6baa13a5c9e652b3bdfeb7c7cde9056c381a190de9

#newrelicapm:
- text: 'NewRelicApmKey=06322a89ef4a5517e44dc86162e44eade11aNRAL'
  apikey: 06322a89ef4a5517e44dc86162e44eade11aNRAL

- text: '# USA APM key: ud13xxda1139e3ea61ce3d966485c74c5138NRAL'
  apikey: ud13xxda1139e3ea61ce3d966485c74c5138NRAL

- text: |
    my new_relic API KEY
    # USA APM key: ud13xxaa1139e3ea61ce3d966485c74c5138NRAL
  apikey: ud13xxaa1139e3ea61ce3d966485c74c5138NRAL
