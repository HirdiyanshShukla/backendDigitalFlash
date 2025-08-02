from rest_framework import serializers
from .models import FlashCard, Deck, Subject


class DeckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck
        fields = '__all__'
        read_only_fields = ['user']



class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'



class CardSerializer(serializers.ModelSerializer):
    deck = serializers.CharField(write_only=True) #used only when writing data
    subject = serializers.CharField(write_only=True)
    deck_name = serializers.CharField(source='deck.name', read_only=True) #used only when reading data
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = FlashCard
        fields = [
            'id', 'question', 'answer', 'difficulty', 'created_at',
            'deck', 'subject',           # for POST (write-only)
            'deck_name', 'subject_name'  # for GET (read-only)
        ]
    def create(self, validated_data):

        deck_name = validated_data.pop('deck')
        subject_name = validated_data.pop('subject')
        
        user = self.context['request'].user

        deck, _ = Deck.objects.get_or_create(name=deck_name.lower(), user=user)

        subject, _ = Subject.objects.get_or_create(name=subject_name.lower(), deck=deck)




        return FlashCard.objects.create(
            user=user,
            deck=deck,
            subject=subject,
            **validated_data
        )
