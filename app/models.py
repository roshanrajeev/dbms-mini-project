from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


# Create your models here.
class User(AbstractUser):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    TYPE_CHOICES = [
        (STUDENT, "STUDENT"),
        (TEACHER, "TEACHER"),
    ]

    username = None
    email = None
    college_email = models.EmailField(unique=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=STUDENT)

    objects = UserManager()

    USERNAME_FIELD = "college_email"
    REQUIRED_FIELDS = []


class Department(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    personal_email = models.EmailField(null=True, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="profile"
    )


class Question(models.Model):
    text = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="questions"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    text = models.TextField(blank=False, null=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text


class Upvote(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="upvotes"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upvotes")
