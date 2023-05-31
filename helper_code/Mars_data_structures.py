def data_structures():
    # Brain Area Info for each version (can be the same) THIS NEEDS TO BE SAME LENGTH FOR ALL AREAS
    areas_children_c = ['caudalMedialVisualCortex', 'lateralVisualCortex', 'superiorVisualCortex', 'cuneus',
                        'rostralMedialVisualCortex', 'medialInferiorTemporalCortex', 'rostralInferiorTemporalCortex',
                        'caudalMiddleTemporalCortex', 'caudalSuperiorTemporalCortex', 'rostralSuperiorTemporalCortex',
                        'rostralMiddleTemporalCortex', 'ventralInferiorParietalCortex', 'dorsalInferiorParietalCortex',
                        'superiorParietalCortex', 'medialSuperiorParietalCortex', 'medialParietalCortex',
                        'ventralSomatosensoryCortex', 'dorsolateralSomatosensoryCortex',
                        'dorsomedialSomatosensoryCortex', 'isthmusCingulateCortex', 'posteriorCingulateCortex',
                        'midCingulateCortex', 'anteriorCingulateCortex', 'ventralMotorCortex',
                        'dorsolateralMotorCortex',
                        'dorsomedialMotorCortex', 'rostralVentralPremotorCortex', 'dorsolateralPremotorCortex',
                        'dorsomedialPremotorCortex', 'caudalDorsolateralPrefrontalCortex',
                        'caudalDorsomedialPrefrontalCortex', "rostralVentrolateralPrefrontalCortex",
                        "rostralDorsolateralInferiorPrefrontalCortex",
                        "rostralDorsolateralSuperiorPrefrontalCortex", "rostralDorsalPrefrontalCortex",
                        "rostralMedialPrefrontalCortex",
                        "ventrolateralOrbitoFrontalCortex", "ventralOrbitoFrontalCortex",
                        "ventromedialOrbitoFrontalCortex",
                        "ventromedialPrefrontalCortex", "insularCortex"]
    areas_1st_parent_c = ['occipital', 'occipital', 'occipital', 'occipital', 'occipital', 'temporal', 'temporal',
                          'temporal',
                          'temporal', 'temporal', 'temporal', 'parietal', 'parietal', 'parietal', 'parietal',
                          'parietal',
                          'parietal', 'parietal', 'parietal', 'cingular', 'cingular', 'cingular', 'cingular', 'frontal',
                          'frontal', 'frontal', 'frontal', 'frontal', 'frontal', 'frontal', "frontal", "frontal",
                          "frontal",
                          "frontal", "frontal", "frontal", "orbitoFrontal", "orbitoFrontal", "orbitoFrontal",
                          "orbitoFrontal", "insula"]
    # areas = {outer_key: {outer_value: areas_2ndParent[0]} for outer_key, outer_value in areas_parent_matched.items()}
    areas_2nd_parent_c = ['brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                          'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                          'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                          'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                          "brain"]

    areas_children_cs = ['caudalMedialVisualCortex', 'lateralVisualCortex', 'superiorVisualCortex', 'cuneus',
                         'rostralMedialVisualCortex',
                         'medialInferiorTemporalCortex', 'rostralInferiorTemporalCortex', 'caudalMiddleTemporalCortex',
                         'caudalSuperiorTemporalCortex',
                         'rostralSuperiorTemporalCortex', 'rostralMiddleTemporalCortex',
                         'ventralInferiorParietalCortex',
                         'dorsalInferiorParietalCortex',
                         'superiorParietalCortex', 'medialSuperiorParietalCortex', 'medialParietalCortex',
                         'ventralSomatosensoryCortex',
                         'dorsolateralSomatosensoryCortex', 'dorsomedialSomatosensoryCortex', 'isthmusCingulateCortex',
                         'posteriorCingulateCortex',
                         'midCingulateCortex', 'anteriorCingulateCortex', 'ventralMotorCortex',
                         'dorsolateralMotorCortex', 'dorsomedialMotorCortex',
                         'rostralVentralPremotorCortex', 'dorsolateralPremotorCortex', 'dorsomedialPremotorCortex',
                         'caudalDorsolateralPrefrontalCortex',
                         'caudalDorsomedialPrefrontalCortex', "rostralVentrolateralPrefrontalCortex",
                         "rostralDorsolateralInferiorPrefrontalCortex",
                         "rostralDorsolateralSuperiorPrefrontalCortex", "rostralDorsalPrefrontalCortex",
                         "rostralMedialPrefrontalCortex",
                         "ventrolateralOrbitoFrontalCortex", "ventralOrbitoFrontalCortex",
                         "ventromedialOrbitoFrontalCortex",
                         "ventromedialPrefrontalCortex", "insularCortex", "thalamus", "caudate", "putamen", "pallidum",
                         "hippocampus", "amygdala", "accumbens"]

    areas_1st_parent_cs = ['occipital', 'occipital', 'occipital', 'occipital', 'occipital', 'temporal', 'temporal',
                           'temporal',
                           'temporal', 'temporal', 'temporal', 'parietal', 'parietal', 'parietal', 'parietal',
                           'parietal',
                           'parietal', 'parietal', 'parietal', 'cingular', 'cingular', 'cingular', 'cingular',
                           'frontal',
                           'frontal', 'frontal', 'frontal', 'frontal', 'frontal', 'frontal', "frontal", "frontal",
                           "frontal",
                           "frontal", "frontal", "frontal", "orbitoFrontal", "orbitoFrontal", "orbitoFrontal",
                           "orbitoFrontal", "insula", "subcortex", "subcortex", "subcortex", "subcortex", "subcortex",
                           "subcortex", "subcortex"]
    # areas = {outer_key: {outer_value: areas_2ndParent[0]} for outer_key, outer_value in areas_parent_matched.items()}
    areas_2nd_parent_cs = ['brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                           'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                           'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                           'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                           "brain", 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain']
    # zip list to store as tuples
    areas_c = list(zip(areas_children_c, areas_1st_parent_c, areas_2nd_parent_c))
    areas_cs = list(zip(areas_children_cs, areas_1st_parent_cs, areas_2nd_parent_cs))
    # area for each version for BAVs and PE
    areas_versions_hierachry = {"Mars_c": areas_c, "Mars_cs": areas_cs}

    # atlas info
    mars_authors_unique = [{"auziasGuillaume": {"familyName": "Auzias", "givenName": "Guillaume",
                                                "ORCID": "https://orcid.org/0000-0002-0414-5691"}},
                           {"brovelliAndrea": {"familyName": "Brovelli", "givenName": "Andrea",
                                               "ORCID": "https://orcid.org/0000-0002-5342-1330"}},
                           {"coulonOlivier": {"familyName": "Coulon", "givenName": "Olivier",
                                              "ORCID": "https://orcid.org/0000-0003-4752-1228"}},
                           {"badierJeanmichael": {"familyName": "Badier", "givenName": "Jean-Michael",
                                                  "ORCID": "https://orcid.org/0000-0002-7272-6455"}},
                           {"boniniFrancesca": {"familyName": "Bonini", "givenName": "Francesca",
                                                "ORCID": None}},
                           {"bartolomeiFabrice": {"familyName": "Bartolomei", "givenName": "Fabrice",
                                                  "ORCID": None}}]

    full_documentation = [{"Mars_c": "https://doi.org/10.1002/hbm.23121"},
                          {"Mars_cs": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016"}]
    main_documentation = "https://doi.org/10.1002/hbm.23121"
    description = "MarsAtlas is a model of cortical parcellation. It can be applied to any cortical surface via the " \
                  "HipHop parameterization pipeline, available in the BrainVisa Cortical Surface Toolbox, under the Anatomy category."
    abbreviation = "Mars"
    fullName = "MarsAtlas"
    shortName = "Mars"
    homepage = "https://meca-brain.org/software/marsatlas/"

    # Data Structures for all VERSIONS (BAVs, PEVs)
    # version info
    versions = [{"Mars_c": {"reference_space": "Mars_HipHop138",
                            "accessibility": "freeAccess", "atlasType": "parcellationScheme",
                            "version_identifier": "Mars Cortex, Mars_HipHop138 template",
                            "version_innovation": "Mars Cortex Atlas",
                            "release_date": "2016-01-27", "short_name": "Mars_c",
                            "homepage": "https://meca-brain.org/software/marsatlas/",
                            "license": "cEcILL-B", "digitalIdentifier": "https://doi.org/10.1002/hbm.23121",
                            "full_doc_name": "Mars_cortex",
                            "authors": ["auziasGuillaume", "brovelliAndrea", "coulonOlivier"],
                            "altVersion": ["Mars_cs"],
                            "criteriaQualityType": ["processive"],
                            "annotationCriteriaType": ["deterministicAnnotation"],
                            "laterality": ["left", "right"], "annotationType": "annotationSurface"}},
                {"Mars_cs": {"reference_space": "Colin27_1998",
                             "accessibility": "freeAccess", "atlasType": "parcellationScheme",
                             "version_identifier": "Mars Cortex + Subcortex, Colin27",
                             "version_innovation": "Mars Cortex + Subcortex Atlas",
                             "release_date": "2017-01-25", "short_name": "Mars_cs",
                             "homepage": "https://meca-brain.org/software/marsatlas-subcortical/",
                             "license": "cEcILL-B",
                             "digitalIdentifier": "https://doi.org/10.1523/JNEUROSCI.1672-16.2016",
                             "full_doc_name": "Mars_cortexAndSubcortex",
                             "authors": ["brovelliAndrea", "badierJeanmichael", "boniniFrancesca", "bartolomeiFabrice",
                                         "coulonOlivier", "auziasGuillaume"],
                             "altVersion": ["Mars_c"], "newVersion": [], "criteriaQualityType": ["processive"],
                             "annotationCriteriaType": ["deterministicAnnotation"],
                             "laterality": ["left", "right"], "annotationType": "annotationSurface"}},
                ]

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

    return (mars_authors_unique, full_documentation, main_documentation, description, abbreviation, fullName,
            shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique)


if __name__ == '__main__':
    mars_authors_unique, full_documentation, main_documentation, description, abbreviation, fullName, shortName, \
        homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = data_structures()
