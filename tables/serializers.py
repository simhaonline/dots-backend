from rest_framework import serializers

from django.conf import settings as app_settings
from pymongo import MongoClient
from .models import Table


class TableSerializer(serializers.HyperlinkedModelSerializer):
    table_uuid = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField()
    url = serializers.HyperlinkedIdentityField(
        view_name='table-detail',
        lookup_field='table_uuid'
    )
    data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Table
        fields = '__all__'

    def get_data(self, obj):
        mongo_client = MongoClient(app_settings.MONGO_URI)
        db_client = mongo_client[app_settings.MONGO_DB_NAME]
        connection = db_client[obj.name.replace(' ', '_')]
        data = connection.find_one({'table_uuid': str(obj.table_uuid)})
        # temporarily delete _id property
        if data is not None:
            del data['_id']
        return data
