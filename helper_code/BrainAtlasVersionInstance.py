import os
import openMINDS.version_manager
import json
import glob


def generate_atlas_versions(entity_path, versions):
    if not os.path.isfile(entity_path):
        for dic in versions:
            for version in dic.keys():
                # retrieve license data
                license_https = "https://openminds.ebrains.eu/instances/licenses/"
                license_info = dic.get(version).get("license")
                license_dic = {"@id": f"{license_https}{license_info}"}

                # retrieve coordinate space
                coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"
                coordinate_space = dic.get(version).get("reference_space")
                coordinate_space_dic = {"@id": f"{coordinate_space_https}{coordinate_space}"}

                # version inno
                version_innovation = dic.get(version).get("version_innovation")
                # bersion identifier
                version_identifier = dic.get(version).get("version_identifier")

                # access
                accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/"
                accessibility = dic.get(version).get("accessibility")
                accessibility_dic = {"@id": f"{accessibility_https}{accessibility}"}

                # release
                release_date = dic.get(version).get("release_date")

                # shortname
                short_name = dic.get(version).get("short_name")

                # docu
                docu_https = "https://openminds.ebrains.eu/core/DOI/"
                doi_str = "https://doi.org/"
                doi = dic.get(version).get("digitalIdentifier")
                doi_stripped = doi.replace(doi_str, "").replace("/", ".")
                full_doc_name = dic.get(version).get("full_doc_name")
                docu_dic = {"@id": f"{docu_https}DOI_{full_doc_name}_{doi_stripped}"}

                # terminology
                has_entity_listofdic = []
                parcellation_entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
                version_entities = dic.get(version).get("areas")
                for area in version_entities:
                    entity_version_dic= {"@id": f"{parcellation_entity_version_https}{short_name}_{area}"}
                    has_entity_listofdic.append(entity_version_dic)
                terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion",
                                   "definedIn": None, "hasEntity": has_entity_listofdic}

                # create atlas version instance
                atlas_version = basic.add_SANDS_brainAtlasVersion(license= license_dic, coordinateSpace= coordinate_space_dic,
                                                                  versionInnovation= version_innovation, accessibility= accessibility_dic,
                                                                  releaseDate= release_date, shortName= short_name, hasTerminology= terminology_dic,
                                                                  fullDocumentation= docu_dic, versionIdentifier=version_identifier)
                basic.get(atlas_version).homepage = dic.get(version).get("homepage")
                basic.get(atlas_version).type = {"@id": f"https://openminds.ebrains.eu/instances/atlasType/{dic.get(version).get('atlasType')}"}
                basic.save("./instances/")

            # copy contents of created file
            latest = max(glob.glob("./instances/brainAtlasVersion/*jsonld"))
            with open(latest, 'r') as f:
                data = json.load(f)
            # write content to new file
            json_target = open(f"{entity_path}{version}{j}", "w")
            json.dump(data, json_target, indent=6)
            json_target.close()


if __name__ == '__main__':

    # directories and variables
    atlas_version_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
    j = ".jsonld"
    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function calling
    generate_atlas_versions(atlas_version_dir, versions)