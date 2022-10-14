from lib2to3.pgen2.token import OP
from socket import fromshare
from django import forms
from exams.models import Questions,Options

class ExamForm(forms.ModelForm):
    class Meta:
        model=Questions
        exclude=('',)

class OptionForm(forms.ModelForm):
    class Meta:
        model=Options
        exclude=('',)

