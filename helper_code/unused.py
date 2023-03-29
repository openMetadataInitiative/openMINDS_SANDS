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



#
# # data and helper variables
# path_to_entity_version = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/" \
#                          "parcellationEntityVersion/"
# version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
# entity_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
# atlas_versions = [
#     "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_individual_cortex",
#     "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_individual_cortexAndSubcortex",
#     "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_HipHop138_cortex",
#     "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_Colin27_1998_cortexAndSubcortex"]
# directory = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars/"
#
# # helper variables
# s1 = "Mars_"
# j = ".jsonld"
#
# # data from the data scraper
# entities = region_names_cortex + region_names_subcortex
#
# # ________________________________________________________________________________________________________#
# # generate directories and filenames for parcellation entity instances by hand
# # (usefull to specify the correct jsonld names which is not supported by the python library yet
#
# directories = {}
# for index, entity in enumerate(entities):
#     directories[index] = directory + s1 + entity + j
#
# # generate files
# for i in directories.values():
#     with open(i, "w") as p:
#         p.write("")
#     p.close()
#
# #____________________________________________________________________________________________________________#
# # generate parcellation entity instances with the python library
# # (useful to create the content of the jsonld)
#
# # intialize openMinds instance creator
# openMINDS.version_manager.init()
# openMINDS.version_manager.version_selection('v3')
# helper = openMINDS.Helper()
# atlas = helper.create_collection()
#
#
# def find_files(directory, partial_name):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if any (part == partial_name for part in str.replace(file, ".jsonld", "").split("_")):
#                 results.append(os.path.join(root, file))
#     return results
#
# # loop over parcellation entitites and add version infos
# for filename in os.listdir(directory):
#     if os.path.isfile(os.path.join(directory, filename)):
#         # strip the area name from the filename
#         stripped_filename = str.replace(filename, ".jsonld", "")
#         area = str.replace(stripped_filename, "Mars_", "")
#
#         # create parcellation entity instance
#         parcellation_entity = atlas.add_SANDS_parcellationEntity(name=area)
#         atlas.get(parcellation_entity).lookupLabel = stripped_filename
#         atlas.get(parcellation_entity).name = area
#
#         # loop over the directories and files of the parcellatio entity versions and  find the str matching to area
#         file_paths = find_files(path_to_entity_version, area)
#
#         # check whether the list entries are part of the version list and add the version to the
#         # parcellation entity instance
#         has_version_listOfdic = []
#         for index, version in enumerate(file_paths):
#             # strip the last part of the strings
#             print(os.path.dirname(file_paths[index]))
#             if (os.path.dirname(file_paths[index])) in atlas_versions:
#                 print("CHECK")
#                 stripped_version_area = os.path.basename(file_paths[index])
#                 stripped_version_area = str.replace(stripped_version_area, ".jsonld", "")
#                 has_version_dic = {"@id": f"{version_https}{stripped_version_area}"}
#                 has_version_listOfdic.append(has_version_dic)
#         atlas.get(parcellation_entity).hasVersion = has_version_listOfdic
#
# atlas.save("./instances/")

#_______________________________________________________________________________________________________________#
# now loop over the jsonls generated in the second  step and add the info to the files generated in the first step
#
# # loop over the directory of step 1 and extract region names
# areas = []
# for filename in os.listdir(directory):
#     if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
#         stripped_filename = str.replace(filename, ".jsonld", "")
#         area = str.replace(stripped_filename, "Mars_", "")
#         areas.append(area)
#
# # Set the directory of step 2
# auto_path = "/home/kiwitz1/PycharmProjects/OpenMinds/instances/parcellationEntity/"
#
# # loop over the areas [] from above and for each area check wehtehr it has a match in the jsonld files generated in step 2 (SHOULD BE THE case
# matched_jsonlds = []
# for area in areas:
#     for filename in os.listdir(auto_path):
#         if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
#             file_path = os.path.join(auto_path, filename)
#             with open(file_path, 'r') as f:
#                 data = json.load(f)
#                 content = json.dumps(data)
#                 if area == data["name"]:
#                     matched_jsonlds.append(content)
#
# # assert that both list have the same length
# assert len(matched_jsonlds) == len(areas)
#
# # Print the matched contents
# print(matched_jsonlds)
#
# # loop over the files from step 1 and insert the contents from the matched jsolds list
# for index, filename in enumerate(os.listdir(directory)):
#     if filename.endswith('.jsonld'): # Check if the file is a JSON-LD file
#         file_path = os.path.join(directory, filename)
#         with open(file_path, 'w') as f:
#             f.write(matched_jsonlds[index])
#         f.close()
#
# #______________________________________________________________________________________________________________#
# # as a final step, change the @id for each file to the appropiate identifier
#
# for filename in os.listdir(directory):
#     if filename.endswith('.jsonld'):  # Check if the file is a JSON-LD file
#         file_path = os.path.join(directory, filename)
#         with open(file_path, 'r') as f:
#             data = json.load(f)
#             f.close()
#         with open(file_path, 'w') as p:
#             data["@id"] = entity_https + data["lookupLabel"]
#             content = json.dumps(data)
#             p.write(content)
#             p.close()
#
#