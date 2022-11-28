from rest_framework import serializers

from .models import Transaction
from utils.store import transactions_store, calculate_store



class TransactionSerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ["store", "currency", "transactions"]

    def get_transactions(self, store):
        return transactions_store(store)
    
    def get_currency(self, store):
        return calculate_store(store)
def get_store(store_name) -> list:
    store = list(store_name.values())[0]
    return Transaction.objects.filter(store=store)

def filter_store(stores) -> list:
    store_names = []
    store_unique = []

    for store in stores:
        if store.store not in store_names:
            store_names.append(store.store)

    for store_name in store_names:
        if store_name not in store_unique:
            store_unique.append({"store": store_name})

    return store_unique

def transactions_store(store_name) -> list:
    stores = get_store(store_name)
    transactions = []
    transactions_type = [
        {"1":"Débito"}, 
        {"2":"Boleto"}, 
        {"3":"Financiamento"}, 
        {"4":"Crédito"}, 
        {"5":"Recebimento Empréstimo"},
        {"6":"Vendas"},
        {"7":"TED"}, 
        {"8":"DOC"},
        {"9":"Aluguel"},
                        ]
    negative = [
        "2",
        "3",
        "9",
    ]
    
    for transaction in stores:
        for trasaction_type in transactions_type:
            if list(trasaction_type.keys())[0] == transaction.type:
                if transaction.type in negative:
                    transactions.append({"type": list(trasaction_type.values())[0], "value": round(-transaction.value,2),},)
                else:
                    transactions.append({"type": list(trasaction_type.values())[0], "value": round(transaction.value,2),},)

    return transactions

def calculate_store(store_name) -> float:
    stores = get_store(store_name)
    negative = [
        "2",
        "3",
        "9",
    ]

    sum = 0
    for transaction in stores:
        if transaction.type in negative:
            sum -= round(transaction.value, 2)
        else:
            sum += round(transaction.value, 2)

    return sum
