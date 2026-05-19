from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True, min_length= 8, style={'input_type':'password'}) #only to write, not to see
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data) #create_user hashes the password, hasking : converting the into hsing, hs: create a group of hash characters into format, (its a one way funct)
            return user
        

