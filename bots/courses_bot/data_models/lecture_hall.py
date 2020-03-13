from typing import Dict, List


class LectureHall:

    def __init__(self, building_name: str, room_number: str, code: str):
        self.building_name = building_name
        self.room_number = room_number
        self.code = code

    @classmethod
    def create(cls, hall: Dict) -> object:
        return cls(
            building_name=hall["building_name"],
            room_number=hall["room_number"],
            code=hall["code"]
        )

    @staticmethod
    def search_by_code(lecture_halls: List[object], code: str) -> object:
        halls = filter(
            lambda x: x.code == code,
            lecture_halls
        )
        halls = list(halls)

        return halls[0] if len(halls) > 0 else None

