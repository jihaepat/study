from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import *
from .models import Snippet


class SnippetSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        # fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
        fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        # fields = ('id', 'username', 'snippets')
        fields = ('url', 'username', 'snippets')
