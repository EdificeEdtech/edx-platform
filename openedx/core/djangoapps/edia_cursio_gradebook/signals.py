"""
This file contains receivers of course publication signals.
"""

import logging

from django.dispatch import receiver
from opaque_keys.edx.keys import CourseKey
from openedx.core.djangoapps.signals.signals import GRADES_UPDATED

log = logging.getLogger(__name__)


@receiver(GRADES_UPDATED)
def listen_for_grade_calculation(sender, username, grade_summary, course_key, deadline, **kwargs):  # pylint: disable=unused-argument
    """Receive 'MIN_GRADE_REQUIREMENT_STATUS' signal and update minimum grade requirement status.

    Args:
        sender: None
        username(string): user name
        grade_summary(dict): Dict containing output from the course grader
        course_key(CourseKey): The key for the course
        deadline(datetime): Course end date or None

    Kwargs:
        kwargs : None

    """
    # This needs to be imported here to avoid a circular dependency
    # that can cause syncdb to fail.
    from openedx.core.djangoapps.credit import api

    course_id = CourseKey.from_string(unicode(course_key))
    is_credit = api.is_credit_course(course_id)
    print('listen_for_grade_calculation for Edia')
    log.info('listen_for_grade_calculation for Edia')
