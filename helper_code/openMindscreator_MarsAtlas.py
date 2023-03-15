import openMINDS
import openMINDS

import json


# MarsAtlas Data
familyNames = ["Auzias", "Brovelli", "Coulon"]
givenNames = ["Guillaume", "Andrea", "Olivier"]
ORCIDs= ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
dataset_identifiers = ["https://doi.org/10.1002/hbm.23121"]


# Initialise the local copy of openMINDS
openMINDS.version_manager.init()

# Das heir checken um schemas zu adden!!!!!!!!!!!!!!!!!!
openMINDS.Schema_Discovery()

# Select which version of openMINDS to use
openMINDS.version_manager.version_selection('v2.0.0')

# initiate the helper class for the dynamic usage of a specific openMINDS version
helper = openMINDS.Helper()

# initiate the collection into which you will store all metadata instances
mycollection = helper.create_collection()
# schema creation persons and ORCIDS
for i in enumerate(givenNames):
        # persons
        person = mycollection.add_core_person(givenName = givenNames[i[0]])
        mycollection.get(person).familyName = str(familyNames[i[0]])
        # ORCIDS
        orcid = mycollection.add_core_ORCID()
        mycollection.get(orcid).identifier = orcid[i[0]]
        # add ORCIDs to person instances
        mycollection.get(person).digitalIdentifier = orcid

# schema creation DOIs
for i in dataset_identifiers:
        # dois
        doi = mycollection.add_core_DOI()
        mycollection.get(doi).identifier = i

# schema creation Brain atlas

#MarsAtlas = mycollection.add_SANDS_BrainAtlas()
## import of scraped data with json import

# save your collection
mycollection.save("./myFirstOpenMINDSMetadataCollection/")



# Getting help for properties
mycollection.help_sands_atlas_brainAtlas()