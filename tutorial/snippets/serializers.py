from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")  # new

    class Meta:
        model = Snippet
        fields = (
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        )  # new


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "snippets")
        ##Создали сериализатор, он использует нашу модель и выводит поля таблицы