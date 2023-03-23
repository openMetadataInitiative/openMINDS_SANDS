
# generate parcellation enetity regions for the atlas instance instance
with open("/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/helper_code/MarsAtlasRegions_subcortex.txt", 'w') as f:
    open = "{"
    close = "}"
    instance = "\"@id\": \"https://openminds.ebrains.eu/instances/parcellationEntity/"

    for index, area in enumerate(region_names_subcortex):
        f.write(f"{open}\n")
        f.write(f"{instance}{region_names[index]}\"\n")
        f.write(f"{close},\n")
f.close()

with open("/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/helper_code/MarsAtlasRegions_cortex.txt", 'w') as d:
    open = "{"
    close = "}"
    instance = "\"@id\": \"https://openminds.ebrains.eu/instances/parcellationEntity/"

    for index, area in enumerate(region_names_cortex):
        d.write(f"{open}\n")
        d.write(f"{instance}{region_names[index]}\"\n")
        d.write(f"{close},\n")
d.close()




# schema creation Brain atlas
marsAtlas = atlas.add_SANDS_brainAtlas(fullName = "MarsAtlas", hasVersion =,  )
