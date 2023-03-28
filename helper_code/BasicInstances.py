import os.path
import glob
import openMINDS.version_manager
import json

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
        # write content to new file
        json_target = open(orcid_path, "w")
        json.dump(data, json_target, indent=6)
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
            f.close()
        # write content to new file
        json_target = open(doi_path, "w")
        json.dump(data, json_target, indent=6)
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
        # write content to new file
        json_target = open(person_path, "w")
        json.dump(data, json_target, indent=6)
        json_target.close()


if __name__ == '__main__':

    # directories and variables
    person_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/person/"
    os.mkdir(person_dir)
    identifier_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/"
    os.mkdir(identifier_dir)
    doi_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
    os.mkdir(doi_dir)
    orcid_dir = "/home/kiwitz1/PycharmProjects/OpenMinds/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"
    os.mkdir(orcid_dir)
    j = ".jsonld"
    p = "./instances/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    # function calling
    generate_persons(person_dir, mars_cortex_authors, mars_cortexAndSubcotex_authors)
    generate_dois(doi_dir, full_documentation)
    generate_orcids(orcid_dir, mars_cortex_authors, mars_cortexAndSubcotex_authors)