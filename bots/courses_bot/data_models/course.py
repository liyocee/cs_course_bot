import json
from typing import List, Callable, TypeVar, Dict

from bots.courses_bot.data_models.lecture_hall import LectureHall
from config import DefaultConfig
from .course_unit import CourseUnit
from .lecturer import Lecturer, CourseTeachingAssistant

T = TypeVar('T')


class Course:
    """Course model"""
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
    def load_courses(cls, config: DefaultConfig):
        """
        Create a Course from course json files resources
        :param config:
        :return:
        """
        lecture_halls = cls.load_course_resource(config.CoursePaths.LECTURER_HALLS.value, LectureHall.create)
        course_units = cls.load_course_resource(config.CoursePaths.COURSE_UNITS.value, CourseUnit.create(lecture_halls))
        lecturers = cls.load_course_resource(config.CoursePaths.LECTURER.value, Lecturer.create(course_units))
        teaching_assistants = cls.load_course_resource(
            config.CoursePaths.TEACHING_ASSISTANTS.value, Lecturer.create(course_units))

        return cls(
            course_units=course_units,
            lecturers=lecturers,
            teaching_assistants=teaching_assistants
        )

    @staticmethod
    def load_course_resource(full_path: str, resource_factory: Callable[[Dict], T]) -> List[T]:
        """
        Create an object of T from a json input
        :param full_path:
        :param resource_factory:
        :return:
        """
        with open(full_path) as input_stream:
            result = map(
                lambda item: resource_factory(item),
                json.load(input_stream)
            )
            return list(result)
