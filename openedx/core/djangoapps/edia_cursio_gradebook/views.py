"""
Course API Views
"""

import logging

from django.db import transaction
from openedx.core.lib.api.view_utils import view_auth_classes, DeveloperErrorViewMixin
from rest_framework.generics import RetrieveAPIView

from api import get_course_scores, get_student_scores, get_course_outline
from serializers import CourseSerializer, StudentSerializer, ProgressSummarySerializer

LOG = logging.getLogger('edia.gradebook.api')


@view_auth_classes(is_authenticated=True)
@transaction.non_atomic_requests
class CourseResultsView(DeveloperErrorViewMixin, RetrieveAPIView):
    serializer_class = CourseSerializer

    @transaction.non_atomic_requests
    def get_object(self):
        """
        Return the requested scores.
        """
        requested_params = self.request.query_params.copy()
        requested_params.update({'course_key': self.kwargs['course_key_string']})
        course_id = requested_params['course_key']

        return get_course_scores(course_id)


@view_auth_classes(is_authenticated=True)
@transaction.non_atomic_requests
class StudentResultsView(DeveloperErrorViewMixin, RetrieveAPIView):
    serializer_class = StudentSerializer

    @transaction.non_atomic_requests
    def get_object(self):
        """
        Return the requested scores.
        """
        requested_params = self.request.query_params.copy()
        requested_params.update({'course_key': self.kwargs['course_key_string']})
        course_id = requested_params['course_key']

        requested_params.update({'username': self.kwargs['username']})
        username = requested_params['username']

        return get_student_scores(course_id, username)


@view_auth_classes(is_authenticated=True)
class OutlineView(DeveloperErrorViewMixin, RetrieveAPIView):
    serializer_class = ProgressSummarySerializer

    @transaction.non_atomic_requests
    def get_object(self):
        """
        Return the course outline
        """
        requested_params = self.request.query_params.copy()
        requested_params.update({'course_key': self.kwargs['course_key_string']})
        course_id = requested_params['course_key']
        user = self.request.user;
        return get_course_outline(user, course_id)