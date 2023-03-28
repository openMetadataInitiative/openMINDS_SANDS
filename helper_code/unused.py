# nice for generator and any() practice

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


#_____________________________________________________________________________#

# create automatically generated schemas using the python library

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


#__________________________---------------------------------------------#

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
