from django.urls import path
from .views import(
    UserView,
    PostView
)

urlpatterns = [
    path("user/" , UserView.as_view() , name = "user"),
    path("post/" , PostView.as_view() , name = "post"),
]