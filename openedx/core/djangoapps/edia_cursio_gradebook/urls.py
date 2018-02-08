"""
Course API URLs
"""
from django.conf import settings
from django.conf.urls import patterns, url, include

from .views import CourseResultsView, StudentResultsView,OutlineView


urlpatterns = patterns(
    '',
    url(r'^v1/course/{}/outline'.format(settings.COURSE_KEY_PATTERN), OutlineView.as_view(), name="student-list"),
    url(r'^v1/course/{}/student/{}'.format(settings.COURSE_KEY_PATTERN, settings.USERNAME_PATTERN), StudentResultsView.as_view(), name="student-list"),
    url(r'^v1/course/{}'.format(settings.COURSE_KEY_PATTERN), CourseResultsView.as_view(), name="course-list")

)
