from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from .serializers import ApiSerializer
from .mixin import mixin
from utils.normalize import normalize_file_txt
from utils.store import  filter_store

# Create your views here.

class ApiView(mixin, ListCreateAPIView):
    serializer_map = {
        "GET": TransactionSerializer,
        "POST": ApiSerializer,
    }

    def get_queryset(self):
        store = filter_store(Transaction.objects.all())
        return store

    def perform_create(self, _):
        uploaded_file = self.request.FILES["file_uploaded"]
        normalize_file_txt(uploaded_file)
