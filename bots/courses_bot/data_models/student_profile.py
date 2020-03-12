from enum import Enum
from typing import Optional

from botbuilder.schema import Attachment

from .course_unit import CourseUnit


class StudentProfile:

    def __init__(
        self,
        name: str = None,
        admission_number: str = None,
        course_unit: CourseUnit = None,
        picture: Attachment = None
    ):
        self.name: Optional[str] = name
        self.admission_number: Optional[str] = admission_number
        self.course_unit: Optional[CourseUnit] = course_unit
        self.picture: Optional[Attachment] = picture


class StudentProfileAttributes(Enum):
    NAME = "name"
    ADMISSION_NUMBER = "admission_number"
    COURSE_UNIT = "course_unit"
    PICTURE = "picture"

