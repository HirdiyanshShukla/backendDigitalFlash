from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FlashCard, Deck, Subject
from .serializers import CardSerializer, DeckSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated


class cards(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            card = serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        flashcards = FlashCard.objects.filter(user=request.user).order_by('-created_at')  
        serializer = CardSerializer(flashcards, many=True)  
        return Response({"success": True, "data": serializer.data})


class deck(APIView):
     permission_classes = [IsAuthenticated]

     def get(self, request):
        decks = Deck.objects.filter(user=request.user)
        serializer = DeckSerializer(decks, many=True)
        return Response({"success": True, "data": serializer.data})

     def post(self, request):
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class subject(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, deck_id):
        subjects = Subject.objects.filter(deck_id=deck_id)
        serializer = SubjectSerializer(subjects, many=True)
        return Response({"success": True, "data": serializer.data})

    def post(self, request, deck_id):
        data = request.data.copy()
        data['deck'] = deck_id  # Inject deck_id into serializer data

        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # deck is already included
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)












        

