import os
import openMINDS.version_manager
import json
import glob


def generate_entities(path, versions, abbreviation, *args):
    """create person directories, files and instances ind a semi-automatic manner"""
    for list in args:
        for area in list:
            if area is None:
                    continue
            else:
                entity_path = f"{path}{abbreviation}_{area}{j}"
                entity_instance_generation(area, abbreviation, entity_path, versions)


def entity_instance_generation(area, abbreviation, entity_path, versions):
    if not os.path.isfile(entity_path):

        # create entity isntance
        entity = basic.add_SANDS_parcellationEntity(name=area)
        basic.get(entity).lookupLabel = f"{abbreviation}_{area}"

        # versions creation
        has_version_listOfdic = []
        entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
        for dic in versions:
            for version in dic.keys():
                if any(area == version_area for version_area in dic.get(version).get("areas")):
                    has_version_dic = {"@id": f"{entity_version_https}{version}_{area}"}
                    has_version_listOfdic.append(has_version_dic)
        basic.get(entity).hasVersion = has_version_listOfdic
        basic.save("./instances/")

        # copy contents of created file
        latest = max(glob.glob("./instances/parcellationEntity/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
        # write content to new file
        json_target = open(entity_path, "w")
        json.dump(data, json_target, indent=6)
        json_target.close()


if __name__ == '__main__':

    # directories and variables
    entity_dir = f"/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/{abbreviation}/"
    os.mkdir(entity_dir)
    j = ".jsonld"
    p = "./instances/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function calling
    generate_entities(entity_dir, versions, abbreviation, region_names_cortex, region_names_subcortex)
