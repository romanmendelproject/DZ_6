from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    SEX_CHOICES = (('m', 'Men'),('f', 'Women'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.full_name


class Student(models.Model):
    SEX_CHOICES = (('m', 'Men'), ('f', 'Women'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField(blank=True)
    city = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    date = models.DateField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title