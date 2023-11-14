from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'contact_number', 'user_type', 'barangay', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            contact_number=validated_data['contact_number'],
            user_type=validated_data['user_type'],
            barangay=validated_data.get('barangay', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ReportSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(required=False)

    class Meta:
        model = Report
        fields = '__all__'
        
class AnnouncementSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    class Meta:
        model = Announcement
        fields = ['subject', 'description', 'date', 'barangay']

class AdminReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminReport
        fields = '__all__'

class AdminNaturalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNaturalReport
        fields = '__all__'