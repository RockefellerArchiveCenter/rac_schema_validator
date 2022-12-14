import re

import jsonschema

from .exceptions import ValidationError


def _is_date(value, instance):
    if not isinstance(instance, str):
        return False
    if instance.count("-") == 2:
        pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    elif instance.count("-") == 1:
        pattern = re.compile("^[0-9]{4}-[0-9]{2}$")
    else:
        pattern = re.compile("^[0-9]{4}$")
    return pattern.match(instance)


def is_valid(data, object_schema, base_schema=None):
    """Main method to validate data against a JSON schema.

    Args:
        data (dict): data to be validated.
        object_schema (dict): schema to validate againsts
        base_schema (dict): base schema against which to resolve object schema (optional)

    Raises:
        TypeError: if data, object_schema or base_schema is not a dict
        rac_schemas.exceptions.ValidationError: if the validation fails
    """
    for arg in [data, object_schema, base_schema]:
        if arg and not isinstance(arg, dict):
            raise TypeError(f"`{arg}` must be a dict, got {type(arg)} instead")

    resolver = jsonschema.RefResolver.from_schema(
        base_schema) if base_schema else None
    type_checker = jsonschema.Draft7Validator.TYPE_CHECKER.redefine(
        "date", _is_date)
    validators = jsonschema.Draft7Validator.VALIDATORS
    validators["date"] = _is_date
    CustomValidator = jsonschema.validators.extend(
        jsonschema.Draft7Validator,
        type_checker=type_checker,
        validators=validators)
    validator = CustomValidator(object_schema, resolver=resolver)
    try:
        validator.check_schema(validator.schema)
        validator.validate(data)
    except jsonschema.exceptions.ValidationError as e:
        raise ValidationError(e)
    return True
