from rest_framework import serializers


class ScoreSerializer(serializers.Serializer):
    earned = serializers.FloatField()
    possible = serializers.FloatField()
    graded = serializers.BooleanField()


class ProblemScoreSerializer(serializers.Serializer):
    raw_earned = serializers.FloatField()
    raw_possible = serializers.FloatField()
    earned = serializers.FloatField()
    possible = serializers.FloatField()
    graded = serializers.BooleanField()


class SectionSerializer(serializers.Serializer):
    display_name = serializers.CharField()
    url_name = serializers.CharField()
    section_total = ScoreSerializer()
    scores = ProblemScoreSerializer(many=True)
    format = serializers.CharField()
    graded = serializers.BooleanField()


class ChaptersSerializer(serializers.Serializer):
    course = serializers.CharField()
    display_name = serializers.CharField()
    url_name = serializers.CharField()
    sections = SectionSerializer(many=True)


class ProgressSummarySerializer(serializers.Serializer):
    chapters = ChaptersSerializer(many=True)


class StudentSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    id = serializers.CharField()
    username = serializers.CharField()
    student_number = serializers.CharField()
    course_key = serializers.CharField()
    course_name = serializers.CharField()
    email = serializers.CharField()
    anonymous = serializers.CharField()
    progress = ProgressSummarySerializer()


class CourseSerializer(serializers.Serializer):
    id = serializers.CharField()
    course_key = serializers.CharField()
    course_name = serializers.CharField()
    students = StudentSerializer(many=True)