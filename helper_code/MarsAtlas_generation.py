import os.path
import glob
import openMINDS.version_manager
import json
import Mars_data_structures
import MarsDataScrape

def generate_orcids(path, *args):
    """create ORCID directories, files and instances ind a semi-automatic manner"""
    # create directory and file shells
    for list in args:
        for item in list:
            for name in item.keys():
                orcid = item.get(name).get("ORCID")
                if orcid is None:
                    continue
                else:
                    orcid_path = f"{path}ORCID_{name}_{os.path.basename(orcid)}{j}"
                    orcid_instance_generation(orcid, orcid_path)


def orcid_instance_generation(orcid, orcid_path):
    if not os.path.isfile(orcid_path):
        # create and save DOI instance
        basic.add_core_ORCID(identifier=orcid)
        basic.save(p)
        # copy contents of created file
        latest = max(glob.glob("./instances/ORCID/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            orcid_name = os.path.basename(orcid_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/ORCID/{orcid_name}"
        # write content to new file
        json_target = open(orcid_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


def generate_dois(path, list):
    """create DOI directories, files and instances ind a semi-automatic manner"""
    doi_str = "https://doi.org/"
    for item in list:
        for version in item.keys():
            doi = item[version]
            doi_stripped = doi.replace(doi_str, "").replace("/", ".")
            if doi is None:
                continue
            else:
                doi_path = f"{path}DOI_{version}_{doi_stripped}{j}"
                doi_instance_generation(doi, doi_path)


def doi_instance_generation(doi, doi_path):
    if not os.path.isfile(doi_path):
        # create and save DOI instance
        basic.add_core_DOI(identifier=doi)
        basic.save(p)
        # copy contents of created file
        latest = max(glob.glob("./instances/DOI/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            doi_name = os.path.basename(doi_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/DOI/{doi_name}"
            f.close()
        # write content to new file
        json_target = open(doi_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


def generate_persons(path, *args):
    """create person directories, files and instances ind a semi-automatic manner"""
    for list in args:
        for item in list:
            for name in item.keys():
                if name is None:
                    continue
                else:
                    person_path = f"{path}{name}{j}"
                    person_instance_generation(item, name, person_path)


def person_instance_generation(item, name, person_path):
    if not os.path.isfile(person_path):
        # create person isntance
        author = basic.add_core_person(givenName=item[name].get("givenName"))
        # add family name and ORCID
        basic.get(author).familyName = item[name].get("familyName")
        basic.get(author).digitalIdentifier = {"@id": item[name].get("ORCID")}
        basic.save(p)
        # copy contents of created file
        latest = max(glob.glob("./instances/person/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            person_name = os.path.basename(person_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/person/{person_name}"
        # write content to new file
        json_target = open(person_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


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


def entity_gen(name, *lists):
    # entity creation
    has_entity_listofdic = []
    entity_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    for list in lists:
        for item in list:
            entity_dic = {"@id" : f"{entity_https}{name}_{item.lower()}"}
            has_entity_listofdic.append(entity_dic)
    return has_entity_listofdic


def terminology_gen(name, *lists):
    # terminology creation
    has_terminology_dic = {}
    has_terminology_dic["@type"] = "https://openminds.ebrains.eu/sands/ParcellationTerminology"
    has_terminology_dic["definedIn"] = None
    has_terminology_dic["hasEntity"] = entity_gen(name, *lists)
    return has_terminology_dic


def version_gen(listofdic):
    has_version_listofdic = []
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    for dic in listofdic:
        for version in dic.keys():
            has_version_dic = {"@id" : f"{version_https}{version}"}
            has_version_listofdic.append(has_version_dic)
    return has_version_listofdic


def generate_atlas(path, mars_authors, regions_cortex, regions_subcortex, docu, info, sName, fName, page, maindoc):
    # generate atlas
    atlas = basic.add_SANDS_brainAtlas(description=info, shortName=sName, fullName=fName,
                                   author=author_gen(mars_authors),
                                   hasTerminology=terminology_gen(sName, regions_cortex, regions_subcortex),
                                   hasVersion=version_gen(docu))
    basic.get(atlas).custodian = [{"@id": "https://openminds.ebrains.eu/instances/person/brovelliAndrea"}]
    basic.get(atlas).digitalIdentifier = [{"@id": f"{maindoc}"}]
    basic.get(atlas).homepage = page
    basic.save(p)
    # copy contents
    latest = max(glob.glob("./instances/brainAtlas/*jsonld"))
    with open(latest, 'r') as f:
        data = json.load(f)
        atlas_name = os.path.basename(path).replace(j, "")
        data["@id"] = f"https://openminds.ebrains.eu/instances/brainAtlas/{atlas_name}"
        f.close()
    # write content to new file
    json_target = open(path, "w")
    json.dump(data, json_target, indent=2, sort_keys=True)
    json_target.write("\n")
    json_target.close()



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
                # docu_https = "https://openminds.ebrains.eu/instances/digitalIdentifier/"
                # doi_str = "https://doi.org/"
                # doi = dic.get(version).get("digitalIdentifier")
                # doi_stripped = doi.replace(doi_str, "").replace("/", ".")
                DOI = dic.get(version).get("digitalIdentifier")
                docu_dic = {"@id": f"{DOI}"}
                # authors
                authors_list_of_dic = []
                author_https = "https://openminds.ebrains.eu/instances/person/"
                authors = dic.get(version).get("authors")
                for author in authors:
                    author_dic = {"@id": f"{author_https}{author}"}
                    authors_list_of_dic.append(author_dic)
                # terminology
                has_entity_listofdic = []
                parcellation_entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
                version_entities = dic.get(version).get("areas")
                for area in version_entities:
                    entity_version_dic= {"@id": f"{parcellation_entity_version_https}{version}_{area.lower()}"}
                    has_entity_listofdic.append(entity_version_dic)
                terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion",
                                   "definedIn": None, "hasEntity": has_entity_listofdic}
                # create atlas version instance
                atlas_version = basic.add_SANDS_brainAtlasVersion(license= license_dic, coordinateSpace= coordinate_space_dic,
                                                                  versionInnovation= version_innovation, accessibility= accessibility_dic,
                                                                  releaseDate= release_date, shortName= short_name, hasTerminology= terminology_dic,
                                                                  fullDocumentation= docu_dic, versionIdentifier=version_identifier)
                basic.get(atlas_version).homepage = dic.get(version).get("homepage")
                basic.get(atlas_version).author = authors_list_of_dic
                basic.get(atlas_version).type = {"@id": f"https://openminds.ebrains.eu/instances/atlasType/"
                                                        f"{dic.get(version).get('atlasType')}"}
                basic.save(p)

            # copy contents of created file
            latest = max(glob.glob("./instances/brainAtlasVersion/*jsonld"))
            with open(latest, 'r') as f:
                data = json.load(f)
                data["@id"] = f"https://openminds.ebrains.eu/instances/brainAtlasVersion/{version}"
            # write content to new file
            json_target = open(f"{entity_path}{version}{j}", "w")
            json.dump(data, json_target, indent=2, sort_keys=True)
            json_target.write("\n")
            json_target.close()



def generate_entities(path, versions, abbreviation, *args):
    """create person directories, files and instances ind a semi-automatic manner"""
    for list in args:
        for area in list:
            if area is None:
                    continue
            else:
                entity_path = f"{path}{abbreviation}_{area.lower()}{j}"
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
                    has_version_dic = {"@id": f"{entity_version_https}{version}_{area.lower()}"}
                    has_version_listOfdic.append(has_version_dic)
        basic.get(entity).hasVersion = has_version_listOfdic
        basic.save(p)

        # copy contents of created file
        latest = max(glob.glob("./instances/parcellationEntity/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            entity_name = os.path.basename(entity_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntity/{entity_name}"
        # write content to new file
        json_target = open(entity_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()



def generate_entity_versions(path, versions):
    """create person directories, files and instances ind a semi-automatic manner"""
    # if not os.path.isfile(path):
    for dic in versions:
        for version in dic.keys():
            for area in dic.get(version).get("areas"):
                entity_ver_path = f"{path}{version}/"
                entity_ver_file_path = f"{entity_ver_path}{version}_{area.lower()}{j}"
                version_identifier = dic.get(version).get("version_identifier")
                entity_version_instance_generation(entity_ver_file_path, area, version_identifier, version)


def entity_version_instance_generation(file_path, area, identifier, version):
    if not os.path.isfile(file_path):
        # create entity version isntance
        entity_version = basic.add_SANDS_parcellationEntityVersion(name=area, versionIdentifier=identifier)
        basic.get(entity_version).lookupLabel = f"{version}_{area}"
        basic.save(p)

        # copy contents of created file
        latest = max(glob.glob("./instances/parcellationEntityVersion/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            entity_ver_name = os.path.basename(file_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntityVersion/{entity_ver_name}"
        # write content to new file
        json_target = open(file_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


if __name__ == '__main__':

    # get Mars Data
    region_names_cortex, region_names_subcortex = MarsDataScrape.datascrape()
    mars_cortex_authors, mars_cortexAndSubcotex_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, versions = Mars_data_structures.data_structures(region_names_cortex, region_names_subcortex)

    # helper vars
    j = ".jsonld"
    p = "./instances/"

    # person dir
    person_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/person/"
    if not person_dir:
        os.mkdir(person_dir)
    # identifier dirs
    identifier_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/"
    if not identifier_dir:
        os.mkdir(identifier_dir)
    doi_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
    if not doi_dir:
        os.mkdir(doi_dir)
    orcid_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"
    if not orcid_dir:
        os.mkdir(orcid_dir)

    # atlas dir
    atlas_dir = f"/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/brainAtlas/{fullName}{j}"
    # atlas version dir
    atlas_version_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
    if not atlas_version_dir:
        os.mkdir(atlas_version_dir)
    # parcellation entity dir
    entity_dir = f"/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntity/{abbreviation}/"
    os.mkdir(entity_dir)
    # parcellation entity version dirs
    entity_ver_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    for dic in versions:
        for version in dic.keys():
            os.mkdir(f"{entity_ver_dir}{version}/")

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function calling
    generate_persons(person_dir, mars_cortex_authors, mars_cortexAndSubcotex_authors)
    generate_dois(doi_dir, full_documentation)
    generate_orcids(orcid_dir, mars_cortex_authors, mars_cortexAndSubcotex_authors)
    generate_atlas(atlas_dir, mars_cortex_authors, region_names_cortex, region_names_subcortex,
                   versions, description, shortName, fullName, homepage, main_documentation)
    generate_atlas_versions(atlas_version_dir, versions)
    generate_entities(entity_dir, versions, abbreviation, region_names_cortex, region_names_subcortex)
    generate_entity_versions(entity_ver_dir, versions)
