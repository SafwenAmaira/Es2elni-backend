from django.urls import path
from questions.views import RandomQuestionAPIView
urlpatterns = [
    path('random-questions/', RandomQuestionAPIView.as_view(), name='random_questions'),
]
