from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, ObtainTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # create token for registered user to using Simple JWT
            refersh = RefreshToken.for_user(user)
            access = refersh.access_token

            return Response({
                "user": UserSerializer(user).data,
                "refresh": str(refersh),
                "access": str(access),
                "message" : "User registered successfully"
                }, 
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenView(GenericAPIView):
    serializer_class = ObtainTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": {
                "username": user.username,
            },
            "refresh" : str(refresh),
            "access": str(refresh.access_token),
            "message": "Token generated successfully"
        }, status=status.HTTP_200_OK)

