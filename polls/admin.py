from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', )

admin.site.register(Question, QuestionAdmin)