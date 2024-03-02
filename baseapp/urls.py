from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from baseapp import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user', views.CustomUserDetailView)

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/registration/', views.CustomUserRegistrateView.as_view()),
    path('api/', include(router.urls)),
]
