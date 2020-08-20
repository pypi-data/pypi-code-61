from jsonschema import Draft7Validator
from jsonschema import validators


def extend_with_default(validator_class):
    '''copy from jsonschema docs'''

    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(
            validator, properties, instance, schema,
        ):
            yield error

    return validators.extend(
        validator_class, {"properties" : set_defaults},
    )

JSONSchema = extend_with_default(Draft7Validator)


class NullRefResolver:

    def push_scope(self, _):
        pass

    def pop_scope(self):
        pass

    def resolve(self, _):
        raise NotImplementedError('should not be called')

null_ref_resolver = NullRefResolver()


def create(schema):
    return JSONSchema(schema, resolver=null_ref_resolver)
