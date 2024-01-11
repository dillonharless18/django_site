from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # Created my own url and view to ensure I understand how dynamic urls work
    # Will reverse the detail of the question and choise text
    path("reverse/", views.reverse, name="reverse"),
]