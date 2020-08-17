from marshmallow import (
    Schema,
    fields,
    validate,
)


class LatestPipelineProductResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    product_name = fields.String(validate=not_blank, required=True)
    latest_catalyst_date = fields.DateTime()
    updated_at = fields.DateTime()
