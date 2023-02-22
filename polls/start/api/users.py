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
@login_required
@require_http_methods(["POST"])
@parse_params(question_create_schema)
def create_question(request, body):
    user_name = request.user.get_username()
    user = User.objects.get(username=user_name)
    question_created = question_manager.create_question(body, user)
    return api_response_data({
        "question_created": question_created,
    }, SUCCESSFUL)


@csrf_exempt
@login_required
@require_http_methods(["POST"])
@parse_params(vote_schema)
def vote(request, body):
    question = question_manager.get_question_by_id(body['question_id'])
    selected_choice = question_manager.get_choice_set_by_question_id(question, body['choice_id'])
    vote_created_info = question_manager.create_vote_history(question, request.user, selected_choice.choice_text)
    # info = json.loads(serialize('json', [newrecord]))
    return api_response_data({
        "vote_created_info": vote_created_info,
    }, SUCCESSFUL)
