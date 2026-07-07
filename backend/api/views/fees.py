from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from fees.models import FeeStructure, Invoice
from api.serializers.fees import FeeStructureSerializer
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