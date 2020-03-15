from typing import Dict, List
from unittest import TestCase

import pytest

from bots.courses_bot.data_models.office_hours import OfficeHours


class TestOfficeHours(TestCase):
    """OfficeHours data model tests"""

    def test_create_lecture_hall(self):
        office_hours_data = [
            {
                "day": "Monday",
                "start_time": "0900 hrs",
                "end_time": "1300 hrs"
            },
            {
                "day": "Tuesday",
                "start_time": "1000 hrs",
                "end_time": "1100 hrs"
            }
        ]

        office_hours: List[OfficeHours] = OfficeHours.create(office_hours_data)
        assert len(office_hours) == 2

        assert {"Monday", "Tuesday"} == set(map(lambda x: x.day, office_hours))
        assert {"0900 hrs", "1000 hrs"} == set(map(lambda x: x.start_time, office_hours))
        assert {"1300 hrs", "1100 hrs"} == set(map(lambda x: x.end_time, office_hours))
