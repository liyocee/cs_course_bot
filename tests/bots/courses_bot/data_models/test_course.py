from bots.courses_bot.data_models.course import Course
from config import DefaultConfig


class TestCourse:
    def test_load_courses(self):
        config = DefaultConfig()
        course = Course.load_courses(config)

        assert course is not None
        assert len(course.course_units) > 0
        assert len(course.lecturers) > 0
        assert len(course.teaching_assistants) > 0

