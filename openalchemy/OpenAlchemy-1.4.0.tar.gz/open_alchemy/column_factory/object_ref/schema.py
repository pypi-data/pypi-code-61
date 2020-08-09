"""Calculate the array schema from the artifacts."""

from open_alchemy import types


def calculate(*, artifacts: types.ObjectArtifacts) -> types.ObjectRefSchema:
    """
    Calculate the array schema from the artifacts.

    Args:
        artifacts: The artifactsfor the array reference.

    Returns:
        The schema for the array to store with the model.

    """
    schema: types.ObjectRefSchema = {
        "type": "object",
        "x-de-$ref": artifacts.relationship.model_name,
    }
    if artifacts.nullable is not None:
        schema["nullable"] = artifacts.nullable
    if artifacts.description is not None:
        schema["description"] = artifacts.description
    if artifacts.write_only is not None:
        schema["writeOnly"] = artifacts.write_only
    return schema
