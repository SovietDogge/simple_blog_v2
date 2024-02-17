from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from baseapp import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'user', views.CustomUserDetailView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('registration/', views.CustomUserRegistrateView.as_view()),
    path('follow/', views.FollowsViewSet.as_view()),
    path('api/', include(router.urls))
]
