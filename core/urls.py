from django.urls import path
from boards import views as board_view
from consultings import views as consulting_view
from consultings2 import views as consulting_view2

app_name = "core"

urlpatterns = [
    path("consulting1/", board_view.MainView.as_view(), name="Main"),
    path("consulting2/", consulting_view.MainView.as_view(), name="Main"),
    path("consulting3/", consulting_view2.MainView.as_view(), name="Main"),
]
