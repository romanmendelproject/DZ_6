from django import forms

from courses.models import Lesson, Course

class BlogBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class LessonForm(BlogBaseForm):
    class Meta:
        model = Lesson
        fields = '__all__'