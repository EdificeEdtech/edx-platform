class CourseDescriptor:
    id = None
    course_key = None
    course_name = None
    students = []

    def __init__(self, id, course_key, course_name=None, students=[]):
        self.id = id;
        self.course_key = course_key
        self.course_name = course_name
        self.students = students;


class StudentDescriptor:
    id = None
    email = None
    username = None
    student_number = None
    anonymous = None
    course_key = None
    course_name = None
    progress = None

    def __init__(self, id, username=None, email=None, anonymous=None, progress=None, course_key=None, student_number=None, course_name=None):
        self.id = id
        self.email = email
        self.username = username
        self.student_number = student_number
        self.anonymous = anonymous
        self.progress = progress
        self.course_key = course_key
        self.course_name = course_name


class ProgressSummary:
    chapters = []

    def __init__(self, chapters=[]):
        self.chapters = chapters;


class Chapter:
    course = None
    display_name = None
    url_name = None
    sections = []

    def __init__(self, course, display_name, url_name, sections=[]):
        self.course = course;
        self.display_name = display_name;
        self.url_name = url_name;
        self.sections = sections;


class Section:
    display_name = None
    url_name = None
    section_total = None
    scores = []
    format = None
    graded = False

    def __init__(self, display_name, url_name, section_total, scores, format, graded):
        self.display_name = display_name;
        self.url_name = url_name;
        self.section_total = section_total;
        self.scores = scores;
        self.format = format;
        self.graded = graded;

#
#
# class Score:
#     block_id = None
#     course_key = None
#     block_type = None
#     earned = 0
#     possible = 1
#     graded = False
#     section = None
#     location = None
#
#     def __init__(self):
#         pass
