from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from fees.models import FeeStructure, Invoice
from api.serializers.fees import FeeStructureSerializer, InvoiceSerializer
from api.permissions import IsStaffOrAdmin, IsAdmin

class FeeStructureListCreateView(ListCreateAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    permission_classes = [IsStaffOrAdmin]


class FeeStructureDetailView(RetrieveUpdateDestroyAPIView):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdmin()]
        return [IsStaffOrAdmin()]


class InvoiceListCreateView(ListCreateAPIView):
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsStaffOrAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'PARENT':
            return Invoice.objects.filter(student__parent=user)
        return Invoice.objects.all()


class InvoiceDetailView(RetrieveUpdateAPIView):
    serializer_class = InvoiceSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            return [IsStaffOrAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'PARENT':
            return Invoice.objects.filter(student__parent=user)
        return Invoice.objects.all()