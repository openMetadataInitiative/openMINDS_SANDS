import os
import openMINDS.version_manager
import json
import glob

def generate_entity_versions(path, versions):
    """create person directories, files and instances ind a semi-automatic manner"""
    # if not os.path.isfile(path):
        for dic in versions:
            for version in dic.keys():
                print(version)
                for area in dic.get(version).get("areas"):
                    # if area is None:
                        # continue
                    # elif not os.path.isdir(f"{path}{version}/"):
                        print(f"{path}{version}/")

                        entity_ver_path = f"{path}{version}/"
                        entity_ver_file_path = f"{entity_ver_path}{version}_{area}{j}"
                        version_identifier = dic.get(version).get("version_identifier")
                        entity_version_instance_generation(entity_ver_file_path, area, version_identifier, version)


def entity_version_instance_generation(file_path, area, identifier, version):
    if not os.path.isfile(file_path):
        # create entity version isntance
        entity_version = basic.add_SANDS_parcellationEntityVersion(name=area, versionIdentifier=identifier)
        basic.get(entity_version).lookupLabel = f"{version}_{area}"
        basic.save("./instances/")

        # copy contents of created file
        latest = max(glob.glob("./instances/parcellationEntityVersion/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
        # write content to new file
        json_target = open(file_path, "w")
        json.dump(data, json_target, indent=4)
        json_target.close()


if __name__ == '__main__':

    # directories and variables
    entity_ver_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    j = ".jsonld"
    for dic in versions:
        for version in dic.keys():
            os.mkdir(f"{entity_ver_dir}{version}/")
    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()


    # function calling
    generate_entity_versions(entity_ver_dir, versions)