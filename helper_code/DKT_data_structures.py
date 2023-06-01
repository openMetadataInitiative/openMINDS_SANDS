
def data_structures():
    # Brain Area Info for each version (can be the same) THIS NEEDS TO BE SAME LENGTH FOR ALL AREAS
    areas_children = ['caudalAnteriorCingulate', 'caudalMiddleFrontal', 'cuneus', 'entorhinal', 'fusiform',
                      'inferiorParietal', 'inferiorTemporal', 'isthmusCingulate', 'lateralOccipital',
                      'lateralOrbitofrontal', 'lingual', 'medialOrbitofrontal', 'middleTemporal', 'parahippocampal',
                      'paracentral', 'parsOpercularis', 'parsOrbitalis', 'parsTriangularis', 'pericalcarine',
                      'postcentral', 'posteriorCingulate', 'precentral', 'precuneus', 'rostralAnteriorCingulate',
                      'rostralMiddleFrontal', 'superiorFrontal', 'superiorParietal', 'superiorTemporal',
                      'supramarginal', 'transverseTemporal', 'insula']
    areas_1st_parent = ['cingulateCortex', 'frontalLobe', 'occipitalLobe', 'medialTemporalLobe', 'medialTemporalLobe',
                        'parietalLobe', 'lateralTemporalLobe', 'cingulateCortex', 'occipitalLobe', 'frontalLobe',
                        'occipitalLobe', 'frontalLobe', 'lateralTemporalLobe', 'medialTemporalLobe', 'frontalLobe',
                        "frontalLobe", 'frontalLobe', 'frontalLobe', 'occipitalLobe', 'parietalLobe', 'cingulateCortex',
                        "frontalLobe", 'parietalLobe', 'cingulateCortex', 'frontalLobe', 'frontalLobe', 'parietalLobe',
                        'lateralTemporalLobe', 'parietalLobe', 'lateralTemporalLobe', None]
    # areas = {outer_key: {outer_value: areas_2ndParent[0]} for outer_key, outer_value in areas_parent_matched.items()}
    areas_2nd_parent = ['brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                        'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                        "brain", 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', None]

    # zip list to store as tuples
    areas = list(zip(areas_children, areas_1st_parent, areas_2nd_parent))

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

    # Data Structures for all VERSIONS (BAVs, PEVs)
    # version info
    versions = [{"DKTA_p101-MNI152": {"reference_space": "MNI_ICBM_152_2009c_nonlin_asym",
                                      "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "101 participants, MNI",
                                      "version_innovation": "Joint fusion volume atlas version of the DKT atlas",
                                      "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                      "license": "ccByNcNd3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                      "full_doc_name": "DKTA_p101-MNI152", "authors": ["kleinArno", "tourvilleJason"], "altVersion": ["DKTA_p101-fsaverage"],
                                      "criteriaQualityType": ["asserted"], "annotationCriteriaType": ["deterministicAnnotation", "probabalisticAnnotation"],
                                      "laterality": ["left", "right"], "annotationType": "annotationMask"}},
                {"DKTA_p101-fsaverage": {"reference_space" : "fsaverage-5",
                                             "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "101 participants, fsaverage",
                                             "version_innovation": "Cortical surface atlas version of the DKT atlas derived from 101 participants",
                                             "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                             "license":"ccByNcNd3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                             "full_doc_name": "DKTA_p101-fsaverage", "authors": ["kleinArno", "tourvilleJason"], "altVersion": ["DKTA_p101-MNI152"], "newVersion": ["DKTA_p40-fsaverage"],
                                             "criteriaQualityType": ["asserted"], "annotationCriteriaType": ["deterministicAnnotation"],
                                             "laterality": ["left", "right"], "annotationType": "annotationSurface"}},
                {"DKTA_p40-fsaverage": {"reference_space": "fsaverage-5",
                                            "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "40 participants, fsaverage",
                                            "version_innovation": "Cortical surface atlas version of the DKT atlas from 40 participants",
                                            "release_date": "2016-07-11", "short_name": "DKT Atlas", "homepage": "https://osf.io/kgdey/",
                                            "license": "ccByNcNd3.0", "digitalIdentifier": "https://doi.org/10.3389/fnins.2012.00171",
                                            "full_doc_name": "DKTA_p40-fsaverage", "authors": ["kleinArno", "tourvilleJason"],
                                            "criteriaQualityType": ["asserted"], "annotationCriteriaType": ["deterministicAnnotation"],
                                            "laterality": ["left", "right"], "annotationType": "annotationSurface"}}
                ]

    # area for each version for BAVs and PE
    areas_versions_hierachry = {"DKTA_p101-MNI152": areas, "DKTA_p101-fsaverage": areas, "DKTA_p40-fsaverage": areas}

    # unique areas for BA
    areas_unique = set()
    for value_list in areas_versions_hierachry.values():
        for tuple_value in value_list:
            first_entry = tuple_value[0]
            areas_unique.add(first_entry)

    # unique parents
    parents_unique = set()
    for value_list in areas_versions_hierachry.values():
        for tuple_value in value_list:
            parents_unique.update(tuple_value[1:])

    return (DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique)


if __name__ == '__main__':
    DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = data_structures()