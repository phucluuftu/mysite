import random
from datetime import datetime
from django.utils import timezone
from common.constants import CURRENT_TIME
from services.models import Question


def create_question(body, user):
    result = Question.objects.create(
        question_text=body['question_text'],
        pub_date=CURRENT_TIME,
        expire_date=timezone.make_aware(datetime.strptime(body['expire_date'], '%Y-%m-%d %H:%M:%S')),
        status=True,
        user_created=user,
        type=body['type'],
        pass_code=random.randint(100000, 999999)
    )
    return result.as_json()
