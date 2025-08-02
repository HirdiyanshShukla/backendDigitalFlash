from django.urls import path
from .views import SignupView, LoginView, LogoutView



urlpatterns = [

    path("signup/", SignupView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
]

# {
#     "username" : "JohnDoe",
#     "password" : "John@123"
# }


#SuperUser
#hirdiyanshshukla
#hirdiyansh123@