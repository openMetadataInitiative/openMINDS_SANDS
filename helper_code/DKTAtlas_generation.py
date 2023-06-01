import os.path
import glob
import openMINDS.version_manager
import json
import DKT_data_structures


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
        latest = max(glob.glob(f"{p}ORCID/*jsonld"))
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
        latest = max(glob.glob(f"{p}DOI/*jsonld"))
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
        latest = max(glob.glob(f"{p}person/*jsonld"))
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
                author_dic = {"@id": f"{person_https}{name}"}
                author_listofdic.append(author_dic)
    return author_listofdic


def entity_gen(name, *entities):
    # entity creation
    has_entity_listofdic = []
    entity_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    for set in entities:
        for area in set:
            if area is not None:
                entity_dic = {"@id": f"{entity_https}{name}_{area}"}
                has_entity_listofdic.append(entity_dic)
    return has_entity_listofdic


def terminology_gen(name, *areas):
    # terminology creation
    has_terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology", "definedIn": None,
                           "hasEntity": entity_gen(name, *areas)}
    return has_terminology_dic


def version_gen(listofdic):
    has_version_listofdic = []
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    for dic in listofdic:
        for version in dic.keys():
            has_version_dic = {"@id": f"{version_https}{version}"}
            has_version_listofdic.append(has_version_dic)
    return has_version_listofdic


def generate_atlas(path, mars_authors, versions, info, sName, fName, page, maindoc, abbreviation, *areas):
    # generate atlas
    atlas = basic.add_SANDS_brainAtlas(description=info, shortName=sName, fullName=fName,
                                       author=author_gen(mars_authors),
                                       hasTerminology=terminology_gen(abbreviation, *areas),
                                       hasVersion=version_gen(versions))
    basic.get(atlas).custodian = [{"@id": "https://openminds.ebrains.eu/instances/person/kleinArno"}]
    basic.get(atlas).digitalIdentifier = [{"@id": f"{maindoc}"}]
    basic.get(atlas).homepage = page
    basic.save(p)
    # copy contents
    latest = max(glob.glob(f"{p}brainAtlas/*jsonld"))
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


def generate_atlas_versions(entity_path, versions, areas_versions_hierachry):
    if not os.path.isfile(entity_path):
        for dic in versions:
            for version in dic.keys():
                license_dic = license(dic, version)
                # retrieve coordinate space
                coordinate_space_dic = coordinateSpace(dic, version)
                # version inno
                version_innovation = dic.get(version).get("version_innovation")
                # bersion identifier
                version_identifier = dic.get(version).get("version_identifier")
                # access
                accessibility_dic = accessibility_extract(dic, version)
                # release
                release_date = dic.get(version).get("release_date")
                # shortname
                short_name = dic.get(version).get("short_name")
                # docu
                DOI = dic.get(version).get("digitalIdentifier")
                docu_dic = {"@id": f"{DOI}"}
                # authors
                authors_list_of_dic = authors_version(dic, version)
                # terminology
                terminology_dic = terminology_versions(version, areas_versions_hierachry)
                # altVersion
                version_https, altVersion_list_of_dic = alternativeVersions(dic, version)
                # newVersion
                newVersion_list_of_dic = newerVersion(version_https, dic, version)
                # create atlas version instance
                atlasVersionInstance_creation(accessibility_dic, altVersion_list_of_dic, authors_list_of_dic,
                                              coordinate_space_dic, dic, docu_dic, license_dic, newVersion_list_of_dic,
                                              release_date, short_name, terminology_dic, version, version_identifier,
                                              version_innovation)

            # copy contents of created file
            latest = max(glob.glob(f"{p}brainAtlasVersion/*jsonld"))
            with open(latest, 'r') as f:
                data = json.load(f)
                data = replace_empty_lists(data)
                data["@id"] = f"https://openminds.ebrains.eu/instances/brainAtlasVersion/{version}"
            # write content to new file
            json_target = open(f"{entity_path}{version}{j}", "w")
            json.dump(data, json_target, indent=2, sort_keys=True)
            json_target.write("\n")
            json_target.close()


def atlasVersionInstance_creation(accessibility_dic, altVersion_list_of_dic, authors_list_of_dic, coordinate_space_dic,
                                  dic, docu_dic, license_dic, newVersion_list_of_dic, release_date, short_name,
                                  terminology_dic, version, version_identifier, version_innovation):
    atlas_version = basic.add_SANDS_brainAtlasVersion(license=license_dic, coordinateSpace=coordinate_space_dic,
                                                      versionInnovation=version_innovation,
                                                      accessibility=accessibility_dic,
                                                      releaseDate=release_date, shortName=short_name,
                                                      hasTerminology=terminology_dic,
                                                      fullDocumentation=docu_dic, versionIdentifier=version_identifier)
    basic.get(atlas_version).isAlternativeVersionOf = altVersion_list_of_dic
    basic.get(atlas_version).isNewVersionOf = newVersion_list_of_dic
    basic.get(atlas_version).homepage = dic.get(version).get("homepage")
    basic.get(atlas_version).author = authors_list_of_dic
    basic.get(atlas_version).type = {"@id": f"https://openminds.ebrains.eu/instances/atlasType/"
                                            f"{dic.get(version).get('atlasType')}"}
    basic.save(p)


def newerVersion(version_https, dic, version):
    newVersion_list_of_dic = []
    newVersions = dic.get(version).get("newVersion")
    if newVersions is not None:
        for newVersion in newVersions:
            newVersion_dic = {"@id": f"{version_https}{newVersion}"}
            newVersion_list_of_dic.append(newVersion_dic)
    return newVersion_list_of_dic


def alternativeVersions(dic, version):
    altVersion_list_of_dic = []
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    altVersions = dic.get(version).get("altVersion")
    if altVersions is not None:
        for altVersion in altVersions:
            altVersion_dic = {"@id": f"{version_https}{altVersion}"}
            altVersion_list_of_dic.append(altVersion_dic)
    return version_https, altVersion_list_of_dic


def terminology_versions(version, areas_versions_hierachry):
    has_entity_listofdic = []
    parcellation_entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
    # the following variable defines that we just want the "child" structure, we may improve this in the future for cases where
    # we have version specific parent structures
    version_entities = (t[0] for t in areas_versions_hierachry[version])
    for area in version_entities:
        entity_version_dic = {"@id": f"{parcellation_entity_version_https}{version}_{area}"}
        has_entity_listofdic.append(entity_version_dic)
    terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion",
                       "definedIn": None, "hasEntity": has_entity_listofdic}
    return terminology_dic


def authors_version(dic, version):
    authors_list_of_dic = []
    author_https = "https://openminds.ebrains.eu/instances/person/"
    authors = dic.get(version).get("authors")
    for author in authors:
        author_dic = {"@id": f"{author_https}{author}"}
        authors_list_of_dic.append(author_dic)
    return authors_list_of_dic


def accessibility_extract(dic, version):
    accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/"
    accessibility = dic.get(version).get("accessibility")
    accessibility_dic = {"@id": f"{accessibility_https}{accessibility}"}
    return accessibility_dic


def coordinateSpace(dic, version):
    coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"
    coordinate_space = dic.get(version).get("reference_space")
    coordinate_space_dic = {"@id": f"{coordinate_space_https}{coordinate_space}"}
    return coordinate_space_dic


def license(dic, version):
    # retrieve license data
    license_https = "https://openminds.ebrains.eu/instances/licenses/"
    license_info = dic.get(version).get("license")
    license_dic = {"@id": f"{license_https}{license_info}"}
    return license_dic


def generate_entities(path, abbreviation, areas_versions_hierachry, areas_unique, parents_unique):
    """create parcellation entitites using unique children and parent structures previously defined
    in the data structure module"""

    for area in areas_unique:
        # version and parent structures as well as the path for the entity generation
        entity_path = f"{path}{abbreviation}_{area}{j}"
        entity_version_list = version_extraction_PE(area, areas_versions_hierachry)
        parent_structure_list = parent_extraction_PE(area, areas_versions_hierachry)
        # create entity
        if area is not None:
            entity_instance_generation(area, abbreviation, entity_path, entity_version_list, parent_structure_list)

    for area in parents_unique:
        # version and parent structures as well as the path for the entity generation
        entity_path = f"{path}{abbreviation}_{area}{j}"
        entity_version_list = version_extraction_PE(area, areas_versions_hierachry, parent_versions=False)
        parent_structure_list = parent_extraction_PE(area, areas_versions_hierachry)
        # create entity
        if area is not None:
            entity_instance_generation(area, abbreviation, entity_path, entity_version_list, parent_structure_list)


def version_extraction_PE(area, areas_versions_hierachry, parent_versions=True):
    entity_version_list = []
    # check whether they are part of a specific version, add version
    for version, areas_version in areas_versions_hierachry.items():
        if any(area in tuple for tuple in areas_version):
            if parent_versions:
                entity_version_list.append(version)
    return entity_version_list


def parent_extraction_PE(area, areas_versions_hierachry):
    parent_structure_list = []
    # check whether they are part of a specific version, add version
    for version, areas_version in areas_versions_hierachry.items():
        if any(area in tuple for tuple in areas_version):
            # loop over the areas of the version to extract the parent structures
            for i, tuple in enumerate(areas_version):
                if area in tuple and area is not None:
                    parent_structure_list.extend(areas_version[i][tuple.index(area)+1:])
                    parent_structure_list= [x for x in parent_structure_list if x is not None]
                    continue
    return parent_structure_list


def entity_instance_generation(area, abbreviation, entity_path, entity_version_list, parent_structure_list):
    """instance creation of parcellation entitites"""
    if not os.path.isfile(entity_path):

        # create entity isntance
        entity = basic.add_SANDS_parcellationEntity(name=area)
        basic.get(entity).lookupLabel = f"{abbreviation}_{area}"

        # add entity version creation
        has_version_listOfdic = []
        entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
        if entity_version_list:
            for version in entity_version_list:
                has_version_dic = {"@id": f"{entity_version_https}{version}_{area}"}
                has_version_listOfdic.append(has_version_dic)
        basic.get(entity).hasVersion = has_version_listOfdic

        # add parent structures
        has_parent_listOfdic = []
        parent_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
        if parent_structure_list:
            has_parent_dic = {"@id": f"{parent_https}{abbreviation}_{parent_structure_list[0]}"}
            has_parent_listOfdic.append(has_parent_dic)
        basic.get(entity).hasParent = has_parent_listOfdic
        basic.save(p)

        # copy contents of created file
        latest = max(glob.glob(f"{p}parcellationEntity/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            data = replace_empty_lists(data)
            entity_name = os.path.basename(entity_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntity/{entity_name}"
        # write content to new file
        json_target = open(entity_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


def generate_entity_versions(path, areas_versions_hierachry, versions):
    """create person directories, files and instances ind a semi-automatic manner"""
    # if not os.path.isfile(path):
    for version, areas_version in areas_versions_hierachry.items():
        entity_ver_path = f"{path}{version}/"
        for area_tuple in areas_version:
            area = area_tuple[0]
            parent = area_tuple[1]
            entity_ver_file_path = f"{entity_ver_path}{version}_{area}{j}"
            entity_version_instance_generation(entity_ver_file_path, area, parent, version, versions)


def entity_version_instance_generation(file_path, area, parent, version, versions):
    if not os.path.isfile(file_path):
        # get version identifier and annotation infos
        for dic in versions:
           if version in dic.keys():
               global version_identifier
               version_identifier = dic.get(version).get("version_identifier")
               global criteriaQualityType
               criteriaQualityType = dic.get(version).get("criteriaQualityType")
               global annotationCriteriaType
               annotationCriteriaType = dic.get(version).get("annotationCriteriaType")
               global laterality
               laterality = dic.get(version).get("laterality")
               global type
               type = dic.get(version).get("annotationType")
               break

        # intiliaize instance
        entity_version = basic.add_SANDS_parcellationEntityVersion(name=area, versionIdentifier=version_identifier)
        basic.get(entity_version).lookupLabel = f"{version}_{area}"

        # parent info
        has_parent_listOfdic = []
        parent_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
        if parent is not None:
            has_parent_dic = {"@id": f"{parent_https}{abbreviation}_{parent}"}
            has_parent_listOfdic.append(has_parent_dic)
        basic.get(entity_version).hasParent = has_parent_listOfdic

        # annotation info
        has_annotation_listOfdic = get_annotation(annotationCriteriaType, criteriaQualityType, laterality, type)
        basic.get(entity_version).hasAnnotation = has_annotation_listOfdic

        # save instance
        basic.save(p)

        # copy contents of saved instance
        latest = max(glob.glob(f"{p}parcellationEntityVersion/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            data = replace_empty_lists(data)
            entity_ver_name = os.path.basename(file_path).replace(j, "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntityVersion/{entity_ver_name}"


        # write content to new file
        json_target = open(file_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()


def get_annotation(annotationCriteriaType, criteriaQualityType, laterality, type):
    has_annotation_listOfdic = []
    for quality in criteriaQualityType:
        for criteria in annotationCriteriaType:
            for lat in laterality:
                annotation = addon.add_SANDS_atlasAnnotation(criteriaQualityType=quality, criteriaType=criteria,
                                                             type=type)
                addon.get(annotation).laterality = lat
                addon.save(p)
                latest = max(glob.glob(f"{p}atlasAnnotation/*jsonld"))
                with open(latest, 'r') as f:
                    data = json.load(f)
                    data = replace_empty_lists(data)
                    del data["@id"]
                    del data["@context"]
                    data["laterality"] = {"@id": f"https://openminds.ebrains.eu/instances/laterality/{lat}"}
                    data["criteriaType"] = {"@id": f"https://openminds.ebrains.eu/instances/annotationCriteriaType/{criteria}"}
                    data["criteriaQualityType"] = {"@id": f"https://openminds.ebrains.eu/instances/criteriaQualityType/{quality}"}
                    data["type"] = {"@id": f"https://openminds.ebrains.eu/controlledTerms/AnnotationType/{type}"}
                    has_annotation_listOfdic.append(data)
                f.close()
    return has_annotation_listOfdic



def replace_empty_lists(obj):
    if isinstance(obj, list) and not obj:
        return None
    elif isinstance(obj, dict):
        return {k: replace_empty_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_empty_lists(elem) for elem in obj]
    else:
        return obj


if __name__ == '__main__':

    # get DKT Data
    DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, \
        shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = DKT_data_structures.data_structures()
    # helper vars
    j = ".jsonld"
    p = "./instances/PythonLibrary/"

    # person dir
    person_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/person/"
    os.mkdir(person_dir)
    # identifier dirs
    identifier_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/digitalIdentifier/"
    os.mkdir(identifier_dir)
    doi_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
    os.mkdir(doi_dir)
    orcid_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"
    os.mkdir(orcid_dir)

    # atlas dir
    atlas_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/{fullName}{j}"
    # atlas version dir
    atlas_version_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"

    # parcellation entity dir
    entity_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntity/{abbreviation}/"
    os.mkdir(entity_dir)
    # parcellation entity version dirs
    entity_ver_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    for dic in versions:
        for version in dic.keys():
            os.mkdir(f"{entity_ver_dir}{version}/")

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()
    addon = helper.create_collection()

    # function calling
    generate_persons(person_dir, DKT_authors)
    generate_dois(doi_dir, full_documentation)
    generate_orcids(orcid_dir, DKT_authors)
    generate_atlas(atlas_dir, DKT_authors,
                   versions, description, shortName, fullName, homepage, main_documentation, abbreviation, areas_unique, parents_unique)
    generate_atlas_versions(atlas_version_dir, versions, areas_versions_hierachry)
    generate_entities(entity_dir, abbreviation, areas_versions_hierachry, areas_unique, parents_unique)
    generate_entity_versions(entity_ver_dir, areas_versions_hierachry, versions)
