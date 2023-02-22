import random
from datetime import datetime
from django.utils import timezone
from common.constants import CURRENT_TIME
from services.models import Question, VoteHistory
from common.utils import objects_to_json

def create_question(body, user):
    question_created = Question.objects.create(
        question_text=body['question_text'],
        pub_date=CURRENT_TIME,
        expire_date=timezone.make_aware(datetime.strptime(body['expire_date'], '%Y-%m-%d %H:%M:%S')),
        status=True,
        user_created=user,
        type=body['type'],
        pass_code=random.randint(100000, 999999)
    )
    choices_list = body['choice']
    for choice in choices_list:
        question_created.choice_set.create(choice_text=choice, votes=0)
    return question_created.as_json()


def get_question_by_id(id):
    return Question.objects.get(id=id)


def get_choice_set_by_question_id(question, id):
    return question.choice_set.get(id=id)


def create_vote_history(question, user_voted, choice_text):
    result = VoteHistory.objects.create(
        question=question,
        user_voted=user_voted,
        choice_text=choice_text)
    return result.as_json()


def get_active_public_question():
    results = Question.objects.filter(status=True, type=1).order_by('pub_date')
    return objects_to_json(results)


def search_question_by_text(query):
    results = Question.objects.filter(question_text__icontains=query)
    return objects_to_json(results)

def get_vote_info(question):
    results = VoteHistory.objects.filter(question=question)
    return objects_to_json(results)
