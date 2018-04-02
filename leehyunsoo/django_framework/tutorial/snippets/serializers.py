from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import *
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(ModelSerializer):
    # id = IntegerField(read_only=True)
    # title = CharField(required=False, allow_blank=True, max_length=100)
    # code = CharField(style={'base_template': 'textarea.html'})
    # linenos = BooleanField(required=False)
    # language = ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = ChoiceField(choices=STYLE_CHOICES, default='friendly')
    #
    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance



    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')