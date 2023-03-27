# nice for generator and any() practice

# loop over ORCIDS and create instances
orcid_https = "https://orcid.org/"
for filename in os.listdir(directory_digitalIdentifier_ORCID):
    if os.path.isfile(os.path.join(directory_digitalIdentifier_ORCID, filename)):
        # strip the ORCID name from the filename
        stripped_orcid = os.path.basename(filename).split("_")[-1].replace(".jsonld", "")
        # area = str.replace(stripped_filename, "Mars_", "")
        # create ORCID  instances
        if any(stripped_orcid in s for s in ORCIDs_mars):
            orcid = basic.add_core_ORCID(identifier=orcid_https+stripped_orcid)
        elif any(stripped_orcid in s for s in ORCIDs_subcortex):
            orcid = basic.add_core_ORCID(identifier=orcid_https + stripped_orcid)