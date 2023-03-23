# ______________________________________________________________________#
# brain atlas versions created by hand first


# ______________________________________________________________________#
# brain tlas versions info created automatically (needs to be integrated into the by hand created#


# hasterminology schemas, parcellation terminology version, needs to be initiated with the hasENtity linking all paercalation entity versions

# data
atlas_version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
atlas_type_https = "https://openminds.ebrains.eu/instances/atlasType/deterministicAtlas"
coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"

# accessibility schemas
accessibility = "freeAccess"
accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/freeAccess"

# coordinate space schamas..do not create HipHop 138, talk to Lyuba about it
coordinate_spaces = ["Collin27_1998", "HipHop138"]

# non schema data
short_name = ["Collin27_1998_cortexAndSubcortex", "HipHop138_cortex"]
version_identifier = "v1"
version_innovation = "This is the first version of this research product"
atlas_type = "deterministic"
release_dates = ["2016-01-27", "2017-01-25"]


# dataset schemas


#brain atlas versions


entities = []
# schema creation brain atlas version
marsAtlas = atlas.add_SANDS_brainAtlasVersion(coordinateSpace= {"@id": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-asym"})


marsAtlasPlusSubcortical = atlas.add_SANDS_brainAtlasVersion(fullName="MarsAtlas + subcortical",coordinateSpace=,versionInnovation=, \
                                       releaseDate=, hasTerminology= , shortName= , versionIdentifier=  )

