from enum import Enum
from typing import List

from bots.courses_bot.data_models.course import Course
from bots.courses_bot.data_models.course_unit import CourseUnit
from bots.courses_bot.data_models.lecturer import Lecturer, CourseTeachingAssistant


class Intents(Enum):
    ViewCourseExamSchedule = "ViewCourseExamSchedule"
    ViewCourseLectureHall = "ViewCourseLectureHall"
    ViewCourseLecturerDetails = "ViewCourseLecturerDetails"
    ViewCourseTeachingAssistant = "ViewCourseTeachingAssistant"


class CourseIntentHandlers:

    @staticmethod
    def get_handlers(course: Course):
        return {
            Intents.ViewCourseExamSchedule.value: CourseIntentHandlers.handle_course_exam_schedule(course),
            Intents.ViewCourseLectureHall.value: CourseIntentHandlers.handle_course_lecture_hall(course),
            Intents.ViewCourseLecturerDetails.value: CourseIntentHandlers.handle_course_lecturer_details(course),
            Intents.ViewCourseTeachingAssistant.value: CourseIntentHandlers.handle_course_ta_details(course)
        }

    @staticmethod
    def handle_course_exam_schedule(course:  Course):
        def course_exam_schedule(course_code: str):
            courses: List[CourseUnit] = CourseUnit.search_by_code(course.course_units, course_code)
            schedule: List[str] = list(map(lambda x: f"{x.exam_schedule} | ", courses))

            return f"Course exam schedule is: {','.join(schedule)}" if len(schedule) > 0 else "No exam schedule found!"

        return course_exam_schedule

    @staticmethod
    def handle_course_lecture_hall(course:  Course):
        def course_lecture_hall(course_code: str):
            courses: List[CourseUnit] = CourseUnit.search_by_code(course.course_units, course_code)
            lecturer_halls: List[str] = list(map(
                lambda x: str(x.lecture_hall) if x else None,
                courses
            ))

            lecturer_hall = list(filter(lambda x: str(x) is not None, lecturer_halls))

            return f"Course Lecturer Hall is: {','.join(lecturer_hall)}" \
                if len(lecturer_hall) > 0 else "No Lecture hall found!"

        return course_lecture_hall

    @staticmethod
    def handle_course_lecturer_details(course:  Course):

        def course_lecturer(course_code: str):
            lecturers: List[Lecturer] = Lecturer.search_by_course_code(course.lecturers, course_code)

            lecturers: List[str] = list(map(
                lambda x: str(x) if x else None,
                lecturers
            ))

            lecturers_str: List[str] = list(filter(lambda x: x is not None, lecturers))

            return f"Lecturer is : {','.join(lecturers_str)}" if len(lecturers_str) > 0 else "No Lecture found!"

        return course_lecturer

    @staticmethod
    def handle_course_ta_details(course:  Course):
        def course_ta(course_code: str):
            ta_s: List[CourseTeachingAssistant] = Lecturer.search_by_course_code(course.lecturers, course_code)

            ta_s: List[str] = list(map(
                lambda x: str(x) if x else None,
                ta_s
            ))

            ta_s_str: List[str] = list(filter(lambda x: x is not None, ta_s))

            return f"Teaching assistant is : {','.join(ta_s_str)}"  if len(ta_s_str) > 0 else "No TA found!"

        return course_ta

