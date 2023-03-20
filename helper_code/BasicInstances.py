
# Initialise the local copy of openMINDS, set version, iitialize helper and collection
openMINDS.version_manager.init()
openMINDS.version_manager.version_selection('v3')
helper = openMINDS.Helper()
atlas = helper.create_collection()


# schema creation persons and ORCIDS
for i in enumerate(givenNames):
        # persons
        person = atlas.add_core_person(givenName = givenNames[i[0]])
        atlas.get(person).familyName = str(familyNames[i[0]])
        # ORCIDS
        orcid = atlas.add_core_ORCID()
        atlas.get(orcid).identifier = ORCIDs[i[0]]
        # add ORCIDs to person instances
        atlas.get(person).digitalIdentifier = [{"@id": orcid}]
        # change @ids from local host to actual orcid



# schema creation DOIs
for i in dataset_identifiers:
        # dois
        doi = atlas.add_core_DOI()
        atlas.get(doi).identifier = i

atlas.save("./myFirstOpenMINDSMetadataCollection/")