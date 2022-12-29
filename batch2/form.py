from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from batch2.models import ProfileData, TeacherData, UploadImage


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = ['first_name','last_name']


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    Email = forms.EmailField(label = "Enter email id",max_length=200)
    age = forms.IntegerField(label="Enter age")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherData
        fields =  ['name','email']


class NewStudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 10)
    email     = forms.EmailField(label="Enter Email")
    file      = forms.FileField() # for creating file input


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'