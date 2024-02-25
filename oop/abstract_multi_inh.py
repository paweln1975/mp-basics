from abc import ABC, abstractmethod


class Alert:
    def __init__(self, id):
        self.id = id

    def get_message(self):
        print("Alert {}".format(self.id))


class Warning(Alert):
    def get_message(self):
        print("Warning {}".format(self.id))


class Error(Alert):
    def get_message(self):
        print("Error {}".format(self.id))


class WarningError(Error, Warning):
    pass


warn_error8 = WarningError(8)
warn_error8.get_message()


class Robot:
    def greet(self):
        print("I am a robot")


class Android(Robot):
    def greet(self):
        super().greet()
        print("I am an android")


class PersonalAssistant(Robot):
    def greet(self):
        super().greet()
        print("I am a personal assistant")


class AssistantAndroid(Android, PersonalAssistant):
    def greet(self):
        super().greet()


r = AssistantAndroid()
r.greet()


class AssistantAndroid:
    @abstractmethod
    def abstract_method(self):
        print("Abstract Method")


class DefinteClass(AssistantAndroid):
    def abstract_method(self):
        print("Definite Method")


d = DefinteClass()
d.abstract_method()
