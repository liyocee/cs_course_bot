#!/usr/bin/env python3
import os
from enum import Enum


def course_resource_path(resource_name):
    return f"{os.getcwd()}/bots/courses_bot/resources/{resource_name}"


class DefaultConfig:
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    # Luis app settings
    LUIS_APP_ID = os.environ.get("LuisAppId", "")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "")

    class CoursePaths(Enum):
        COURSE_UNITS = course_resource_path("course_units.json")
        LECTURER_HALLS = course_resource_path("lecture_halls.json")
        LECTURER = course_resource_path("lecturers.json")
        TEACHING_ASSISTANTS = course_resource_path("teaching_assistants.json")

