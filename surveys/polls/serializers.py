from rest_framework.serializers import ModelSerializer

from .models import Poll


class PollListSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'description',
            'date_start',
            'date_finish',
            'created_by']


class UpdatePollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'description',
            'created_by']


class CreateDestroyPollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = [
            'id',
            'title',
            'description',
            'date_start',
            'date_finish']

    def validate(self, attrs):
        # заполнение поля создателя опроса текущим пользователем
        attrs['created_by'] = self.context['request'].user
        return attrs
