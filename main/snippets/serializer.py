from typing_extensions import Required
from django.db.models.fields import IntegerField
from pygments import styles
from rest_framework import serializers

from main.snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=100, allow_blank=True, required = False)
    code = serializers.CharField(styles = {'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers(default='python')
    style = serializers.CharField(default='friendly', max_length=100)

    def create(self, validate_data):
        
        return Snippet.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.code = validate_data.get('code', instance.code)
        instance.linenos = validate_data.get('linenos', instance.linenos)
        instance.language = validate_data.get('language', instance.language)
        instance.style = validate_data.get('style', instance.style)
        instance.save()

        return instance

