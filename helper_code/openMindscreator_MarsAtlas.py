import openMINDS.version_manager
import json

# atlas Data
familyNames = ["Auzias", "Brovelli", "Coulon"]
givenNames = ["Guillaume", "Andrea", "Olivier"]
ORCIDs= ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
dataset_identifiers = ["https://doi.org/10.1002/hbm.23121"]

# Initialise the local copy of openMINDS, set version, iitialize helper and collection
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v2.0.0')
helper = openMINDS.Helper()
atlas = helper.create_collection()


# schema creation persons and ORCIDS
for i in enumerate(givenNames):
        # persons
        person = atlas.add_core_person(givenName = givenNames[i[0]])
        atlas.get(person).familyName = str(familyNames[i[0]])
        # ORCIDS
        orcid = atlas.add_core_ORCID()
        atlas.get(orcid).identifier = orcid[i[0]]
        # add ORCIDs to person instances
        atlas.get(person).digitalIdentifier = orcid

# schema creation DOIs

for i in dataset_identifiers:
        # dois
        doi = atlas.add_core_DOI()
        atlas.get(doi).identifier = i

# schema creation brain atlas version
marsAtlas = atlas.add_SANDS_brainAtlasVersion(fullName="MarsAtlas", coordinateSpace=, versionInnovation=, releaseDate=, \
                                              hasTerminology= , shortName= , versionIdentifier=   )
marsAtlasPlusSubcortical = atlas.add_SANDS_brainAtlasVersion(fullName="MarsAtlas + subcortical",coordinateSpace=,versionInnovation=, \
                                       releaseDate=, hasTerminology= , shortName= , versionIdentifier=  )
# schema creation Brain atlas
marsAtlas = atlas.add_SANDS_brainAtlas(fullName = "MarsAtlas", hasVersion =,  )

# add connections to other metadata instances
#email_openminds = mycollection.add_core_contactInformation(email="openminds@ebrains.eu")
#mycollection.get(person_open).contactInformation = email_openminds
## import of scraped data with json import

# save your collection
atlas.save("./myFirstOpenMINDSMetadataCollection/")

with open('/home/kiwitz1/PycharmProjects/OpenMinds/myFirstOpenMINDSMetadataCollection/ORCID/257af828-c40e-11ed-a866-00155daeebba', 'r') as fobj:
    data = json.load(fobj)

print(data)

with open('/home/kiwitz1/PycharmProjects/OpenMinds/myFirstOpenMINDSMetadataCollection/ORCID/pretty.json', "w") as test:
    json.dump(data, test)

atlas_json = json.loads("./myFirstOpenMINDSMetadataCollection/")


# Getting help for properties
atlas.help_sands_atlas_brainAtlas()