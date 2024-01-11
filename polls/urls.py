from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # Created my own url and view to ensure I understand how dynamic urls work
    # Mirrors the question list text - did this halfway through Chapter 3
    path("mirrored-questions/", views.mirrored_questions, name="mirrored-questions"),
]