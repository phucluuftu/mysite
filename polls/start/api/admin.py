from django.contrib import admin

from services.models import Question, VoteHistory, Choice

admin.site.register(Question)
admin.site.register(VoteHistory)
admin.site.register(Choice)