from django.db import models
from core import models as core_models


class Consulting2(core_models.TimeStampedModel):

    """ Consulting2 Model Definition """
    STUDENT_M_1 = "m1"
    STUDENT_M_2 = "m2"
    STUDENT_M_3 = "m3"
    STUDENT_H_1 = "h1"
    STUDENT_H_2 = "h2"
    STUDENT_H_3 = "h3"

    STUDENT_CHOICES = (
        (STUDENT_M_1, "중학생 1학년"),
        (STUDENT_M_2, "중학생 2학년"),
        (STUDENT_M_3, "중학생 3학년"),
        (STUDENT_H_1, "고등학생 1학년"),
        (STUDENT_H_2, "고등학생 2학년"),
        (STUDENT_H_3, "고등학생 3학년"),
    )

    TIME_CHOICES = (
        ("time1", "오전 9시 - 오전 10시"),
        ("time2", "오전 10시 - 오전 11시"),
        ("time3", "오전 11시 - 오후 12시"),
        ("time4", "오후 12시 - 오후 13시"),
        ("time5", "오후 13시 - 오후 14시"),
        ("time6", "오후 14시 - 오후 15시"),
        ("time7", "오후 15시 - 오후 16시"),
        ("time8", "오후 16시 - 오후 17시"),
        ("time9", "오후 17시 - 오후 18시"),
        ("time10", "오후 18시 - 오후 19시"),
        ("time11", "오후 19시 - 오후 20시"),
        ("time12", "오후 20시 - 오후 21시"),
    )

    student_name = models.CharField(max_length=140)
    student_grade = models.CharField(
        max_length=20, choices=STUDENT_CHOICES, default='')
    phone_number1 = models.CharField(max_length=3)
    phone_number2 = models.CharField(max_length=4)
    phone_number3 = models.CharField(max_length=4)

    region = models.CharField(max_length=140)
    consulting_time = models.CharField(
        max_length=12, choices=TIME_CHOICES, default='')

    Personal_information_consent = models.BooleanField(default=False)

    def phone_number(self):
        phone_number = f"{self.phone_number1} - {self.phone_number2} - {self.phone_number3}"
        return phone_number
