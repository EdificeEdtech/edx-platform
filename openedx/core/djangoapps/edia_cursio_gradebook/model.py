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
