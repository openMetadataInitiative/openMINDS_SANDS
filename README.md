<a href="https://github.com/HumanBrainProject/openMINDS_SANDS/blob/v1/img/openMINDS_SANDS_logo.png">
    <img src="https://github.com/HumanBrainProject/openMINDS_SANDS/blob/v3/img/light_openMINDS-SANDS-logo.png" alt="openMINDS SANDS logo" title="openMINDS SANDS" align="right" height="70" />
</a>

# openMINDS_SANDS

The openMINDS_SANDS repository is part of the **open** **M**etadata **I**nitiative for **N**euroscience **D**ata **S**tructures (openMINDS). It contains the 
schema-templates used for **S**patial **A**nchoring of **N**euroscience **D**ata (SANDS) metadata model.

The major versions are developed and maintained in different version-branches. The default branch is always the latest version-branch. **Each version can be accessed by checking out the corresponding version-branch.** This README describes the version-branch v3. 

**NOTE: this is an unreleased development branch and not yet fully functional**

For more information on openMINDS in general, please go to the main repository: https://github.com/HumanBrainProject/openMINDS

## schemas
The SANDS schemas are defined as JSON-schema inspired templates with only a few customized technical properties (prefixed with `"_"`). These simplified schema-templates are easy to read and can be robustly translated to other, well known target formats (e.g., HTML, JSON-schema, etc.). 

## tests
In **tests** you can find JSON-LDs designed to test the validation behaviour of each schema. They follow the naming convention `{schema_name}-{custom_test_name}.jsonld`. For test cases supposed to fail the validation, the suffix **`-nok`** should be attached (`{schema_name}-{custom_test_name}-nok.jsonld`). The tests are validated every time a change is introduced and therefore are ensuring the correct behavior of the schemas.

## examples
In **examples** you will find several possible serializations of the openMINDS_SANDS metadata model. The scope of each example is described in it's README. The correspondingly generated JSON-LDs may be further structured (e.g., grouped according to the schema they are validated against).

## How to contribute
Please check our [contribution document](./CONTRIBUTING.md).

## License
This work is licensed under the MIT License.

**Logo:** The openMINDS logo was created by U. Schlegel, based on an original sketch by C. Hagen Blixhavn and feedback by L. Zehl.
