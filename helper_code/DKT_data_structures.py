
def data_structures():
    # atlas info
    DKT_authors = [{"kleinArno" : {"familyName" : "Klein", "givenName" : "Arno", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}},
                   {"tourvilleJason" : {"familyName" : "Tourville", "givenName" : "Jason", "ORCID" : "https://orcid.org/0000-0002-7197-2427"}}]

    full_documentation =  [{"DKT31": "https://www.frontiersin.org/articles/10.3389/fnins.2012.00171/full"}]
    main_documentation = "https://doi.org/10.3389/fnins.2012.00171"
    description = "Mindboggle-101 surface and volume brain atlases (anatomical labels from a population of brains)."
    abbreviation = "DKT"
    fullName = "Desikan-Killiany-Tourville-Atlas"
    shortName = "DKT"
    homepage = "https://osf.io/kgdey/wiki/home/"
    areas = ["temporalLobeMedialAspect_entorhinalCortex", "temporalLobeMedialAspect_parahippocampalGyrus","temporalLobeMedialAspect_fusiformGyrus",
             "temporalLobeLateralAspect_superiorTemporalGyrus", "temporalLobeLateralAspect_middleTemporalGyrus", "temporalLobeLateralAspect_inferiorTemporalGyrus",
             "temporalLobeLateralAspect_transverseTemporalGyrus", "frontalLobe_superiorFrontal", "frontalLobe_middleFrontalGyrusRostral",
             "frontalLobe_middleFrontalGyrusCaudal","frontalLobe_inferiorFrontalGyrusParsOpercularis","frontalLobe_inferiorFrontalGyrusParsOrbitalis",
             "frontalLobe_inferiorFrontalGyrusParsTriangularis","frontalLobe_orbitofrontalGyrus","frontalLobe_lateralDivision","frontalLobe_medialDivision",
             "frontalLobe_precentralGyrus","frontalLobe_paracentralLobule", "parietalLobe_poscentralGyrus", "parietalLobe_supraMarginalGyrus", "parietalLobe_superiorParietalLobule", "parietalLobe_inferiorParietalLobule", "parietalLobe_precuneus",
             "occipitalLobe_lingualGyrus", "occipitalLobe_pericalcarineCortex", "occipitalLobe_cuneusCortex", "occipitalLobe_lateralOccipitalCortex", "cingulateCortex_rostralAnterior", "cingulateCortex_caudalAnterior", "cingulateCortex_posterior", "cingulateCortex_isthmus"]
    areas_surf = [s + "_lH" for s in areas] + [s + "_rH" for s in areas]


    # versions is a list of all versions stored as dictionaries with reference spaces and areas attached IMPORTANT
    versions = [{"DKT_dkt31VolLabels": {"reference_space": "MNI_ICBM_152_2009c_nonlin_asym", "areas": areas,
                                      "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "v1",
                                      "version_innovation": "Joint fusion volume atlas version of the DKT atlas",
                                      "release_date": "2016-07-11", "short_name": "dkt31VolLabels", "homepage": "https://osf.io/kgdey/",
                                      "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                      "full_doc_name": "DKT31_vol_labels", "authors": ["kleinArno", "tourvilleJason"]}},
                {"DKT_dkt31VolProb": {"reference_space" : "MNI_ICBM_152_2009c_nonlin_asym", "areas" : areas,
                                             "accessibility": "freeAccess", "atlasType": "probabilisticAtlas", "version_identifier": "v2",
                                             "version_innovation": "Joint fusion label probabilitiy version of the DKT atlas",
                                             "release_date": "2016-07-11", "short_name": "dkt31VolProb", "homepage": "https://osf.io/kgdey/",
                                             "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                             "full_doc_name": "DKT31_vol_probabilistic", "authors": ["kleinArno", "tourvilleJason"]}},
                {"DKT_dkt31Surf101": {"reference_space": "fsaverage", "areas": areas_surf,
                                            "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "v3",
                                            "version_innovation": "Cortical surface atlas version of the DKT atlas from all 101 participants",
                                            "release_date": "2016-07-11", "short_name": "dkt31Surf101", "homepage": "https://osf.io/kgdey/",
                                            "license": "CC BY-NC-ND 3.0", "digitalIdentifier": " https://doi.org/10.3389/fnins.2012.00171",
                                            "full_doc_name": "DKT31_surf_101subjects", "authors": ["kleinArno", "tourvilleJason"]}},
                {"DKT_dktSurf40": {"reference_space": "fsaverage", "areas": areas_surf,
                                            "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "v4",
                                            "version_innovation": "Cortical surface atlas version of the DKT atlas from 40 participants",
                                            "release_date": "2016-07-11", "short_name": "dktSurf40", "homepage": "https://osf.io/kgdey/",
                                            "license": "CC BY-NC-ND 3.0", "digitalIdentifier": " https://doi.org/10.3389/fnins.2012.00171",
                                            "full_doc_name": "DKT_surf_40sujects", "authors": ["kleinArno", "tourvilleJason"]}}
                ]

    return (DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage,areas, areas_surf, versions)


if __name__ == '__main__':

    DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage,areas, areas_surf, versions = data_structures()