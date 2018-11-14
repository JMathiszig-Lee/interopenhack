import requests

Auth_Stuff = {
  "iss": "http://ec2-54-194-109-184.eu-west-1.compute.amazonaws.com/#/search",
  "sub": "1",
  "aud": "https://authorize.fhir.nhs.net/token",
  "exp": 1520782200,
  "iat": 1520781900,
  "reason_for_request": "directcare",
  "requested_scope": "patient/*.read",
  "requesting_device": {
    "resourceType": "Device",
    "identifier": [
      {
        "system": "Web Interface",
        "value": "GP Connect Demonstrator"
      }
    ],
    "model": "Demonstrator",
    "version": "1.2.2",
    "url": "http://ec2-54-194-109-184.eu-west-1.compute.amazonaws.com/#/search"
  },
  "requesting_organization": {
    "resourceType": "Organization",
    "identifier": [
      {
        "system": "https://fhir.nhs.uk/Id/ods-organization-code",
        "value": "A11111"
      }
    ],
    "name": "GP Connect Demonstrator"
  },
  "requesting_practitioner": {
    "resourceType": "Practitioner",
    "id": "1",
    "identifier": [
      {
        "system": "https://fhir.nhs.uk/sds-user-id",
        "value": "G13579135"
      },
      {
        "system": "https://fhir.nhs.uk/Id/sds-role-profile-id",
        "value": "111111111"
      },
      {
        "system": "LocalUserSystem",
        "value": "1"
      }
    ],
    "name": [
      {
        "family": "Demonstrator",
        "given": [
          "GPConnect"
        ],
        "prefix": [
          "Mr"
        ]
      }
    ]
  }
}

headers = {
  'accept': 'application/fhir+json',
  'Ssp-TraceID': '09a01679-2564-0fb4-5129-aecc81ea2706',
  'Ssp-From': '200000000359',
  'Ssp-To': '200000000359',
  'Ssp-InteractionID': 'urn:nhs:names:services:gpconnect:fhir:rest:search:patient-1',
  'Authorization':'Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.ewogICJpc3MiOiAiaHR0cDovL2VjMi01NC0xOTQtMTA5LTE4NC5ldS13ZXN0LTEuY29tcHV0ZS5hbWF6b25hd3MuY29tLyMvc2VhcmNoIiwKICAic3ViIjogIjEiLAogICJhdWQiOiAiaHR0cHM6Ly9hdXRob3JpemUuZmhpci5uaHMubmV0L3Rva2VuIiwKICAiZXhwIjogMTUyMDc4MjIwMCwKICAiaWF0IjogMTUyMDc4MTkwMCwKICAicmVhc29uX2Zvcl9yZXF1ZXN0IjogImRpcmVjdGNhcmUiLAogICJyZXF1ZXN0ZWRfc2NvcGUiOiAicGF0aWVudC8qLnJlYWQiLAogICJyZXF1ZXN0aW5nX2RldmljZSI6IHsKICAgICJyZXNvdXJjZVR5cGUiOiAiRGV2aWNlIiwKICAgICJpZGVudGlmaWVyIjogWwogICAgICB7CiAgICAgICAgInN5c3RlbSI6ICJXZWIgSW50ZXJmYWNlIiwKICAgICAgICAidmFsdWUiOiAiR1AgQ29ubmVjdCBEZW1vbnN0cmF0b3IiCiAgICAgIH0KICAgIF0sCiAgICAibW9kZWwiOiAiRGVtb25zdHJhdG9yIiwKICAgICJ2ZXJzaW9uIjogIjEuMi4yIiwKICAgICJ1cmwiOiAiaHR0cDovL2VjMi01NC0xOTQtMTA5LTE4NC5ldS13ZXN0LTEuY29tcHV0ZS5hbWF6b25hd3MuY29tLyMvc2VhcmNoIgogIH0sCiAgInJlcXVlc3Rpbmdfb3JnYW5pemF0aW9uIjogewogICAgInJlc291cmNlVHlwZSI6ICJPcmdhbml6YXRpb24iLAogICAgImlkZW50aWZpZXIiOiBbCiAgICAgIHsKICAgICAgICAic3lzdGVtIjogImh0dHBzOi8vZmhpci5uaHMudWsvSWQvb2RzLW9yZ2FuaXphdGlvbi1jb2RlIiwKICAgICAgICAidmFsdWUiOiAiQTExMTExIgogICAgICB9CiAgICBdLAogICAgIm5hbWUiOiAiR1AgQ29ubmVjdCBEZW1vbnN0cmF0b3IiCiAgfSwKICAicmVxdWVzdGluZ19wcmFjdGl0aW9uZXIiOiB7CiAgICAicmVzb3VyY2VUeXBlIjogIlByYWN0aXRpb25lciIsCiAgICAiaWQiOiAiMSIsCiAgICAiaWRlbnRpZmllciI6IFsKICAgICAgewogICAgICAgICJzeXN0ZW0iOiAiaHR0cHM6Ly9maGlyLm5ocy51ay9zZHMtdXNlci1pZCIsCiAgICAgICAgInZhbHVlIjogIkcxMzU3OTEzNSIKICAgICAgfSwKICAgICAgewogICAgICAgICJzeXN0ZW0iOiAiaHR0cHM6Ly9maGlyLm5ocy51ay9JZC9zZHMtcm9sZS1wcm9maWxlLWlkIiwKICAgICAgICAidmFsdWUiOiAiMTExMTExMTExIgogICAgICB9LAogICAgICB7CiAgICAgICAgInN5c3RlbSI6ICJMb2NhbFVzZXJTeXN0ZW0iLAogICAgICAgICJ2YWx1ZSI6ICIxIgogICAgICB9CiAgICBdLAogICAgIm5hbWUiOiBbCiAgICAgIHsKICAgICAgICAiZmFtaWx5IjogIkRlbW9uc3RyYXRvciIsCiAgICAgICAgImdpdmVuIjogWwogICAgICAgICAgIkdQQ29ubmVjdCIKICAgICAgICBdLAogICAgICAgICJwcmVmaXgiOiBbCiAgICAgICAgICAiTXIiCiAgICAgICAgXQogICAgICB9CiAgICBdCiAgfQp9.'
  }
payload = {'identifier': 'https://fhir.nhs.uk/Id/nhs-number|9658218873'}
nhsno = '9658218873'
url = 'https://orange.testlab.nhs.uk/gpconnect-demonstrator/v1/fhir/Patient'


r = requests.get(url, params=payload, headers=headers)
print (r.content)
print (" ")
print (" ")
print (r.json)