from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from polls.constants import ANSWER_WITH_ONE_OPTION, ANSWER_WITH_SEVERAL_OPTIONS
from polls.models import Poll, Question
from .models import Questionnaire


class QuestionnairesSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = [
            'text',
            'user',
            'answers_data']

    def validate(self, attrs):
        attrs['user'] = None if self.context['request'].user.is_anonymous else self.context['request'].user
        poll = attrs['poll']
        question_list = poll.question_set.all()
        answers = attrs['answers_data']

        for question in  question_list:
            answer = answers[question.id]
            if question.type == ANSWER_WITH_ONE_OPTION:
                if answer not in question.variants:
                    raise serializers.ValidationError('Invalid answers')
            if question.type == ANSWER_WITH_SEVERAL_OPTIONS:
                answer_set, variants_set = set(answer), set(question.variants)
                if not answer_set.issubset(variants_set):
                    raise serializers.ValidationError('Invalid answers')

        question_list_ids = list(answers.keys())
        if set(question_list_ids) != set(question_list):
            raise serializers.ValidationError('Invalid answers')
        return attrs

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class TakePollSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'description',
            'date_start',
            'date_finish',
            'questions',
            'created_by']
