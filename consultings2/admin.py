from django.contrib import admin
from . import models


@admin.register(models.Consulting2)
class Consulting2Admin(admin.ModelAdmin):
    """ Consulting2 Admin Definition """

    list_display = ("student_name", "student_grade",
                    "phone_number", "region", "consulting_time", )
    ordering = ("student_name", "student_grade", )
    list_filter = ("region",)

    search_fields = ("=student_name", "=region")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "상담 관리"
