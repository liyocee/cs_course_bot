from plistlib import Dict
from typing import List

from bots.courses_bot.data_models.lecture_hall import LectureHall


class CourseUnit:
    def __init__(self, name: str, code: str, lecture_hall: LectureHall, exam_schedule: str):
        self.name: str = name
        self.code: str = code
        self.lecture_hall: LectureHall = lecture_hall
        self.exam_schedule = exam_schedule

    @classmethod
    def create(cls, lecture_halls: List[LectureHall]):

        def apply(course_unit: Dict) -> CourseUnit:
            return cls(
                name=course_unit["name"],
                code=course_unit["code"],
                exam_schedule=course_unit["exam_schedule"],
                lecture_hall=LectureHall.search_by_code(lecture_halls, course_unit["lecture_hall"])
            )
        return apply

    @staticmethod
    def search_by_code(course_units: List[object], codes: List[str]) -> List[object]:
        units = filter(
            lambda x: x.code == x.code in codes,
            course_units
        )
        return list(units)
