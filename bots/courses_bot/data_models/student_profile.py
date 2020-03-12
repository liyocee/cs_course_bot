from typing import Optional

from .course_unit import CourseUnit


class StudentProfile:

    def __init__(self, name: str = None,  admission_number: str = None, course_unit: CourseUnit = None):
        self.name: Optional[str] = name
        self.admission_number: Optional[str] = admission_number
        self.course_unit: Optional[CourseUnit] = course_unit
