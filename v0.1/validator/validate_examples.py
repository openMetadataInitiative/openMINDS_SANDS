from jsonschema import Draft7Validator
from pathlib import Path

import sys
import json

def main():
    for filename in Path('../examples').glob('*.json'):
        with open(filename,'r') as f:
            # find schema in @context
            data = json.load(f)
            print(data["@context"])
            # validate against schema


if __name__ == "__main__":
    main()
