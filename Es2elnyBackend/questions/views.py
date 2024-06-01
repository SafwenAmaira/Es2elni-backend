# questions/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
import random

class RandomQuestionAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        shuffled_questions = list(questions)
        random.shuffle(shuffled_questions)
        serializer = QuestionSerializer(shuffled_questions, many=True)
        return Response(serializer.data)
