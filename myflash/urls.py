
from django.urls import path, include
from .views import cards, subject, deck

urlpatterns = [
    path('card/', cards.as_view(), name='card'),
    path('deck/', deck.as_view(), name='deck'),
    path('subject/', subject.as_view(), name='subject')

]

# {
#     "username" : "JohnDoe",
#     "password" : "John@123"
# }