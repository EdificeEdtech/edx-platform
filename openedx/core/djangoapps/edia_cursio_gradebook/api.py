import logging
import pprint
import json

from courseware import courses
from django.contrib.auth.models import User
# from .grades import get_weighted_scores
from lms.djangoapps.grades.new.course_grade_factory import CourseGradeFactory
from django.db import transaction
from opaque_keys.edx.keys import CourseKey
from student.models import CourseEnrollment
from student.models import anonymous_id_for_user, user_by_anonymous_id
from model import StudentDescriptor, CourseDescriptor, ProgressSummary, Chapter, Section
from social_django.models import UserSocialAuth

LOG = logging.getLogger('edia.gradebook.api')


@transaction.non_atomic_requests
def get_course_scores(course_id):
    course_key = CourseKey.from_string(unicode(course_id));
    course = courses.get_course(course_key)

    students = []
    # enrolled_students = [student for student in CourseEnrollment.objects.users_enrolled_in(course_key) if student.is_active]
    enrolled_students = [student for student in CourseEnrollment.objects.users_enrolled_in(course_key)]
    for student in enrolled_students:
        student_descriptor = build_student(course, student)
        students.append(student_descriptor)

    return CourseDescriptor(id=course.id, course_key=course_id, course_name=course.display_name, students=students)


@transaction.non_atomic_requests
def get_student_scores(course_id, username):
    course_key = CourseKey.from_string(unicode(course_id));
    course = courses.get_course(course_key)
    student = get_student_from_identifier(username)
    return build_student(course, student)


@transaction.non_atomic_requests
def get_course_outline(user, course_id):
    # pp = pprint.PrettyPrinter(indent=4, depth=6)
    course_key = CourseKey.from_string(unicode(course_id));
    course = courses.get_course(course_key)
    progress = get_weighted_scores(user, course)
    return progress


def get_weighted_scores(student, course):
    chapter_grades = CourseGradeFactory().create(student, course).chapter_grades
    return ProgressSummary(get_chapters(chapter_grades, course))


def get_chapters(chapter_grades, course):
    for chapter in chapter_grades.values():
        yield Chapter(course.id, chapter['display_name'], chapter['url_name'], get_sections(chapter))


def get_sections(chapter):
    for section in chapter['sections']:
        yield Section(section.display_name,
                      section.url_name,
                      section.all_total,
                      section.problem_scores.values(),
                      section.format, section.graded)


def build_student(course, student):
    # pp = pprint.PrettyPrinter(indent=4, depth=6)
    anonymous = anonymous_id_for_user(student, course.id)
    progress = get_weighted_scores(student, course)
    student_number = get_student_number(student)

    # LOG.info(pp.pformat(progress))
    student_descriptor = StudentDescriptor(student.id,
                                           username=student.username,
                                           student_number=student_number,
                                           email=student.email,
                                           anonymous=anonymous,
                                           progress=progress,
                                           course_key=course.id,
                                           course_name=course.display_name)
    return student_descriptor


def get_student_number(student):
    """HvA specific code to get the student_number"""
    student_number = None
    user_social_auth = get_social_user('tpa-saml', student)
    if user_social_auth is not None:
        student_number = user_social_auth.uid.rsplit(':', 1)[-1]

    return student_number


def get_social_user(provider, student):
    rv = [usa for usa in UserSocialAuth.get_social_auth_for_user(student) if usa.provider == provider]
    if len(rv) > 0:
        return rv[0]


def get_student_from_identifier(unique_student_identifier):
    """
    Gets a student object using either an email address or username.

    Returns the student object associated with `unique_student_identifier`

    Raises User.DoesNotExist if no user object can be found.
    """
    unique_student_identifier = strip_if_string(unique_student_identifier)

    # Check if the user is anonymous, deref if the user is
    if not user_by_anonymous_id(unique_student_identifier) is None:
        student = user_by_anonymous_id(unique_student_identifier)
    elif "@" in unique_student_identifier:
        student = User.objects.get(email=unique_student_identifier)
    else:
        student = User.objects.get(username=unique_student_identifier)
    return student


def strip_if_string(value):
    if isinstance(value, basestring):
        return value.strip()
    return value
