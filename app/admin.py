from django.contrib import admin
from .models import TeacherDepartment, Answer, Question, QuestionDepartment, QuestionRequestedTeacher, Upvote, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('college_email', 'type')


class QuestionAdmin(admin.ModelAdmin):
    list_display=('text', 'user')


class AnswerAdmin(admin.ModelAdmin):
    list_display=('question', 'text', 'user')


class QuestionDepartmentAdmin(admin.ModelAdmin):
    list_display=('question', 'department')


class TeacherDepartmentAdmin(admin.ModelAdmin):
    list_display=('teacher', 'department')


class QuestionRequestedTeacherAdmin(admin.ModelAdmin):
    list_display=('question', 'teacher')


admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Upvote)
admin.site.register(TeacherDepartment, TeacherDepartmentAdmin)
admin.site.register(QuestionDepartment, QuestionDepartmentAdmin)
admin.site.register(QuestionRequestedTeacher, QuestionRequestedTeacherAdmin)