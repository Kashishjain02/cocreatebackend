from mentorconnect.models import Applications
from rest_framework import routers, serializers, viewsets



class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = '__all__'
        # exclude = ['is_blocked','is_active','phone']

# class AccountSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Account
#         fields = '__all__'
#         # exclude = ['is_blocked','is_active','phone']

