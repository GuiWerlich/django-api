from django.urls import path
from .views import AccountFindView

urlpatterns = [
    path("accounts/", AccountFindView.as_view()),
]