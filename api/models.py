import numbers
from statistics import mode
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class User(models.Model):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    TYPE_CHOICES = [
        (STUDENT, 'STUDENT'),
        (TEACHER, 'TEACHER'),
    ]

    username = models.CharField(unique=True, max_length=12)
    name = models.CharField(max_length=126, null=False, blank=False)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=STUDENT)
    personal_email = models.EmailField(unique=True)
    college_email = models.EmailField(unique=True)


class Question(models.Model):
    text = models.CharField(max_length=1000, blank=False, null=False)
    upvotes_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")


class QuestionRequestedTeacher(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="requested_teachers")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_questions")


class Answer(models.Model):
    text = models.CharField(max_length=3000, blank=False, null=False)
    question_id = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="answer")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")   


class Upvote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')


class Topic(models.Model):
    topic = models.CharField(max_length=30, blank=False, null=False)
    question = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")


class TeacherRelatedSubject(models.Model):
    pass