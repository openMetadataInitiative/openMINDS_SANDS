# ______________________________________#
import os.path
import re
import openMINDS.version_manager
import json

# variables for constructing correct JSON-LD documents
json_person = "https://openminds.ebrains.eu/instances/"

# person and Identifier schemas
familyNames_mars = ["Auzias", "Brovelli", "Coulon"]
givenNames_mars = ["Guillaume", "Andrea", "Olivier"]
familyNames_subcortex = ["Brovelli", "Badier", "Bonini", "Bartolomei", "Coulon", "Auzias"]
givenNames_subcortex = ["Andrea", "Jean-Michael", "Francesca", "Fabrice", "Olivier", "Guillaume"]
ORCIDs_mars = ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
ORCIDs_subcortex = ["https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0002-7272-6455", "", "", "https://orcid.org/0000-0003-4752-1228", "https://orcid.org/0000-0002-0414-5691"]

# documentation schemas
full_documentation =  [("Mars", "https://doi.org/10.1002/hbm.23121"),("Mars_cortexAndSubcortex", "https://doi.org/10.1523/JNEUROSCI.1672-16.2016")]

# directories
directory_person = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/person/"
directory_digitalIdentifier_DOI = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
directory_digitalIdentifier_ORCID = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"

#__________________________________________________________#
# create directories for ORCIDs DOIs and persons

directories_ORCID_mars = {}
directories_ORCID_subcortex = {}
directories_person_mars = {}
directories_person_subcortex = {}
directories_DOI = {}
j = ".jsonld"

for index, ORCID in enumerate(ORCIDs_mars):
    directories_ORCID_mars[index] = directory_digitalIdentifier_ORCID + "ORCID_" + str.lower(familyNames_mars[index]) + givenNames_mars[index].capitalize() + "_" + os.path.basename(ORCID) + j
for index, ORCID in enumerate(ORCIDs_subcortex):
    directories_ORCID_subcortex[index] = directory_digitalIdentifier_ORCID + "ORCID_" + str.lower(familyNames_subcortex[index]) + \
                                                                                  givenNames_subcortex[index].capitalize() + "_" + os.path.basename(ORCID) + j
for index, person in enumerate(familyNames_mars):
    directories_person_mars[index] = directory_person + str.lower(familyNames_mars[index].replace("-","")) + givenNames_mars[index].replace("-","").capitalize() + j

for index, person in enumerate(familyNames_subcortex):
    directories_person_subcortex[index] = directory_person + str.lower(familyNames_subcortex[index].replace("-","")) + givenNames_subcortex[index].replace("-","").capitalize() + j

for index, DOI in enumerate(full_documentation):
    directories_DOI[index] = directory_digitalIdentifier_DOI + "DOI_" + full_documentation[index][0] + "_" + str.replace(DOI[1], "/", "$") + j

# generate files
for i in directories_ORCID_mars.values():
    with open(i, "w") as p:
        p.write("")
    p.close()

for i in directories_ORCID_subcortex.values():
    with open(i, "w") as t:
        t.write("")
    t.close()

for i in directories_person_mars.values():
    with open(i, "w") as p:
        p.write("")
    p.close()

for i in directories_person_subcortex.values():
    with open(i, "w") as t:
        t.write("")
    t.close()

for i in directories_DOI.values():
    with open(i, "w") as t:
        t.write("")
    t.close()


# ___________________________________________________#
# create automatically generated schemas usong the python library

# intialize openMinds instance creator
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
basic = helper.create_collection()

# loop over ORCIDS and create instances
orcid_https = "https://orcid.org/"
for filename in os.listdir(directory_digitalIdentifier_ORCID):
    if os.path.isfile(os.path.join(directory_digitalIdentifier_ORCID, filename)):
        # strip the ORCID name from the filename
        stripped_orcid = os.path.basename(filename).split("_")[-1].replace(".jsonld", "")
        # area = str.replace(stripped_filename, "Mars_", "")
        # create ORCID  instances
        if any(stripped_orcid in s for s in ORCIDs_mars):
            orcid = basic.add_core_ORCID(identifier=orcid_https+stripped_orcid)
        elif any(stripped_orcid in s for s in ORCIDs_subcortex):
            orcid = basic.add_core_ORCID(identifier=orcid_https + stripped_orcid)

basic.save("./instances/")

# loop over DOIs and create instances
for filename in os.listdir(directory_digitalIdentifier_DOI):
    if os.path.isfile(os.path.join(directory_digitalIdentifier_DOI, filename)):
        # strip the DOI name from the filename
        stripped_doi = os.path.basename(filename).split("_")[-1].replace(".jsonld", "").replace("$", "/")
        # create DOI  instances
        if any(stripped_doi in s[1] for s in full_documentation):
            doi = basic.add_core_DOI(identifier=stripped_doi)

basic.save("./instances/")

# loop over persons and create instances, this is a bit tricky and needs to be done with regular expressions
for filename in os.listdir(directory_person):
    if os.path.isfile(os.path.join(directory_person, filename)):
        # strip the area name from the filename
        stripped_name = filename.replace(".jsonld", "")
        # create a 2-element list split by capitalized letters [0] = family name, [-1] = givenName
        stripped_name = re.findall(r'[a-z]+|[A-Z][a-z]*', stripped_name)
        print(stripped_name)
        # check whether the stripped name exists in the respective lists (a lot of str handling involved here)
        if (any(stripped_name[0].lower() == s.lower().replace("-","") for s in familyNames_mars) and any(stripped_name[1].lower() == s.lower().replace("-","") for s in givenNames_mars))\
                or (any(stripped_name[0].lower() == t.lower().replace("-","") for t in familyNames_subcortex) and any(stripped_name[1].lower() == t.lower().replace("-","") for t in givenNames_subcortex)):
            # create person instance
            person = basic.add_core_person(givenName=stripped_name[1].capitalize())
            # add family name
            basic.get(person).familyName = stripped_name[0].capitalize()
            # add the ORCID
            basic.get(person).digitalIdentifier = stripped_name[0].capitalize()
basic.save("./instances/")


#_________________________________________________________#
# automatic creation

# Initialise the local copy of openMINDS, set version, iitialize helper and collection
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
basic = helper.create_collection()


# schema creation persons and ORCIDS
for i in enumerate(givenNames):
        # persons
        person = atlas.add_core_person(givenName = givenNames[i[0]])
        atlas.get(person).familyName = str(familyNames[i[0]])
        # ORCIDS
        orcid = atlas.add_core_ORCID()
        atlas.get(orcid).identifier = ORCIDs[i[0]]
        # add ORCIDs to person instances
        atlas.get(person).basicIdentifier = [{"@id": orcid}]
        # change @ids from local host to actual orcid



# schema creation DOIs
for i in dataset_identifiers:
        # dois
        doi = atlas.add_core_DOI()
        atlas.get(doi).identifier = i

atlas.save("./myFirstOpenMINDSMetadataCollection/")