from django import http
from .constants import *
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.related import ManyToManyField
from itertools import chain


def to_json(data, ensure_ascii=False, ensure_bytes=False, default=None):
    result = json.dumps(data, ensure_ascii=ensure_ascii, separators=(',', ':'), default=default)
    if ensure_bytes and isinstance(result, str):
        result = result.encode('utf-8')
    return result


def api_response_data(data, status=FAIL):
    if status == SUCCESSFUL:
        data = {
            'status': SUCCESSFUL,
            'payload': data
        }
    else:
        data['status'] = FAIL
    return http.HttpResponse(to_json(data), content_type='application/json; charset=utf-8')


def model_to_dict(instance):
    """
    Convert Django model object to dictionary
    """
    if not instance:
        return {}
    return json.loads(json.dumps(instance.__dict__, cls=DjangoJSONEncoder))


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data

