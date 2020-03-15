from typing import List, Dict, Callable
from unittest import TestCase

from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.lecture_hall import LectureHall
from bots.courses_bot.data_models.lecturer import Lecturer


class TestLecturer:
    lecture_halls = [
        {
            "building_name": "HALL_1",
            "room_number": "100",
            "code": "100"
        },
        {
            "building_name": "HALL_2",
            "room_number": "100",
            "code": "300"
        }
    ]
    halls: List[LectureHall] = list(map(lambda x: LectureHall.create(x), lecture_halls))

    def _create_course_units(self) -> List[CourseUnit]:
        course_units_data = [
            {
                "name": "Data structures and Algorithms",
                "code": "CS-120",
                "lecture_hall": "100",
                "exam_schedule": "April 30, 2020"
            },
            {
                "name": "Discrete Mathematics",
                "code": "CS-121",
                "lecture_hall": "101",
                "exam_schedule": "May 14, 2020"
            }
        ]
        course_unit_factory: Callable[[Dict], CourseUnit] = CourseUnit.create(self.halls)

        return list(map(lambda x: course_unit_factory(x), course_units_data))

    def test_create(self):
        lecturer_data = {
            "name": "Dr Kennedy Bett",
            "email": "bett@uon.ac.ke",
            "phone": "+254715441309",
            "office_hours": [
                {
                    "day": "Monday",
                    "start_time": "0900 hrs",
                    "end_time": "1300 hrs"
                },
                {
                    "day": "Fridays",
                    "start_time": "0700 hrs",
                    "end_time": "1000 hrs"
                }
            ],
            "course_units": [
                "CS-120"
            ]
        }

        lecturer_factory: Callable[[Dict], Lecturer] = Lecturer.create(self._create_course_units())
        lecturer = lecturer_factory(lecturer_data)
        assert lecturer is not None
        assert lecturer.name == "Dr Kennedy Bett"
        assert len(lecturer.course_units) == 1
        assert len(lecturer.office_hours) == 2

    def _create_lecturers(self) -> List[Lecturer]:
        data = [
            {
                "name": "Dr Kennedy Bett",
                "email": "bett@uon.ac.ke",
                "phone": "+254715441309",
                "office_hours": [
                    {
                        "day": "Monday",
                        "start_time": "0900 hrs",
                        "end_time": "1300 hrs"
                    },
                    {
                        "day": "Fridays",
                        "start_time": "0700 hrs",
                        "end_time": "1000 hrs"
                    }
                ],
                "course_units": [
                    "CS-120"
                ]
            },
            {
                "name": "Prof Elijah Simiyu",
                "email": "simiyu@uon.ac.ke",
                "phone": "+254715449009",
                "office_hours": [
                    {
                        "day": "Tuesday",
                        "start_time": "1100 hrs",
                        "end_time": "1300 hrs"
                    },
                    {
                        "day": "Wednesday",
                        "start_time": "1600 hrs",
                        "end_time": "1700 hrs"
                    }
                ],
                "course_units": [
                    "CS-121"
                ]
            }
        ]

        lecturer_factory: Callable[[Dict], Lecturer] = Lecturer.create(self._create_course_units())
        return list(map(lambda x: lecturer_factory(x), data))

    def test_search_by_course_code(self):
        found: List[Lecturer] = Lecturer.search_by_course_code(self._create_lecturers(), 'CS-121')
        assert len(found) == 1
        assert found[0].name == "Prof Elijah Simiyu"
        assert len(found[0].course_units) == 1
        assert found[0].course_units[0].code == 'CS-121'

    def test_search_by_course_code_not_found(self):
        found: List[Lecturer] = Lecturer.search_by_course_code(self._create_lecturers(), 'Not Found')
        assert len(found) == 0
