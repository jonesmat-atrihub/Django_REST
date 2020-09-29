from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Snippet


class SnippetSerializer( serializers.ModelSerializer ):
    owner = serializers.ReadOnlyField( source='owner.username' )
    highlight = serializers.HyperlinkedIdentityField( view_name='snippet-highlight', format='html' )

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer( serializers.ModelSerializer ):
    snippets = serializers.PrimaryKeyRelatedField( many=True, queryset=Snippet.objects.all() )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets', ]
