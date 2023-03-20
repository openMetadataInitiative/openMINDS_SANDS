import openMINDS.version_manager
import json

# atlas Data
familyNames = ["Auzias", "Brovelli", "Coulon"]
givenNames = ["Guillaume", "Andrea", "Olivier"]
ORCIDs = ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
dataset_identifiers = ["https://doi.org/10.1002/hbm.23121"]


# variables for constructing correct JSON-LD documents
json_person = "https://openminds.ebrains.eu/instances/"

# add connections to other metadata instances
# email_openminds = mycollection.add_core_contactInformation(email="openminds@ebrains.eu")
# mycollection.get(person_open).contactInformation = email_openminds
## import of scraped data with json import

# pretty printing

with open('/home/kiwitz1/PycharmProjects/OpenMinds/myFirstOpenMINDSMetadataCollection/ORCID/257af828-c40e-11ed-a866-00155daeebba', 'r') as fobj:
    data = json.load(fobj)

print(data)

with open('/home/kiwitz1/PycharmProjects/OpenMinds/myFirstOpenMINDSMetadataCollection/ORCID/pretty.json', "w") as test:
    json.dump(data, test)

atlas_json = json.loads("./myFirstOpenMINDSMetadataCollection/")


