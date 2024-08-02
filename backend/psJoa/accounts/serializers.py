from .models import CustomUser
from rest_framework import serializers

class MyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class YourInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','id')


# {
#     "id": 3,
#     "password": "pbkdf2_sha256$720000$TRtf83mxcXrxw9SIKBCv6I$pCqYRf1yqPe2kzOkQrchcQVJrDnvC5dHZbNJ03c3gZo=",
#     "last_login": "2024-07-08T10:53:37.894529Z",
#     "is_superuser": false,
#     "username": "psjoa111",
#     "first_name": "",
#     "last_name": "",
#     "is_staff": false,
#     "is_active": true,
#     "date_joined": "2024-07-08T10:53:37.700576Z",
#     "email": "",
#     "groups": [],
#     "user_permissions": []
# }