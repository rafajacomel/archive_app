from rest_framework import serializers

from api.models import Fix


class FixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fix
        fields = ('id', 'fspId', 'name',
                  'path', 'status',
                  'number_of_last_download',
                  'number_of_users')
