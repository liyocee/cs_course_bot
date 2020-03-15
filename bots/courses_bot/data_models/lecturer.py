from typing import List, Dict, Set

from bots.courses_bot.data_models import course_unit
from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.office_hours import OfficeHours


class Lecturer:
    """Lecturer data model"""

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
        """
        Create a factory function for creating Lecture
        :param course_units:
        :return:
        """

        def apply(lecturer: Dict) -> Lecturer:
            """
            Lecturer factory function
            :param lecturer:
            :return:
            """
            invariants: Set[str] = {'name', 'email', 'phone', 'course_units', 'office_hours'}
            provided_keys: Set[str] = set(lecturer.keys())
            # Validate invariants
            assert invariants == set(provided_keys), f"Missing parameters: {invariants.difference(provided_keys)}"

            return cls(
                name=lecturer["name"],
                email=lecturer["email"],
                phone=lecturer["phone"],
                course_units=CourseUnit.search_by_codes(course_units, lecturer["course_units"]),
                office_hours=OfficeHours.create(lecturer["office_hours"])
            )
        return apply

    def __str__(self):
        office_hours = ",".join(list(map(lambda x: str(x), self.office_hours)))
        return f"Name: {self.name} | Email: {self.email} | phone: {self.phone} | Office Hours: {office_hours}| "

    @staticmethod
    def search_by_course_code(lecturers: List[object], course_code: str) -> List[object]:
        """
        Search Lecturer by a course code for the course unit they teach
        :param lecturers:
        :param course_code:
        :return:
        """
        results = filter(
            lambda x: len(CourseUnit.search_by_code(x.course_units, course_code)) > 0,
            lecturers
        )

        return list(results)


class CourseTeachingAssistant(Lecturer):
    pass
