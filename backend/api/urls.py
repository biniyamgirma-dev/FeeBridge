from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.accounts import MeView, RegisterView
from api.views.students import StudentListCreateView, StudentDetailView
from api.views.fees import FeeStructureListCreateView, FeeStructureDetailView, InvoiceListCreateView, InvoiceDetailView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('register/', RegisterView.as_view(), name='register'),
    
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    path('fee-structures/', FeeStructureListCreateView.as_view(), name='fee-structure-list-create'),
    path('fee-structures/<int:pk>/', FeeStructureDetailView.as_view(), name='fee-structure-detail'),

    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]