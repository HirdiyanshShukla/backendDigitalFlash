from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken


class SignupView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "Username and password required."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=400)

        user = User.objects.create_user(username=username, password=password)
        access_token = AccessToken.for_user(user)

        return Response({
            "success": True,
            "username": user.username,
            "access": str(access_token)
        }, status=201)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            access_token = AccessToken.for_user(user)
            return Response({
                "success": True,
                "access": str(access_token),
                "username": user.username
            })
        return Response({"error": "Invalid credentials"}, status=401)


class LogoutView(APIView):
    def post(self, request):
        # With JWT, logout is client-side (just delete the token)
        return Response({"success": True, "message": "Logged out"})
