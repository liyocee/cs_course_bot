from typing import List

from .course_unit import CourseUnit
from .lecturer import Lecturer, CourseTeachingAssistant


class Course:
    def __init__(
        self,
        course_units: List[CourseUnit],
        lecturers: List[Lecturer],
        teaching_assistants: List[CourseTeachingAssistant]
    ):
        self.course_units = course_units
        self.lecturers = lecturers
        self.teaching_assistants = teaching_assistants

    @classmethod
    def load_courses(cls):
        pass
