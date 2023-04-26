import MarsDataScrape

def data_structures(lista , listb):
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
    full_documentation =  [{"DKT31": "https://www.frontiersin.org/articles/10.3389/fnins.2012.00171/full"}]

    description = "Mindboggle-101 surface and volume brain atlases (anatomical labels from a population of brains)."
    abbreviation = "DKT"
    fullName = "Desikan–Killiany–Tourville Atlas"
    shortName = "DKT"
    homepage = "https://osf.io/kgdey/wiki/home/"
    areas = ["temporalLobeMedialAspect_enthorinalCortex", "temporalLobeMedialAspect_parahippocampalGyrus","temporalLobeMedialAspect_fusiformGyrus",
             "temporalLobeLateralAspect_superiorTemporalGyrus", "temporalLobeLateralAspect_middleTemporalGyrus", "temporalLobeLateralAspect_inferiorTemporalGyrus",
             "temporalLobeLateralAspect_transverseTemporalGyrus", "frontalLobe_superiorFrontal", "frontalLobe_middleFrontalGyrusRostral",
             "frontalLobe_middleFrontalGyrusCaudal","frontalLobe_inferiorFrontalGyrusParsOpercularis","frontalLobe_inferiorFrontalGyrusParsOrbitalis",
             "frontalLobe_inferiorFrontalGyrusParsTriangularis","frontalLobe_orbitofrontalGyrus","frontalLobe_lateralDivision","frontalLobe_medialDivision",
             "frontalLobe_precentralGyrus","frontalLobe_paracentralLobule", ]
    # versions is a list of all versions stored as dictionaries with reference spaces and areas attached IMPORTANT
    versions = [{"DKT31_vol_d": {"reference_space": "fsaverage", "areas": lista, "accessibility": "freeAccess",
                                    "atlasType": "parcellationScheme", "version_identifier": "v1", "version_innovation": "This is the first version of this research product",
                                    "release_date": "2016-01-27", "short_name": "Mars_v1_c", "homepage": "https://meca-brain.org/software/marsatlas/",
                                    "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.1002/hbm.23121", "full_doc_name": "Mars_cortex",
                                    "authors": ["auziasGuillaume", "brovelliAndrea", "coulonOlivier"]}},
                {"DKT31_vol_p": {"reference_space" : "fsaverage", "areas" : lista + listb, "accessibility": "freeAccess",
                                                "atlasType": "parcellationScheme", "version_identifier": "v2", "version_innovation": "This is the second version of this research product",
                                                "release_date": "2017-01-25", "short_name": "Mars_v2_cs", "homepage": "https://meca-brain.org/software/marsatlas-subcortical/",
                                                "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016", "full_doc_name": "Mars_cortexAndSubcortex",
                                                "authors": ["brovelliAndrea", "badierJeanmichael", "boniniFrancesca", "bartolomeiFabrice", "coulonOlivier", "auziasGuillaume"]}},
                {"DKT31_surf": {"reference_space": "fsaverage", "areas": lista + listb, "accessibility": "freeAccess",
                     "atlasType": "parcellationScheme", "version_identifier": "v2",
                     "version_innovation": "This is the second version of this research product",
                     "release_date": "2017-01-25", "short_name": "Mars_v2_cs",
                     "homepage": "https://meca-brain.org/software/marsatlas-subcortical/",
                     "license": "CC BY-NC-ND 3.0",
                     "digitalIdentifier": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016",
                     "full_doc_name": "Mars_cortexAndSubcortex",
                     "authors": ["brovelliAndrea", "badierJeanmichael", "boniniFrancesca", "bartolomeiFabrice",
                                 "coulonOlivier", "auziasGuillaume"]}}]

    return (mars_cortex_authors, mars_cortexAndSubcotex_authors, full_documentation, description, abbreviation, fullName, shortName, homepage, versions)


if __name__ == '__main__':

    region_names_cortex, region_names_subcortex = MarsDataScrape. datascrape()
    mars_cortex_authors, mars_cortexAndSubcotex_authors, full_documentation, description, abbreviation, fullName, shortName, homepage, versions = data_structures(region_names_cortex, region_names_subcortex)