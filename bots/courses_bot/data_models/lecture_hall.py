from typing import Dict, List


class LectureHall:
    """Lecture hall data model"""

    def __init__(self, building_name: str, room_number: str, code: str):
        self.building_name = building_name
        self.room_number = room_number
        self.code = code

    def __str__(self):
        return f"Building Name: {self.building_name} | Room No: {self.room_number} | "

    @classmethod
    def create(cls, hall: Dict) -> object:
        """
        Create a lecture hall from the provided hall dict
        :param hall:
        :return:
        """
        # validate invariants
        for invariant in ['building_name', 'room_number', 'code']:
            assert invariant in hall, f'Missing required parameter {invariant}'

        return cls(
            building_name=hall["building_name"],
            room_number=hall["room_number"],
            code=hall["code"]
        )

    @staticmethod
    def search_by_code(lecture_halls: List[object], code: str) -> object:
        """
        Search for a lecture hall matching the provided code
        :param lecture_halls:
        :param code:
        :return:
        """
        halls = filter(
            lambda x: x.code == code,
            lecture_halls
        )
        halls = list(halls)

        return halls[0] if len(halls) > 0 else None

