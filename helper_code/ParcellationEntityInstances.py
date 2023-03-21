import os
import openMINDS.version_manager

# generate directories and filenames for parcellation entity instances
s1 = "Mars_"
j = ".jsonld"
# from the data scraper
entities = region_names_cortex + region_names_subcortex
directories = {}
path = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars/"

for index, entity in enumerate(entities):
    directories[index] = path + s1 + entity + j

# generate files
for directory in directories.values():
    with open(directory, "w") as p:
        p.write("")
    p.close()

# generate parcellation entity instances
# loop over every file in the parcellation entity folder of the Mars atlas and create isntances
# intialize openMinds instance creator
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
atlas = helper.create_collection()
directory = '/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars'


def find_files(directory, partial_name):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if partial_name in file:
                results.append(os.path.join(root, file))
    return results


for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        # strip the area name from the filename
        stripped_filename = str.replace(filename, ".jsonld", "")
        area = str.replace(stripped_filename, "Mars_", "")

        # create parcellation entity instance
        global parcellation_entity
        parcellation_entity = atlas.add_SANDS_parcellationEntity(name=area)
        atlas.get(parcellation_entity).lookupLabel = stripped_filename
        atlas.get(parcellation_entity).name = area

        # add the versions to hasVersion
        path_to_entity_version = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/" \
                                 "parcellationEntityVersion/"
        version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
        atlas_versions = ["/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_individual_cortex", "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_individual_cortexAndSubcortex", "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_HipHop138_cortex","/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/Mars_Colin27_1998_cortexAndSubcortex"]

        # loop over the directories and files of the parcellatio entity versions and  find the str matching to area
        file_paths = find_files(path_to_entity_version, area)
        for path in file_paths:
            print(path)

        # check whether the list entries are part of the version list and add the version to the
        # parcellation entity instance
        for index, version in enumerate(file_paths):
            # strip the last part of the strings
            print(os.path.dirname(file_paths[index]))
            if (os.path.dirname(file_paths[index])) in atlas_versions:
                print("CHECK")
                stripped_version_area = os.path.basename(file_paths[index])
                stripped_version_area = str.replace(stripped_version_area, ".jsonld", "")
                atlas.get(parcellation_entity).hasVersion = [{"@id": f"{parcellation_entity}{stripped_version_area}", }]

atlas.save("./myFirstOpenMINDSMetadataCollection/")

