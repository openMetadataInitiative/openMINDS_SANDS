import os
# generate parcellation entity versions for each parcellation entity
# list of subcortical vs cortical from the scrype script
# combine scrapes into unified datastructure
entities = region_names_cortex + region_names_subcortex
entities_label = [0] * (len(region_names_cortex)+len(region_names_subcortex))
for index in range(len(entities_label)):
    if index < len(region_names_cortex):
        entities_label[index] = "c"
    else:
        entities_label[index] = "s"
all_entitites = zip(entities, entities_label)
all_entitites = list(all_entitites)

# loop over each parcellation entity and create parcelation enetiy versions strings
atlas_versions = ["Mars_individual_cortex", "Mars_individual_cortexAndSubcortex", "Mars_HipHop138_cortex", "Mars_Colin27_1998_cortexAndSubcortex"]
cortex_versions = ["Mars_individual_cortex", "Mars_HipHop138_cortex"]
cortexAndSubcortex_versions = ["Mars_individual_cortexAndSubcortex", "Mars_Colin27_1998_cortexAndSubcortex"]
path = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
j = ".jsonld"
sep = "/"
print(all_entitites)
for version in atlas_versions:
    os.mkdir(f"{path}{version}")


for area in all_entitites:
    if area[1] == "c":
        for version in cortex_versions:
            with open(f"{path}{version}{sep}{area[0]}{j}", "w") as p:
                p.write("")
    else:
        for version in cortexAndSubcortex_versions:
            with open(f"{path}{version}{sep}{area[0]}{j}", "w") as z:
                z.write("")


# create new directoreis and filenames and create aprcellatioj enetity version subdirectories

# generate directories and filenames for atlas instances

directories = {}


for index, entity in enumerate(entities):
    directories[index] = path + s1 + entity + j

# generate files

for directory in directories.values():
    with open(directory, "w") as p:
        p.write("")
    p.close()