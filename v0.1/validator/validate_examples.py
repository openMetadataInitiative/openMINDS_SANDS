from jsonschema import validate
from pathlib import Path

import sys
import json

def main():
    for filename in Path('../examples').glob('*.json'):
        with open(filename,'r') as f:
            # load example
            data = json.load(f)
            # validate against schema
            with open(data["@context"], 'r') as schemaFile:
                #print(json.load(schemaFile))
                validate(instance=data, schema=json.load(schemaFile))

if __name__ == "__main__":
    main()
