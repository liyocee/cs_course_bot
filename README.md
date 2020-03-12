# Computer Science(CS) Course Units Bot (cs_course_bot)
A demonstration bot built to help Computer Science students find out details about the course units they are undertaking in
a hypothetical university

This bot leverages  Microsoft Bot Framework and it shows how to create a simple bot using [Bot Framework](https://dev.botframework.com)

## Prerequisites

This sample **requires** prerequisites in order to run.

### Install Python 3.6

### Running the sample
- Create a python 3.6 virtual environment
- Switch to the created virtual environment
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python app.py`


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/v1/echo` - for the echo bot that occurs back your input
- Enter a Bot URL of `http://localhost:3978/api/v1/course_units` - for the CS course bot

