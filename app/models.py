
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    TYPE_CHOICES = [
        (STUDENT, 'STUDENT'),
        (TEACHER, 'TEACHER'),
    ]

    username = None
    email = None
    college_email = models.EmailField(unique=True)
    personal_email = models.EmailField(null=True, blank=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=STUDENT)

    objects = UserManager()

    USERNAME_FIELD = 'college_email'
    REQUIRED_FIELDS = []


class Question(models.Model):
    text = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    text = models.TextField(blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text


class Upvote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')


class QuestionDepartment(models.Model):
    CS = 'COMPUTER SCIENCE'
    DS = 'DATA SCIENCE'
    EC = 'ELECTRONICS'
    MECH = 'MECHANICAL'
    EEE = 'ELECTRICAL'
    OTHER_DPT = 'OTHER'
    
    DEPARTMENT_CHOICES = [
        (CS, 'COMPUTER SCIENCE'),
        (DS, 'DATA SCIENCE'),
        (EC, 'ELECTRONICS'),
        (MECH, 'MECHANICAL'),
        (EEE, 'ELECTRICAL'),
        (OTHER_DPT, 'OTHER')
    ]

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="departments")
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, blank=False, null=False)


class TeacherDepartment(models.Model):
    CS = 'COMPUTER SCIENCE'
    DS = 'DATA SCIENCE'
    EC = 'ELECTRONICS'
    MECH = 'MECHANICAL'
    EEE = 'ELECTRICAL'
    
    DEPARTMENT_CHOICES = [
        (CS, 'COMPUTER SCIENCE'),
        (DS, 'DATA SCIENCE'),
        (EC, 'ELECTRONICS'),
        (MECH, 'MECHANICAL'),
        (EEE, 'ELECTRICAL')
    ]

    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name="my_department", null=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES, blank=False, null=False)
    


class QuestionRequestedTeacher(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="requested_teachers")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_questions")
