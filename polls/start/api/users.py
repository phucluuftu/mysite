from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from common.utils import api_response_data, model_to_dict, to_dict
from common.constants import *

@login_required
@require_http_methods(["GET"])
def get(request):
        user = User.objects.get(username=request.user.get_username())
        print(type(user))
        user_to_dict = to_dict(user)
        # user_to_list = serialize('json', [user])
        return api_response_data({
            "user": user_to_dict,
        }, SUCCESSFUL)

