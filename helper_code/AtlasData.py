import openMINDS.version_manager
import json

# atlas Data
familyNames = ["Auzias", "Brovelli", "Coulon"]
givenNames = ["Guillaume", "Andrea", "Olivier"]
ORCIDs = ["https://orcid.org/0000-0002-0414-5691", "https://orcid.org/0000-0002-5342-1330", "https://orcid.org/0000-0003-4752-1228"]
dataset_identifiers = ["https://doi.org/10.1002/hbm.23121"]


# variables for constructing correct JSON-LD documents
json_person = "https://openminds.ebrains.eu/instances/"

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

