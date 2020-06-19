from django.urls import path
from boards import views as board_view

app_name = "core"

urlpatterns = [path("", board_view.MainView.as_view(), name="Main")]
