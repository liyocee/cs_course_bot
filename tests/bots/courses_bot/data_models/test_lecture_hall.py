from typing import Dict

import pytest

from bots.courses_bot.data_models.lecture_hall import LectureHall


class TestLectureHall:
    """LectureHall data model tests"""

    def test_create_lecture_hall(self):
        lecture_hall_dict: Dict = {
            "building_name": "HALL_1",
            "room_number": "100",
            "code": "1201"
        }
        lecture_hall: LectureHall = LectureHall.create(lecture_hall_dict)
        assert lecture_hall.building_name == "HALL_1"
        assert lecture_hall.room_number == "100"
        assert lecture_hall.code == "1201"
        assert str(lecture_hall) == "Building Name: HALL_1 | Room No: 100 | "

    def test_create_lecture_hall_invalid_data(self):
        lecture_hall_dict: Dict = {
            "building_name": "HALL_1",
            "code": "1201"
        }
        with pytest.raises(AssertionError):
            LectureHall.create(lecture_hall_dict)

    def test_search_by_code(self):
        halls = [
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

        halls = list(map(lambda x: LectureHall.create(x), halls))
        found_hall: LectureHall = LectureHall.search_by_code(halls, "300")
        assert found_hall is not None
        assert found_hall.code == "300"
        assert found_hall.building_name == "HALL_2"

    def test_search_by_code_hall_found(self):
        assert LectureHall.search_by_code([], "300") is None
