# rac_schema_validator

Validators for RAC JSONSchemas.

## Requirements
- Python 3.9 or higher
- [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)
- [tox](https://tox.readthedocs.io/) (for running tests)
- [pre-commit](https://pre-commit.com/) (for running linters before committing)

## Installation

The recommended way to install this package is using `pip`:

```
pip install rac_schema_validator
```

After installing pre-commit, install the git-hook scripts:

```
$ pre-commit install
```

## Usage

This library has one main public method, `is_valid()`, which takes two required
arguments:
- the data to be validated
- the JSONSchema to validate against

and a third optional argument:
- a base schema to resolve references against (see [official docs](https://python-jsonschema.readthedocs.io/en/latest/references/))

```
from rac_schema_validator import is_valid

data = {"key": "value" ... }
schema = { ... }
is_valid(data, schema)
```

Invalid data will raise a `rac_schema_validator.exceptions.ValidationError`, and
an invalid schema will raise a `jsonschema.exceptions.SchemaError`.

#### Tests

`rac_schema_validator` comes with unit tests as well as linting. The easiest way
to make sure all tests pass is to run `tox` from the root of the repository.
This will execute all tests, and will also run `autopep8` and `flake8` linters
against the codebase.

## License

Code is released under an MIT license. See`LICENSE.md`.
