import os
import openMINDS.version_manager
# region_names cortex and subcortex generated wth data scrape script
# generate json code for integration into Brain atlas instances
with open("/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/helper_code/MarsAtlasRegions_subcortex.txt", 'w') as f:
    f.write("Mars_Areas\n")
    open = "{"
    close = "}"
    instance = "\"@id\": \"https://openminds.ebrains.eu/instances/parcellationEntity/"

    for index, area in enumerate(region_names):
        f.write(f"{open}\n")
        f.write(f"{instance}{region_names[index]}\"\n")
        f.write(f"{close},\n")
f.close()

with open("/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/helper_code/MarsAtlasRegions_cortex.txt", 'w') as d:
    d.write("Mars_Areas\n")
    open = "{"
    close = "}"
    instance = "\"@id\": \"https://openminds.ebrains.eu/instances/parcellationEntity/"

    for index, area in enumerate(region_names_cortex):
        d.write(f"{open}\n")
        d.write(f"{instance}{region_names[index]}\"\n")
        d.write(f"{close},\n")
d.close()

# generate directories and filenames for atlas instances
s1 = "Mars_"
j =".jsonld"
entities = region_names_cortex + region_names_subcortex
directories = {}
path = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars/"

for index,entity in enumerate(entities):
    directories[index] = path + s1 + entity +j

#generate files

for directory in directories.values():
    with open(directory, "w") as p:
        p.write("")
    p.close()

# generate instances

# loop over every file in the directory and create isntances
# intialize openMinds instance creator

openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
atlas = helper.create_collection()

#
# create instances
directory = '/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars'

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        # strip the area name from the filename
        stripped_filename = str.replace(filename, ".jsonld", "")
        area = str.replace(stripped_filename, "Mars_", "")
        # create parcellation entity instance
        parcellation_entity = atlas.add_SANDS_parcellationEntity(name = area)
        atlas.get(parcellation_entity).lookupLabel = stripped_filename
        # add the versions to hasVersion
        # paths an info for the instance file
        path_to entity_version = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
        version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
        atlas_versions = ["Mars_individual_cortex", "Mars_individual_cortexAndSubcortex", "Mars_HipHop138_cortex",
                          "Mars_Colin27_1998_cortexAndSubcortex"]
        # loop over the directories and find the str matching to area

        ## here is code from chat gpt:



        #def find_file(directory, filename):
        #    for root, dirs, files in os.walk(directory):
        #        if filename in files:
        #            return root


        #directory = '/path/to/directory'
        #filename = 'example.txt'

        #result = find_file(directory, filename)

        #if result:
        #    print(f'The file {filename} was found in the directory: {result}')
        #else:
         #   print(f'The file {filename} was not found in the directory: {directory}')
        #

        version_name = []


        atlas.get(parcellation_entity).hasVersion = [{"@id": orcid}]
        #"lookupLabel": "Mars_ACC",
        #"name": "ACC",


for i in enumerate(givenNames):
        # persons
        person = atlas.add_core_person(givenName = givenNames[i[0]])
        atlas.get(person).familyName = str(familyNames[i[0]])
        # ORCIDS
        orcid = atlas.add_core_ORCID()
        atlas.get(orcid).identifier = ORCIDs[i[0]]
        # add ORCIDs to person instances
        atlas.get(person).digitalIdentifier = [{"@id": orcid}]
        # change @ids from local host to actual orcid
#
## extract the ending string
## replace the @id with the ending string in the json file


## parse the json code automatically and adapt the @id t


#loop over every file and extract the strings for the parcellation entity version (should be maximum of 4 didfferent strs)
## relace the hasVersion argument of the json wih the appropiate str