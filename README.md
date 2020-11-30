# openMINDS_SANDS

The openMINDS_SANDS repository is part of the **open** **M**etadata **I**nitiative for **N**euroscience **D**ata **S**tructures (openMINDS). It contains the 
schema-templates used for **S**patial **A**nchoring of **N**euroscience **D**ata (SANDS) metadata model.

For more information on openMINDS in general, please go to the main repository: https://github.com/HumanBrainProject/openMINDS

## schemas
The SANDS v1 schemas are JSON-schema inspired schema-templates with a few custom template-properties (prefixed with `"_"`) which allow us to simplify their readability and increase their reusability.

## tests
In **tests** you can find JSON-LDs designed to test the validation behaviour of each schema. JSON-LDs that should fail the validation are identifiable via a "-nok" suffix in the file name.

## examples
In **examples** you will find several possible serializations of the openMINDS_SANDS metadata model. The scope of each example is described in it's README. The correspondingly generated JSON-LDs may be further structured (e.g., grouped according to the schema they are validated against).

## How to contribute
Please check our [contribution document](./CONTRIBUTING.md).

## License
This work is licensed under the MIT License.
