from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return JsonResponse({"error": "Username and password required."}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already taken."}, status=400)

    User.objects.create_user(username=username, password=password)
    return JsonResponse({"message": "User registered successfully."})


class LoginView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse({"error": "Username and password required."}, status=400)

        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({"error": "Invalid credentials."}, status=401)

        login(request, user)
        return JsonResponse({"message": "User logged in successfully."})
