from django.contrib import admin
from .models import Answer, Department, Question, Upvote, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("college_email", "type")


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "user")


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "text", "user")


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Upvote)
admin.site.register(Department)
