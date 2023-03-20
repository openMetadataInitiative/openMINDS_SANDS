import os
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
