from typing import List, Dict

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

    @classmethod
    def create(cls, course_units: List[CourseUnit]):

        def apply(lecturer: Dict) -> Lecturer:
            return cls(
                name=lecturer["name"],
                email=lecturer["email"],
                phone=lecturer["phone"],
                course_units=CourseUnit.search_by_code(course_units, lecturer["course_units"]),
                office_hours=OfficeHours.create(lecturer["office_hours"])
            )
        return apply


class CourseTeachingAssistant(Lecturer):
    pass
