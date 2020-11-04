#   Copyright (c) 2018, EPFL/Human Brain Project PCO
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import json
import os
import glob

import jsonschema
from jsonschema import Draft7Validator, ValidationError


def _get_schema(schema):
    root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "target/")
    root_schema_path = os.path.join(root_path, schema)
    with open(root_schema_path, 'r') as root_schema_file:
        root_schema = json.load(root_schema_file)
    Draft7Validator.check_schema(root_schema)
    return root_schema


def test_examples():
    for examples_path in glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), '**/examples'), recursive=True):
        version_nr = os.path.basename(os.path.dirname(examples_path))
        for example_path in glob.glob(os.path.join(examples_path, '**/*.json'), recursive=True):
            schema_name = f"{os.path.basename(example_path).split('-')[0]}.schema.json"
            schema = _get_schema(f"{version_nr}/jsonschema/{schema_name}")
            with open(example_path, 'r') as example_file:
                example = json.load(example_file)
            if os.path.basename(example_path).endswith("-nok.json"):
                try:
                    jsonschema.validate(example, schema)
                    raise AssertionError(f"Was expecting a validation error for {os.path.basename(example_path)}")
                except ValidationError:
                    print(f"Validation failed as expected for {os.path.basename(example_path)}")
            else:
                jsonschema.validate(example, schema)
