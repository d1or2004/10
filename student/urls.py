from django.urls import path
from .views import StudentView
from .views import LendingWive, UserRigisterView, LoginView,LogoutView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student'),
    path('', LendingWive.as_view(), name='landing'),
    path('auth/register/', UserRigisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
