from typing import List, Dict


class OfficeHours:
    """OfficeHours data model"""
    def __init__(self, day: str, start_time: str, end_time: str):
        self.day: str = day
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Day: {self.day} From: {self.start_time} To: {self.end_time} |"

    @classmethod
    def create(cls, durations: List[Dict]) -> List[object]:
        """
        Create OfficeHour object from the provided list of dicts
        :param durations:
        :return:
        """
        office_hours = map(
            lambda x: cls(**x),
            durations
        )

        return list(office_hours)
