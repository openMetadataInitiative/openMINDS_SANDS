import os
import json

input_dir = 'instances/atlas/parcellationEntityVersion/JBA-v2-9'
output_dir = 'instances/atlas/parcellationEntity/JBA'

def main():
    existing_dict = {}

    def get_existing(pev_filename: str):
        jba_version, space, areaname, version, hemisphere = pev_filename.split('_')
        if areaname not in existing_dict:
            with open(f'{output_dir}/JBA_{areaname}.jsonld', 'r') as fp:
                existing_dict[areaname] = json.load(fp)
        return existing_dict[areaname]

    input_files = os.listdir(input_dir)
    output_files = os.listdir(output_dir)

    for file in input_files:
        with open(f'{input_dir}/{file}', 'r') as fp:
            id = json.load(fp).get('@id')
        out = get_existing(file)
        has_version = out.get('hasVersion') or []
        out['hasVersion'] = [
            *has_version,
            { '@id': id }]
    for key, value in existing_dict.items():
        with open(f'{output_dir}/JBA_{key}.jsonld', 'w') as fp:
            json.dump(value, fp=fp, indent=4)
            fp.write('\n')
    

if __name__ == "__main__":
    main()