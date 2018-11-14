import requests
import json
import pprint
nhsno = '9658218881'

headers = {
  'accept': 'application/fhir+json',
  'Ssp-TraceID': '09a01679-2564-0fb4-5129-aecc81ea2706',
  'Ssp-From': '200000000359',
  'Ssp-To': '200000000359',
  'Ssp-InteractionID': 'urn:nhs:names:services:gpconnect:fhir:operation:gpc.getstructuredrecord-1',
  'Authorization':'Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.ewogICJpc3MiOiAiaHR0cDovL2VjMi01NC0xOTQtMTA5LTE4NC5ldS13ZXN0LTEuY29tcHV0ZS5hbWF6b25hd3MuY29tLyMvc2VhcmNoIiwKICAic3ViIjogIjEiLAogICJhdWQiOiAiaHR0cHM6Ly9hdXRob3JpemUuZmhpci5uaHMubmV0L3Rva2VuIiwKICAiZXhwIjogMTUyMDc4MjIwMCwKICAiaWF0IjogMTUyMDc4MTkwMCwKICAicmVhc29uX2Zvcl9yZXF1ZXN0IjogImRpcmVjdGNhcmUiLAogICJyZXF1ZXN0ZWRfc2NvcGUiOiAicGF0aWVudC8qLnJlYWQiLAogICJyZXF1ZXN0aW5nX2RldmljZSI6IHsKICAgICJyZXNvdXJjZVR5cGUiOiAiRGV2aWNlIiwKICAgICJpZGVudGlmaWVyIjogWwogICAgICB7CiAgICAgICAgInN5c3RlbSI6ICJXZWIgSW50ZXJmYWNlIiwKICAgICAgICAidmFsdWUiOiAiR1AgQ29ubmVjdCBEZW1vbnN0cmF0b3IiCiAgICAgIH0KICAgIF0sCiAgICAibW9kZWwiOiAiRGVtb25zdHJhdG9yIiwKICAgICJ2ZXJzaW9uIjogIjEuMi4yIiwKICAgICJ1cmwiOiAiaHR0cDovL2VjMi01NC0xOTQtMTA5LTE4NC5ldS13ZXN0LTEuY29tcHV0ZS5hbWF6b25hd3MuY29tLyMvc2VhcmNoIgogIH0sCiAgInJlcXVlc3Rpbmdfb3JnYW5pemF0aW9uIjogewogICAgInJlc291cmNlVHlwZSI6ICJPcmdhbml6YXRpb24iLAogICAgImlkZW50aWZpZXIiOiBbCiAgICAgIHsKICAgICAgICAic3lzdGVtIjogImh0dHBzOi8vZmhpci5uaHMudWsvSWQvb2RzLW9yZ2FuaXphdGlvbi1jb2RlIiwKICAgICAgICAidmFsdWUiOiAiQTExMTExIgogICAgICB9CiAgICBdLAogICAgIm5hbWUiOiAiR1AgQ29ubmVjdCBEZW1vbnN0cmF0b3IiCiAgfSwKICAicmVxdWVzdGluZ19wcmFjdGl0aW9uZXIiOiB7CiAgICAicmVzb3VyY2VUeXBlIjogIlByYWN0aXRpb25lciIsCiAgICAiaWQiOiAiMSIsCiAgICAiaWRlbnRpZmllciI6IFsKICAgICAgewogICAgICAgICJzeXN0ZW0iOiAiaHR0cHM6Ly9maGlyLm5ocy51ay9zZHMtdXNlci1pZCIsCiAgICAgICAgInZhbHVlIjogIkcxMzU3OTEzNSIKICAgICAgfSwKICAgICAgewogICAgICAgICJzeXN0ZW0iOiAiaHR0cHM6Ly9maGlyLm5ocy51ay9JZC9zZHMtcm9sZS1wcm9maWxlLWlkIiwKICAgICAgICAidmFsdWUiOiAiMTExMTExMTExIgogICAgICB9LAogICAgICB7CiAgICAgICAgInN5c3RlbSI6ICJMb2NhbFVzZXJTeXN0ZW0iLAogICAgICAgICJ2YWx1ZSI6ICIxIgogICAgICB9CiAgICBdLAogICAgIm5hbWUiOiBbCiAgICAgIHsKICAgICAgICAiZmFtaWx5IjogIkRlbW9uc3RyYXRvciIsCiAgICAgICAgImdpdmVuIjogWwogICAgICAgICAgIkdQQ29ubmVjdCIKICAgICAgICBdLAogICAgICAgICJwcmVmaXgiOiBbCiAgICAgICAgICAiTXIiCiAgICAgICAgXQogICAgICB9CiAgICBdCiAgfQp9.',
  'Content-Type': 'application/fhir+json'
  }
payload = {
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "patientNHSNumber",
      "valueIdentifier": {
        "system": "https://fhir.nhs.uk/Id/nhs-number",
        "value": nhsno
      }
    },
    {
      "name": "includeAllergies",
      "part": [
        {
          "name": "includeResolvedAllergies",
          "valueBoolean": True
        }
      ]
    },
    {
      "name": "includeMedication",
      "part": [
        {
          "name": "includePrescriptionIssues",
          "valueBoolean": True
        },
        {
          "name": "medicationSearchFromDate",
          "valueDate": "2015-01-01"
        }
      ]
    }
  ]
}

url = 'https://orange.testlab.nhs.uk/gpconnect-demonstrator/v1/fhir/Patient/$gpc.getstructuredrecord'


r = requests.post(url, data=str(payload), headers=headers)
Pdata = json.loads(r.text)
medications = []
allergies = []
for data in Pdata['entry']:
  resource_type = data['resource']['resourceType'] 
  if resource_type == 'Medication' :
    medications.append(data['resource']['code']['coding'][0]['display'])
    #pprint.pprint(data['resource'])
  elif resource_type == 'AllergyIntolerance' :
    #pprint.pprint(data['resource'])
    
    allergy = data['resource']['code']['coding'][0]['display']
    reaction = data['resource']['reaction'][0]['manifestation'][0]['coding'][0]['display']
    allergies.append((allergy, reaction))
  elif resource_type == 'Patient' :
    #pprint.pprint(data['resource'])
    patient_details = {}
    patient_details['dob'] = data['resource']['birthDate']
    patient_details['firstname'] = data['resource']['name'][0]['given'][0]
    patient_details['surname'] = data['resource']['name'][0]['family']
    

print ('---')
print ('DEMOGRAPHICS:')
pprint.pprint(patient_details)
print (" ")
print ('MEDICATIONS:')
for med in medications:
  print ('-' + med)
print (" ")
print ('ALLERGIES:')
for allergy in allergies:
  print (allergy)