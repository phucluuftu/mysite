from jsonschema import Draft202012Validator
import json
from functools import wraps
from django.views import defaults


def response_http_404(request):
    return defaults.page_not_found(request, '')


def parse_params(schema, error_handler=response_http_404):
    def _parse_params(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            body = json.loads(request.body.decode("utf-8"))
            draft_202012_validator = Draft202012Validator(schema)
            if draft_202012_validator.is_valid(body):
                return func(request, body, *args, **kwargs)
            else:
                return error_handler(request)
        return wrapper
    return _parse_params