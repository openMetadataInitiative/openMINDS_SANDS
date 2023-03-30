import os
import openMINDS.version_manager
import json
import glob







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
