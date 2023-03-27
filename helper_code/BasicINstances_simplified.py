# ______________________________________#
import os.path
import re
import openMINDS.version_manager
import json

# variables for constructing correct JSON-LD documents
json_person = "https://openminds.ebrains.eu/instances/"
ORCID_https = "https://orcid.org/"
# basic infos
mars_cortex_authors = [{"auziasGuillaume" : {"familyName" : "Auzias", "givenName" : "Guillaume", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}},
                       {"brovelliAndrea" : {"familyName" : "Brovelli", "givenName" : "Andrea", "ORCID" : "https://orcid.org/0000-0002-5342-1330"}},
                        {"coulonOlivier" : {"familyName" : "Coulon", "givenName" : "Olivier", "ORCID" : "https://orcid.org/0000-0003-4752-1228"}}]

mars_cortexAndSubcotex_authors = [{"brovelliAndrea" : {"familyName" : "Brovelli", "givenName" : "Andrea", "ORCID" : "https://orcid.org/0000-0002-5342-1330"}},
                                  {"badierJeanmichael" : {"familyName" : "Badier", "givenName" : "Jean-Michael", "ORCID" : "https://orcid.org/0000-0002-7272-6455"}},
                                  {"boniniFrancesca" : {"familyName" : "Bonini", "givenName" : "Francesca", "ORCID" : None}},
                                  {"bartolomeiFabrice" : {"familyName" : "Bartolomei", "givenName" : "Fabrice", "ORCID" : None}},
                                  {"coulonOlivier" : {"familyName" : "Coulon", "givenName" : "Olivier", "ORCID" : "https://orcid.org/0000-0003-4752-1228"}},
                                  {"auziasGuillaume" : {"familyName" : "Auzias", "givenName" : "Guillaume", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}}]
full_documentation =  [{"Mars": "https://doi.org/10.1002/hbm.23121"},{"Mars_cortexAndSubcortex": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016"}]

# person and Identifier schemas
familyNames_mars = ["Auzias", "Brovelli", "Coulon"]
givenNames_mars = ["Guillaume", "Andrea", "Olivier"]
familyNames_subcortex = ["Brovelli", "Badier", "Bonini", "Bartolomei", "Coulon", "Auzias"]
givenNames_subcortex = ["Andrea", "Jean-Michael", "Francesca", "Fabrice", "Olivier", "Guillaume"]
ORCIDs_mars = ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
ORCIDs_subcortex = ["https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0002-7272-6455", "", "", "https://orcid.org/0000-0003-4752-1228", "https://orcid.org/0000-0002-0414-5691"]

# intialize openMinds instance creator
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
basic = helper.create_collection()
#__________________________________________________________#
# create directories for ORCIDs DOIs and persons

j = ".jsonld"


def generate_ORCIDS(path, *args):
    """create ORCID directories, files and instances ind a semi-automatic manner"""
    # create directory and file shells
    for list in args:
        for item in list:
            for name in item.keys():
                orcid = item.get(name).get("ORCID")
                if orcid is None:
                    continue
                else:
                    orcid_path = f"{path}ORCID_{name}_{os.path.basename(orcid)}{j}"
                    if not os.path.isfile(orcid_path):
                        with open(orcid_path, "w") as p:
                        p.write("")
                        p.close()
                        # create instance automatically
                        basic.add_core_ORCID(identifier=orcid)
    # save automatic orcid instances
    basic.save("./instances/")
    # copy data from instance to file


directory_digitalIdentifier_ORCID = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"
generate_ORCIDS(directory_digitalIdentifier_ORCID, mars_cortex_authors, mars_cortexAndSubcotex_authors)


def generate_DOIS(path, list):
    doi_str = "https://doi.org/"
    for item in list:
        for version in item.keys():
            doi = item[version]
            doi_stripped = doi.replace(doi_str, "").replace("/", ".")
            if doi is None:
                continue
            else:
                doi_path = f"{path}DOI_{version}_{doi_stripped}{j}"
                if not os.path.isfile(doi_path):
                    with open(doi_path, "w") as p:
                    p.write("")
                    p.close()
                    # create instance automatically
                    basic.add_core_DOI(identifier=doi)
    # save automatic orcid instances
    basic.save("./instances/")
    # copy data from instance to file


directory_digitalIdentifier_DOI = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
generate_DOIS(directory_digitalIdentifier_DOI, full_documentation)


def generate_persons(path, *args):
    for list in args:
        for item in list:
            for name in item.keys():
                if name is None:
                    continue
                else:
                    person_path = f"{path}{name}{j}"
                    if not os.path.isfile(person):
                        with open(person_path, "w") as p:
                        p.write("")
                        p.close()

directory_person = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/person/"
generate_persons(directory_person, mars_cortex_authors, mars_cortexAndSubcotex_authors)

# ___________________________________________________#

# create automatically generated schemas usong the python library




# loop over DOIs and create instances
for filename in os.listdir(directory_digitalIdentifier_DOI):
    if os.path.isfile(os.path.join(directory_digitalIdentifier_DOI, filename)):
        # strip the DOI name from the filename
        stripped_doi = os.path.basename(filename).split("_")[-1].replace(".jsonld", "").replace("$", "/")
        # create DOI  instances
        if any(stripped_doi in s[1] for s in full_documentation):
            doi = basic.add_core_DOI(identifier=stripped_doi)

basic.save("./instances/")

def find_path(directory, partial_name):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any (part == partial_name for part in str.replace(file, ".jsonld", "").split("_")):
                result.append(os.path.join(root, file))
    return result


# loop over persons and create instances, this is a bit tricky and needs to be done with regular expressions
for filename in os.listdir(directory_person):
    if os.path.isfile(os.path.join(directory_person, filename)):
        # strip the area name from the filename
        stripped_name = filename.replace(".jsonld", "")
        # create a 2-element list split by capitalized letters [0] = family name, [-1] = givenName
        stripped_name_re = re.findall(r'[a-z]+|[A-Z][a-z]*', stripped_name)
        print(stripped_name_re)
        # check whether the stripped name exists in the respective lists (a lot of str handling involved here)
        if (any(stripped_name_re[0].lower() == s.lower().replace("-","") for s in familyNames_mars) and any(stripped_name_re[1].lower() == s.lower().replace("-","") for s in givenNames_mars))\
                or (any(stripped_name_re[0].lower() == t.lower().replace("-","") for t in familyNames_subcortex) and any(stripped_name_re[1].lower() == t.lower().replace("-","") for t in givenNames_subcortex)):
            # create person instance
            person = basic.add_core_person(givenName=stripped_name_re[1].capitalize())
            # add family name
            basic.get(person).familyName = stripped_name_re[0].capitalize()

        # add the ORCID, loop over the ORCID directory and extract the orcid from the filname
        orcid_path = find_path(directory_digitalIdentifier_ORCID, stripped_name)
        print(orcid_path)
        orcid_complete = ORCID_https + os.path.basename(orcid_path[0]).replace(".jsonld", "")
        basic.get(person).digitalIdentifier = {"@id": f"{orcid_complete}"}

basic.save("./instances/")


#_________________________________________________________#


# final step: copying the contents back to the manually created files

# Set the directory of step 2
doi_path = "/home/kiwitz1/PycharmProjects/OpenMinds/instances/DOI/"
orcid_path = "/home/kiwitz1/PycharmProjects/OpenMinds/instances/ORCID/"
person_path = "/home/kiwitz1/PycharmProjects/OpenMinds/instances/person/"

# loop over DOIS from step 1
dois = []
for filename in os.listdir(directory_digitalIdentifier_DOI):
    if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
        stripped_doi = os.path.basename(filename).split("_")[-1].replace(".jsonld", "").replace("$", "/")
        dois.append(stripped_doi)

# loop over orcids from step 1
orcids = []
orcid_https = "https://orcid.org/"
for filename in os.listdir(directory_digitalIdentifier_ORCID):
    if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
        stripped_orcid = os.path.basename(filename).split("_")[-1].replace(".jsonld", "")
        orcids.append(orcid_https + stripped_orcid)

# loop over persons from step 1
persons = []
for filename in os.listdir(directory_person):
    if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
        stripped_person = filename.replace(".jsonld", "")
        persons.append(stripped_person)



# loop over the dois and check whether they match   the jsonld files generated in step 2 (SHOULD BE THE case)
matched_dois = []
for doi in dois:
    for filename in os.listdir(doi_path):
        if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
            file_path = os.path.join(doi_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                content = json.dumps(data)
                if doi == data["identifier"]:
                    matched_dois.append(content)

# loop over the orcids and check whether they match  the jsonld files generated in step 2 (SHOULD BE THE case)
matched_orcids = []
for identifier in orcids:
    if identifier == orcid_https:
        continue
    for filename in os.listdir(orcid_path):
        if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
            file_path = os.path.join(orcid_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                content = json.dumps(data)
                if identifier == data["identifier"]:
                    matched_orcids.append(content)


# loop over the persons and check whether they match  the jsonld files generated in step 2 (SHOULD BE THE case)
matched_persons = []
for person in persons:
    for filename in os.listdir(person_path):
        if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
            file_path = os.path.join(person_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                content = json.dumps(data)
                if person.lower() == str.lower(data["familyName"] + data["givenName"]):
                    matched_persons.append(content)


for index, filename in enumerate(os.listdir(directory_digitalIdentifier_DOI)):
    if filename.endswith('.jsonld'): # Check if the file is a JSON-LD file
        file_path = os.path.join(directory_digitalIdentifier_DOI, filename)
        with open(file_path, 'w') as f:
            f.write(matched_dois[index])
        f.close()


for index, filename in enumerate(os.listdir(directory_person)):
    if filename.endswith('.jsonld'): # Check if the file is a JSON-LD file
        file_path = os.path.join(directory_person, filename)
        with open(file_path, 'w') as f:
            f.write(matched_persons[index])
        f.close()
## needs to be redone
# loop over the files from step 1 and insert the contents from the matched jsolds list
for index, filename in enumerate(os.listdir(directory_digitalIdentifier_ORCID)):
    if any(not char.isdigit() for char in os.path.basename(filename)):
        continue
    if filename.endswith('.jsonld'): # Check if the file is a JSON-LD file
        file_path = os.path.join(directory_digitalIdentifier_ORCID, filename)
        with open(file_path, 'w') as f:
            f.write(matched_orcids[index])
        f.close()
