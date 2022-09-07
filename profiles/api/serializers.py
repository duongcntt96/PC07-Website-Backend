from rest_framework import serializers
from profiles.models import Team, UserProfile
from django.contrib.auth.models import User, Group


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    member = UserProfileSerializer(
        source='UserProfile_set', many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username', 'email',
        #   'date_joined', 'groups', 'team_set']
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_username(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'Tên đăng nhập quá ngắn')
        return value

    def validate_first_name(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'Vui lòng nhập đầy đủ họ và tên')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'Mật khẩu phải dài từ 6 ký tự trở lên')
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()
        return user
