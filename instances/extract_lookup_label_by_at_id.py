import glob
import json
import os
types = ["https://openminds.ebrains.eu/sands/ParcellationEntity", "https://openminds.ebrains.eu/sands/ParcellationEntityVersion"]

for instance_source in glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), f'**/*.jsonld'), recursive=True):
    with open(instance_source) as source_file:
        payload = json.load(source_file)
    if payload["@type"] in types:
        at_id = payload["@id"]
        shortened_at_id = os.path.basename(at_id)
        payload["lookupLabel"] = shortened_at_id
        with open(instance_source, "w") as target_file:
            target_file.write(json.dumps(payload, indent=4, sort_keys=True))