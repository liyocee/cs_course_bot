from typing import Dict, Callable, List

from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.lecture_hall import LectureHall


class TestCourseUnit:
    """Tests for CourseUnit data model"""

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

    def test_create(self):
        course_unit_data: Dict = {
            "name": "Data structures and Algorithms",
            "code": "CS-120",
            "lecture_hall": "100",
            "exam_schedule": "April 30, 2020"
        }
        course_unit_factory: Callable[[Dict], CourseUnit] = CourseUnit.create(self.halls)
        course_unit: CourseUnit = course_unit_factory(course_unit_data)
        assert course_unit is not None
        assert course_unit.name == course_unit_data['name']
        assert course_unit.code == course_unit_data['code']
        assert course_unit.exam_schedule == course_unit_data['exam_schedule']
        assert course_unit.lecture_hall is not None
        assert course_unit.lecture_hall.building_name == "HALL_1"

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

    def test_search_by_codes(self):
        course_units: List[CourseUnit] = CourseUnit.search_by_codes(self._create_course_units(), ["CS-120"])
        assert len(course_units) == 1
        assert course_units[0].name == "Data structures and Algorithms"
        assert course_units[0].code == "CS-120"

    def test_search_by_codes_not_found(self):
        course_units: List[CourseUnit] = CourseUnit.search_by_codes(self._create_course_units(), ["Not Found"])
        assert len(course_units) == 0

    def test_search_by_code(self):
        course_units: List[CourseUnit] = CourseUnit.search_by_code(self._create_course_units(), "CS-120")
        assert len(course_units) == 1
        assert course_units[0].name == "Data structures and Algorithms"
        assert course_units[0].code == "CS-120"

    def test_search_by_code_not_found(self):
        course_units: List[CourseUnit] = CourseUnit.search_by_code(self._create_course_units(), "CS-120_not_found")
        assert len(course_units) == 0
