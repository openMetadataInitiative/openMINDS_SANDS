import os.path
import glob
import openMINDS.version_manager
import json


def author_gen(listofdic):
    author_listofdic = []
    person_https = "https://openminds.ebrains.eu/instances/person/"
    for item in listofdic:
        for name in item.keys():
            if name is None:
                continue
            else:
                author_dic = {"@id":f"{person_https}{name}"}
                author_listofdic.append(author_dic)
    return author_listofdic


def entity_gen(*lists):
    # entity creation
    has_entity_listofdic = []
    entity_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    for list in lists:
        for item in list:
            entity_dic = {"@id" : f"{entity_https}{item}"}
            has_entity_listofdic.append(entity_dic)
            print(has_entity_listofdic)
    return has_entity_listofdic


def terminology_gen(*lists):
    # terminology creation
    has_terminology_dic = {}
    has_terminology_dic["@type"] = "https://openminds.ebrains.eu/sands/ParcellationTerminology"
    has_terminology_dic["definedIn"] = None
    has_terminology_dic["hasEntity"] = entity_gen(*lists)
    return has_terminology_dic


def version_gen(listofdic):
    has_version_listofdic = []
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    for dic in listofdic:
        for version in dic.keys():
            has_version_dic = {"@id" : f"{version_https}{version}"}
            has_version_listofdic.append(has_version_dic)
    return has_version_listofdic


def generate_atlas(path, mars_authors, regions_cortex, regions_subcortex, docu, info, sName, fName):
    # generate atlas
    atlas = basic.add_SANDS_brainAtlas(description=info, shortName=sName, fullName=fName,
                                   author=author_gen(mars_authors),
                                   hasTerminology=terminology_gen(regions_cortex, regions_subcortex),
                                   hasVersion=version_gen(docu))
    basic.get(atlas).custodian = [{"@id": "https://openminds.ebrains.eu/instances/person/brovelliAndrea"}]
    basic.get(atlas).digitalIdentifier = [{"@id": "https://openminds.ebrains.eu/instances/digitalIdentifier/DOI_Mars_10.1002.hbm.23121"}]
    basic.get(atlas).homepage = [{"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Mars_v1_cortex_homepage"},
                             {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Mars_v2_cortexAndSubcortex_homepage"}]
    basic.save("./instances/")
    # copy contents
    latest = max(glob.glob("./instances/brainAtlas/*jsonld"))
    with open(latest, 'r') as f:
        data = json.load(f)
        f.close()
    # write content to new file
    json_target = open(path, "w")
    json.dump(data, json_target, indent=6)
    json_target.close()


if __name__ == '__main__':

    # directories and variables
    j = ".jsonld"
    atlas_dir = f"/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/brainAtlas/{fullName}{j}"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function call
    generate_atlas(atlas_dir, mars_cortex_authors, region_names_cortex, region_names_subcortex,
                   full_documentation, description, shortName, fullName)
