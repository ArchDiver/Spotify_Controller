from rest_framework import serializers
from .model import room

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomSerializer
        fields = ('id', 'code', 'host', 'guest_can_pause',
                    'votes_to_skip', 'created_at')
