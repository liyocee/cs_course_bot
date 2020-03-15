from plistlib import Dict
from typing import List, Set, Callable

from bots.courses_bot.data_models.lecture_hall import LectureHall


class CourseUnit:
    """CourseUnit data model"""
    def __init__(self, name: str, code: str, lecture_hall: LectureHall, exam_schedule: str):
        self.name: str = name
        self.code: str = code
        self.lecture_hall: LectureHall = lecture_hall
        self.exam_schedule = exam_schedule

    @classmethod
    def create(cls, lecture_halls: List[LectureHall]) -> Callable[[Dict], object]:
        """
        Create a factory function for creating a CourseUnit from the provided lecture halls
        :param lecture_halls:
        :return:
        """

        def apply(course_unit: Dict) -> CourseUnit:
            """
            CourseUnit factory function
            :param course_unit:
            :return:
            """
            invariants: Set[str] = {'name', 'code', 'exam_schedule', 'lecture_hall'}
            provided_keys: Set[str] = set(course_unit.keys())
            # Validate invariants
            assert invariants == set(provided_keys), f"Missing parameters: {invariants.difference(provided_keys)}"

            return cls(
                name=course_unit["name"],
                code=course_unit["code"],
                exam_schedule=course_unit["exam_schedule"],
                lecture_hall=LectureHall.search_by_code(lecture_halls, course_unit["lecture_hall"])
            )
        return apply

    @staticmethod
    def search_by_codes(course_units: List[object], codes: List[str]) -> List[object]:
        """
        Search CourseUnits matching the provided course units codes
        :param course_units:
        :param codes:
        :return:
        """
        units = filter(
            lambda x: x.code in codes,
            course_units
        )
        return list(units)

    @staticmethod
    def search_by_code(course_units: List[object], code: str) -> List[object]:
        """
        Search CourseUnits matching a provided course unit code
        :param course_units:
        :param code:
        :return:
        """
        units = filter(
            lambda x: x.code == code,
            course_units
        )
        return list(units)
