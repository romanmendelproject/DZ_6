from django.urls import path, re_path, include

import courses.views as courses

app_name = 'courses'

urlpatterns = [

    path('', courses.CourseListView.as_view(), name='index'),
    path('course/create/', courses.CourseCreateView.as_view(),
         name='course_create'),
    path('course/detail/<int:pk>/',
         courses.CourseDetailView.as_view(),
         name='course'),
    path('course/update/<int:pk>/',
         courses.CourseUpdateView.as_view(),
         name='course_update'),
    path('course/delete/<int:pk>/',
         courses.CourseDeleteView.as_view(),
         name='course_delete'),
    ]