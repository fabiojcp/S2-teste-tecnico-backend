from rest_framework.serializers import Serializer, FileField


class ApiSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = "__all__"
