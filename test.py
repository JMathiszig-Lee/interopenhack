from fhirclient import client
settings = {
  'app_id': 'interopenapp',
  'api_base':'https://fhir.nhs.uk/STU3/StructureDefinition'
}
smart = client.FHIRClient(settings=settings)

import fhirclient.models.patient as p

patient = p.Patient.read('9658218873', smart.server)

print (patient)