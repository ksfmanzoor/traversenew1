from rest_framework import serializers
from .models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class RegisterUserSerializer(serializers.ModelSerializer):

        def validate(self, data):
            # here data has all the fields which have validated values
            # so we can create a User instance out of it
            user = User(**data)

            # get the password from the data
            password = data.get('password')

            errors = dict()
            try:
                # validate the password and catch the exception
                validators.validate_password(password=password, user=User)

            # the exception raised here is different than serializers.ValidationError
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)

            return super(RegisterUserSerializer, self).validate(data)

        def create(self, validated_data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Snippet` instance, given the validated data.
            """
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.date_posted = validated_data.get('date_posted', instance.date_posted, blank=True)
            instance.author = validated_data.get('author', instance.author)
            instance.image = validated_data.get('image', instance.image)
            instance.save()
            return instance

