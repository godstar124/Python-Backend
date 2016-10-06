# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'start_date', 'end_date', )


class AnswerSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ('id', 'question', 'user', 'response', 'created_at', )
