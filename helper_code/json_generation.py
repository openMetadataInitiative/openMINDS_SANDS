# customized scraping to get the right info
print(tables_data["table_1"][2])
region_names = tables_data["table_1"][2]
print(region_names)
region_names.remove(region_names[0])
print(region_names)

# generate json code for integration
with open("/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/helper_code/MarsAtlasRegions.txt", 'w') as f:
    f.write("Mars_Areas\n")
    open = "{"
    close = "}"
    instance = "\"@id\": \"https://openminds.ebrains.eu/instances/parcellationEntity/"

    for index, area in enumerate(region_names):
        f.write(f"{open}\n")
        f.write(f"{instance}{region_names[index]}\"\n")
        f.write(f"{close},\n")
f.close()




