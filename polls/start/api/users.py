from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from common.utils import api_response_data
from common.constants import *
from services.users import user_manager

@login_required
@require_http_methods(["GET"])
def get(request):
        user_name = request.user.get_username()
        user_infos = user_manager.get_infos_json(user_name)
        return api_response_data({
            "user": user_infos,
           # "question": question_infos,
        }, SUCCESSFUL)

@require_http_methods(["POST"])
def create_question(request):
    pass


