from jsonschema import Draft7Validator
from pathlib import Path

import sys
import json

def main():
    for filename in Path('../examples').glob('*.json'):
        print(filename)


if __name__ == "__main__":
    main()
