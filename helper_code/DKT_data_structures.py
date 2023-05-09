
def data_structures():
    # atlas info
    DKT_authors = [{"kleinArno" : {"familyName" : "Klein", "givenName" : "Arno", "ORCID" : "https://orcid.org/0000-0002-0414-5691"}},
                   {"tourvilleJason" : {"familyName" : "Tourville", "givenName" : "Jason", "ORCID" : "https://orcid.org/0000-0002-7197-2427"}}]

    full_documentation =  [{"DKT": "https://doi.org/10.3389/fnins.2012.00171"}]
    main_documentation = "https://doi.org/10.3389/fnins.2012.00171"
    description = "Mindboggle-101 surface and volume brain atlases (anatomical labels from a population of brains)."
    abbreviation = "DKTA"
    fullName = "Desikan-Killiany-Tourville Atlas"
    shortName = "DKT Atlas"
    homepage = "https://osf.io/kgdey/wiki/home/"

    # Data Structures for PEs
    # areas = ["caudalAnteriorCingulate", "caudalMiddleFrontal","cuneus",
    #          "entorhinal", "fusiform", "inferiorParietal",
    #          "inferiorTemporal", "isthmusCingulate", "lateralOccipital",
    #          "lateralOrbitofrontal","lingual","medialOrbitofrontal",
    #          "middleTemporal","parahippocampal","paracentral","parsOpercularis",
    #          "parsOrbitalis","parsTriangularis", "pericalcarine", "postcentral", "posteriorCingulate", "precentral", "precuneus",
    #          "rostralAnteriorCingulate", "rostralMiddleFrontal", "superiorFrontal", "superiorParietal", "superiorTemporal", "supramarginal", "transverseTemporal", "insula"]

    areas_1stParent = ["medialTemporalLobe", "lateralTemporalLobe", "frontalLobe", "parietalLobe", "occipitalLobe", "cingulateCortex"]
    areas_2ndParent = ["brain"]
    areas_parent_matched = {"caudalAnteriorCingulate": "cingulateCortex", "caudalMiddleFrontal": "frontalLobe", "cuneus": "occipitalLobe",
             "entorhinal": "medialTemporalLobe", "fusiform": "medialTemporalLobe", "inferiorParietal": "parietalLobe",
             "inferiorTemporal": "lateralTemporalLobe", "isthmusCingulate": "cingulateCortex", "lateralOccipital": "occipitalLobe",
             "lateralOrbitofrontal": "frontalLobe", "lingual": "occipitalLobe", "medialOrbitofrontal": "frontalLobe",
             "middleTemporal": "lateralTemporalLobe" ,"parahippocampal": "medialTemporalLobe","paracentral": "frontalLobe", "parsOpercularis": "frontalLobe",
             "parsOrbitalis": "frontalLobe", "parsTriangularis": "frontalLobe", "pericalcarine": "occipitalLobe", "postcentral": "parietalLobe", "posteriorCingulate": "cingulateCortex", "precentral": "frontalLobe", "precuneus": "parietalLobe",
             "rostralAnteriorCingulate": "cingulateCortex", "rostralMiddleFrontal": "frontalLobe", "superiorFrontal": "frontalLobe", "superiorParietal": "parietalLobe", "superiorTemporal": "lateralTemporalLobe", "supramarginal": "parietalLobe", "transverseTemporal": "lateralTemporalLobe", "insula": None}
    areas = {outer_key: {outer_value: areas_2ndParent[0]} for outer_key, outer_value in areas_parent_matched.items()}

 # Data Structures for all VERSIONS (BAVs, PEVs)

        # probabilistic Atlas, determinstic atlas
    # versions is a list of all versions stored as dictionaries with reference spaces and areas attached IMPORTANT
    versions = [{"DKTA_p101-MNI152": {"reference_space": "MNI_ICBM_152_2009c_nonlin_asym", "areas": areas,
                                      "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "101 participants, MNI",
                                      "version_innovation": "Joint fusion volume atlas version of the DKT atlas",
                                      "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                      "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                      "full_doc_name": "DKTA_p101-MNI152", "authors": ["kleinArno", "tourvilleJason"], "altVersion": ["DKTA_p101-fsaverage"]}},
                {"DKTA_p101-fsaverage": {"reference_space" : "MNI_ICBM_152_2009c_nonlin_asym", "areas" : areas,
                                             "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "101 participants, fsaverage",
                                             "version_innovation": "Cortical surface atlas version of the DKT atlas derived from 101 participants",
                                             "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                             "license":"CC BY-NC-ND 3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                             "full_doc_name": "DKTA_p101-fsaverage", "authors": ["kleinArno", "tourvilleJason"], "altVersion": ["DKTA_p101-MNI152"], "newVersion": ["DKTA_p40-fsaverage"]}},
                {"DKTA_p40-fsaverage": {"reference_space": "fsaverage_5", "areas": areas,
                                            "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "40 participants, fsaverage",
                                            "version_innovation": "Cortical surface atlas version of the DKT atlas from 40 participants",
                                            "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                            "license": "CC BY-NC-ND 3.0", "digitalIdentifier": " https://doi.org/10.3389/fnins.2012.00171",
                                            "full_doc_name": "DKTA_p40-fsaverage", "authors": ["kleinArno", "tourvilleJason"]}},
                ]

    return (DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, areas, versions)


if __name__ == '__main__':

    DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage,areas, versions = data_structures()