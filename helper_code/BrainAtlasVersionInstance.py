# ______________________________________________________________________#
# brain atlas versions created by hand first


# ______________________________________________________________________#
# brain tlas versions info created automatically (needs to be integrated into the by hand created#

# data

atlas_version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/freeAccess"
atlas_type_https = "https://openminds.ebrains.eu/instances/atlasType/deterministicAtlas"
coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"

coordinate_spaces = ["Collin27_1998", "HipHop138"]

abbreviation = "Mars"



#brain atlas versions

# schema creation brain atlas version
marsAtlas = atlas.add_SANDS_brainAtlasVersion(coordinateSpace= {"@id": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-asym"})


marsAtlasPlusSubcortical = atlas.add_SANDS_brainAtlasVersion(fullName="MarsAtlas + subcortical",coordinateSpace=,versionInnovation=, \
                                       releaseDate=, hasTerminology= , shortName= , versionIdentifier=  )

