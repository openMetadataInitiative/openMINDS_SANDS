import os
import openMINDS.version_manager
import glob

# generate directories and filenames for parcellation entity instances
s1 = "Mars_"
j =".jsonld"
# from the data scraper
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

# generate parcellation entity instances
# loop over every file in the parcellation entity folder of the Mars atlas and create isntances
# intialize openMinds instance creator
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
atlas = helper.create_collection()
directory = '/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars'


for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        # strip the area name from the filename
        stripped_filename = str.replace(filename, ".jsonld", "")
        area = str.replace(stripped_filename, "Mars_", "")

        # create parcellation entity instance
        global parcellation_entity = atlas.add_SANDS_parcellationEntity(name = area)
        atlas.get(parcellation_entity).lookupLabel = stripped_filename
        atlas.get(parcellation_entity).nane = area

        # add the versions to hasVersion
        path_to_entity_version = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/" \
                                 "parcellationEntityVersion/"
        version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
        atlas_versions = ["Mars_individual_cortex", "Mars_individual_cortexAndSubcortex", "Mars_HipHop138_cortex",
                          "Mars_Colin27_1998_cortexAndSubcortex"]

        # loop over the directories and files of the parcellatio entity versions and  find the str matching to area

        def find_files(pattern, path):
            files = []
            for filename in glob.iglob(os.path.join(path, '**', pattern), recursive=True):
                if os.path.isfile(filename):
                    files.append(filename)
            if not files:
                return f"No file matching pattern {pattern} found in {path}"
            return files


        file_paths = find_files(area, path_to_entity_version)

        for path in file_paths:
            print(path)

        # check whether the list entries are part of the version list and add the version to the parcellation entity instance
        for version in file_paths:
            if (file_paths[version]) in atlas_versions:
                stripped_version_area = os.path.basename(file_paths[version])
                stripped_version_area = str.replace(stripped_version_area, ".jsonld", "")
                atlas.get(parcellation_entity).hasVersion = [{"@id": f"{parcellation_entity}{stripped_version_area}"]

atlas.save("./myFirstOpenMINDSMetadataCollection/")
