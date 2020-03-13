WELCOME_CARD = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.0",
    "type": "AdaptiveCard",
    "speak": "Welcome to Computer Science course units bot",
    "body": [
        {
            "type": "TextBlock",
            "text": "Welcome to Computer Science course units bot",
            "weight": "bolder",
            "isSubtle": True,
            "separator": True
        },
        {
            "type": "TextBlock",
            "text": "Information you will found about a selected course includes",
            "separator": True,
            "size": "auto"
        },
        {
            "type": "ColumnSet",
            "separator": True,
            "columns": [
                {
                    "type": "Column",
                    "width": "auto",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Course's Lecture Hall",
                            "color": "accent",
                            "weight": "bolder",
                            "size": "auto",
                            "spacing": "medium",
                        },
                        {
                            "type": "TextBlock",
                            "color": "accent",
                            "text": "Course's Exam Schedule",
                            "size": "auto",
                            "weight": "bolder",
                            "spacing": "medium",
                        },
                    ],
                },
            ]
        },
        {
            "type": "ColumnSet",
            "separator": True,
            "columns": [
                {
                    "type": "Column",
                    "width": "auto",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Course's TAs",
                            "color": "accent",
                            "weight": "bolder",
                            "spacing": "medium",
                            "size": "auto",
                        },
                        {
                            "type": "TextBlock",
                            "color": "accent",
                            "text": "Course's Lecturer details",
                            "weight": "bolder",
                            "spacing": "medium",
                            "size": "auto",
                        },
                    ],
                },
            ]
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "You ready? Click to start!",
        }
    ],
}
