from account.models import Startup,Mentor,Account
from rest_framework import routers, serializers, viewsets


class StartupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Startup
        fields = '__all__'
        # exclude = ['debate_pros','comment','proslike']


class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        # fields = '__all__'
        exclude = ['is_blocked','is_active','phone']

# class AccountSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Account
#         fields = '__all__'
#         # exclude = ['is_blocked','is_active','phone']

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id','email', 'password', 'contact_number', 'name')
        # fields = '__all__'

    # def validate_password(self, password):
    #     try:
    #         validate_password(password)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(str(e))
    #     return password

    def create(self, validated_data):
        user = Account.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            contact_number=validated_data.get('phone', ''),
            name=validated_data.get('name', ''),
        )
        print(user.id)
        return user 