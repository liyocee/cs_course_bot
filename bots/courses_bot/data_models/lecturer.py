from typing import List

from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.office_hours import OfficeHours


class Lecturer:

    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        office_hours: List[OfficeHours],
        course_units: List[CourseUnit],
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.office_hours = office_hours
        self.course_units = course_units


class CourseTeachingAssistant(Lecturer):
    pass
