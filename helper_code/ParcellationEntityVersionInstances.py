import os
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

# create percellation entity version directories
atlas_versions = ["Mars_individual_cortex", "Mars_individual_cortexAndSubcortex", "Mars_HipHop138_cortex", "Mars_Colin27_1998_cortexAndSubcortex"]
cortex_versions = ["Mars_individual_cortex", "Mars_HipHop138_cortex"]
cortexAndSubcortex_versions = ["Mars_individual_cortexAndSubcortex", "Mars_Colin27_1998_cortexAndSubcortex"]
path = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
j = ".jsonld"
sep = "/"
us = "_"
print(all_entitites)
for version in atlas_versions:
    os.mkdir(f"{path}{version}")

# create instance files for each parcellation entity version directory
for area in all_entitites:
    # create jsonlds for the subcortex atlases (they always include corttex and subcortex)
    for version in cortexAndSubcortex_versions:
        with open(f"{path}{version}{sep}{version}{us}{area[0]}{j}", "w") as z:
            z.write("")
    # create the atlases that only onvolve corticla parcellations
    if area[1] == "c":
        for version in cortex_versions:
            with open(f"{path}{version}{sep}{version}{us}{area[0]}{j}", "w") as p:
                p.write("")

# to