from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from common.utils import api_response_data
from common.constants import *
from services.users import user_manager
from services.questions import question_manager
from django.views.decorators.csrf import csrf_exempt
from .schema import *
from common.decorator import *


@login_required
@require_http_methods(["GET"])
def get(request):
    user_name = request.user.get_username()
    user_infos = user_manager.get_infos_json(user_name)
    return api_response_data({
        "user": user_infos,
        # "question": question_infos,
    }, SUCCESSFUL)


@csrf_exempt
@require_http_methods(["POST"])
@parse_params(question_create_schema)
def create_question(request, body):
    if request.user is None:
        return api_response_data({
        "error": "not loggin",
        })
    else:
        user_name = request.user.get_username()
        user = User.objects.get(username=user_name)
        print(body)
        print(user)
        a = question_manager.create_question(body, user)
        print(a)
        return api_response_data({
            "question": "create_question(body, user)",
        }, SUCCESSFUL)
