from bots.courses_bot.data_models.lecture_hall import LectureHall


class CourseUnit:
    def __init__(self, name: str, code: str, lecture_hall: LectureHall):
        self.name: str = name
        self.code: str = code
        self.lecture_hall: LectureHall = lecture_hall

