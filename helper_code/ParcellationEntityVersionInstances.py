import os
import openMINDS.version_manager
import json
import glob

def generate_entity_versions(path, versions):
    """create person directories, files and instances ind a semi-automatic manner"""
    if not os.path.isfile(path):
        for dic in versions:
            for version in dic.keys():
                for area in dic.get(version).get("areas"):
                    if area is None:
                        continue
                    elif not os.path.isdir(f"{path}{version}/"):
                        entity_ver_path = os.mkdir(f"{path}{version}/")
                        entity_ver_file_path = f"{entity_ver_path}{version}_{area}{j}"
                        entity_version_instance_generation(area, entity_ver_file_path, version, versions)


def entity_version_instance_generation(area, file_path, version, versions):
    if not os.path.isfile(file_path):
        # create entity version isntance
        entity_version = basic.add_SANDS_parcellationEntityVersion(name=area)
        basic.get(entity).lookupLabel = f"{version}_{area}"

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
    entity_ver_dir = f"/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    j = ".jsonld"
    p = "./instances/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function calling
    generate_entity_versions(entity_ver_dir, versions)
