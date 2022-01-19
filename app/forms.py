from django import forms
from django.db.models import fields

from app.models import Question


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)
    college_email = forms.EmailField(
        max_length=120, label="College Email", required=True
    )
    password = forms.CharField(
        max_length=30, label="Password", widget=forms.PasswordInput(), required=True
    )


class LoginForm(forms.Form):
    college_email = forms.EmailField(
        max_length=120, label="College Email", required=True
    )
    password = forms.CharField(
        max_length=30, label="Password", widget=forms.PasswordInput(), required=True
    )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text", "department")

    # text = forms.CharField(widget=forms.Textarea, required=True, label="Question")
    # department = forms.Foreign(choices=DEPARTMENT_CHOICES, required=True, label="Department")


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True, label="Answer")
