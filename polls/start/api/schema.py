from jsonschema import validate

question_schema = {
    "type": "object",
    "properties": {
        "question_text": {"type": "string"},
        "expire_date": {"type": "string"},
        "status": {"type": "boolean"},
        "type": {"type": "number"},
    },
    "required": ["question_text", "expire_date", "status", "type"],
    "additionalProperties": False
}