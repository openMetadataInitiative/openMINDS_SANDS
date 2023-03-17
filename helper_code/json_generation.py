import os
# customized scraping to get the right info
print(tables_data["table_1"][2])
region_names_cortex = tables_data["table_1"][2]
print(region_names_cortex)
region_names_cortex.remove(region_names_cortex[0])
print(region_names_cortex)

print(tables_data["table_1"][2])
region_names_subcortex = tables_data["table_1"][2]
print(region_names_subcortex)
region_names_subcortex.remove(region_names_subcortex[0])
print(region_names_subcortex)


# generate json code for integration
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

# generate directories for atlas instances
s1 = "Mars_"
j =".jsonld"
enteties = region_names_cortex + region_names_subcortex
directories = {}
path = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/Mars/"

for index,entety in enumerate(enteties):
    directories[index] = path + s1+ entety +j

#generate files

for directory in directories.values():
    with open(directory, "w") as p:
        p.write("")
    p.close()
