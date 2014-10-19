from django.contrib import admin
from myapp.models import PollsChoice,PollsQuestion

admin.site.register(PollsChoice)
admin.site.register(PollsQuestion)
