from django.utils import timezone
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BoardType(AbstractItem):

    """ BoardType Model Definition """

    class Meta:
        verbose_name = "Board Type"


# 강의 소개에 들어갈 공통된 것들
class TeachingTextbooks(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "강의 교재"


class LectureGrade(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "강의대상"


class TextbookFeatures(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "교재 특징"


class CoursePeriod(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "수강기간"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="board_photos")
    board = models.ForeignKey(
        "Board", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Board(core_models.TimeStampedModel):

    """ Board Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="boards", on_delete=models.CASCADE
    )
    board_type = models.ForeignKey(
        "BoardType", related_name="boards", on_delete=models.SET_NULL, null=True
    )
    teaching_textbooks = models.ManyToManyField(
        "TeachingTextbooks", related_name="boards", blank=True)
    lecture_grade = models.ManyToManyField(
        "LectureGrade", related_name="boards", blank=True)
    course_period = models.ManyToManyField(
        "CoursePeriod", related_name="boards", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("boards:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
