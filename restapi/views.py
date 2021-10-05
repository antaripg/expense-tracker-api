from django.shortcuts import render

# from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.


class ExpenseListCreate(ListCreateAPIView):
    """class ExpenseListCreate(ListCreateAPIView):
    def get(self, request):

        expenses = models.Expense.objects.all()
        serializer = serializers.Expense(expenses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = serializers.Expense(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)"""

    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()


class ExpenseRetrieveDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
