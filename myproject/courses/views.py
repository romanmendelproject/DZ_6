from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.db import transaction
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from courses.models import Course, Lesson
from django.urls import reverse_lazy
from courses.forms import LessonForm

class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('courses:index')
    fields = '__all__'


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
            data = super().get_context_data(**kwargs)
            CourseFormSet = inlineformset_factory(Course, Lesson, form=LessonForm, extra=1)
            data['lesson_courses'] = CourseFormSet(self.request.POST or None, instance=self.object)
            return data

    def form_valid(self, form):
        context = self.get_context_data()
        lesson_courses = context['lesson_courses']

        with transaction.atomic():
            self.object = form.save()
            if lesson_courses.is_valid():
                lesson_courses.instance = self.object
                lesson_courses.save()

        return super().form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())