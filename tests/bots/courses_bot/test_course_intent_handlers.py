from bots.courses_bot.course_intent_handlers import CourseIntentHandlers, Intents
from bots.courses_bot.data_models.course import Course
from config import DefaultConfig


class TestCourseIntentHandlers:
    course = Course.load_courses(DefaultConfig())

    def test_get_handlers(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        required_handlers = {
            Intents.ViewCourseExamSchedule.value,
            Intents.ViewCourseLectureHall.value,
            Intents.ViewCourseLecturerDetails.value,
            Intents.ViewCourseTeachingAssistant.value
        }

        assert set(handlers.keys()) == required_handlers

    def test_handle_course_exam_schedule(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseExamSchedule.value)
        assert handler is not None
        assert 'April 30, 2020' in handler('CS-120')

    def test_handle_course_exam_schedule_course_schedule_not_found(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseExamSchedule.value)
        assert handler is not None
        assert 'No exam schedule found!' in handler('not found')

    def test_handle_course_lecture_hall(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseLectureHall.value)
        assert handler is not None
        assert 'Course Lecturer Hall is: Building Name: JKF Towers' in handler('CS-120')

    def test_handle_course_lecture_hall_course_lecture_hall_not_found(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseLectureHall.value)
        assert handler is not None
        assert 'No Lecture hall found!' in handler('not found')

    def test_handle_course_lecturer_details(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseLecturerDetails.value)
        assert handler is not None
        assert 'Lecturer is : Name: Dr Kennedy Bett' in handler('CS-120')

    def test_handle_course_lecturer_details_not_found(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseLecturerDetails.value)
        assert handler is not None
        assert 'No Lecturer found!' in handler('not found')

    def test_handle_course_ta_details(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseTeachingAssistant.value)
        assert handler is not None
        assert 'Teaching assistant is : Name: Towet Anatoliy' in handler('CS-120')

    def test_handle_course_ta_details_course_ta_not_found(self):
        handlers = CourseIntentHandlers.get_handlers(self.course)
        handler = handlers.get(Intents.ViewCourseTeachingAssistant.value)
        assert handler is not None
        assert 'No TA found!' in handler('Not found')
