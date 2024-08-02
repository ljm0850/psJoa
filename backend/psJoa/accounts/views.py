from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.contrib.auth import get_user_model
from .models import CustomUser
from .serializers import MyInfoSerializers,YourInfoSerializers
from rest_framework import status

@api_view(['GET'])
def getProfile(request):
    # if not request.user.is_authenticated:
    #     return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    request_user = request.GET.get("you")
    if not request_user:
        return Response({'detail': 'Bad Request: "you"파라미터 필요'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(CustomUser, username=request_user)
    
    if request_user == request.user.username:
        userserializer = MyInfoSerializers(user)
        print("내 프로필")
    else:
        userserializer = YourInfoSerializers(user)
        print("타인 프로필")
    return Response(userserializer.data, status=status.HTTP_200_OK)