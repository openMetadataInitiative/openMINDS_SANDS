import MarsDataScrape

def data_structures():
    # atlas info
    mars_cortex_authors = [{"auziasGuillaume" : {"familyName" : "Auzias", "givenName" : "Guillaume", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}},
                           {"brovelliAndrea" : {"familyName" : "Brovelli", "givenName" : "Andrea", "ORCID" : "https://orcid.org/0000-0002-5342-1330"}},
                            {"coulonOlivier" : {"familyName" : "Coulon", "givenName" : "Olivier", "ORCID" : "https://orcid.org/0000-0003-4752-1228"}}]

    mars_cortexAndSubcotex_authors = [{"brovelliAndrea" : {"familyName" : "Brovelli", "givenName" : "Andrea", "ORCID" : "https://orcid.org/0000-0002-5342-1330"}},
                                      {"badierJeanmichael" : {"familyName" : "Badier", "givenName" : "Jean-Michael", "ORCID" : "https://orcid.org/0000-0002-7272-6455"}},
                                      {"boniniFrancesca" : {"familyName" : "Bonini", "givenName" : "Francesca", "ORCID" : None}},
                                      {"bartolomeiFabrice" : {"familyName" : "Bartolomei", "givenName" : "Fabrice", "ORCID" : None}},
                                      {"coulonOlivier" : {"familyName" : "Coulon", "givenName" : "Olivier", "ORCID" : "https://orcid.org/0000-0003-4752-1228"}},
                                      {"auziasGuillaume" : {"familyName" : "Auzias", "givenName" : "Guillaume", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}}]
    full_documentation =  [{"Mars_cortex": "https://doi.org/10.1002/hbm.23121"},{"Mars_cortexAndSubcortex": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016"}]

    description = "MarsAtlas is a model of cortical parcellation. It can be applied to any cortical surface via the HipHop parameterization pipeline, available in the BrainVisa Cortical Surface Toolbox, under the Anatomy category."
    abbreviation = "Mars"
    fullName = "MarsAtlas"
    shortName = "MarsAtlas"
    homepage = "https://meca-brain.org/software/marsatlas/"
    # versions is a list of all versions stored as dictionaries with reference spaces and areas attached IMPORTANT
    versions = [{"Mars_v1_cortex": {"reference_space": "Mars_HipHop138", "areas": region_names_cortex, "accessibility": "freeAccess",
                                    "atlasType": "parcellationScheme", "version_identifier": "v1", "version_innovation": "This is the first version of this research product",
                                    "release_date": "2016-01-27", "short_name": "Mars_v1_c", "homepage": "https://meca-brain.org/software/marsatlas/",
                                    "license":"CeCILL-B", "digitalIdentifier": "https://doi.org/10.1002/hbm.23121", "full_doc_name": "Mars_cortex",
                                    "authors": ["auziasGuillaume", "brovelliAndrea", "coulonOlivier"]}},
                {"Mars_v2_cortexAndSubcortex": {"reference_space" : "Colin27_1998", "areas" : region_names_cortex + region_names_subcortex, "accessibility": "freeAccess",
                                                "atlasType": "parcellationScheme", "version_identifier": "v2", "version_innovation": "This is the second version of this research product",
                                                "release_date": "2017-01-25", "short_name": "Mars_v2_cs", "homepage": "https://meca-brain.org/software/marsatlas-subcortical/",
                                                "license":"CeCILL-B", "digitalIdentifier": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016", "full_doc_name": "Mars_cortexAndSubcortex",
                                                "authors": ["brovelliAndrea", "badierJeanmichael", "boniniFrancesca", "bartolomeiFabrice", "coulonOlivier", "auziasGuillaume"]}}]

    return (mars_cortex_authors, mars_cortexAndSubcotex_authors, full_documentation, description, abbreviation, fullName, shortName, homepage, versions)


if __name__ == '__main__':

    Mars_DataScrape.datascrape()
    mars_cortex_authors, mars_cortexAndSubcotex_authors, full_documentation, description, abbreviation, fullName, shortName, homepage, versions = data_structures()
    region_names_cortex, region_names_subcortex = datascrape()
