from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from baseapp import views as base_views

# router = DefaultRouter()
# router.register(r'user', base_views.FollowersViewSet)

urlpatterns = [path('admin/', admin.site.urls),
               path('login/', TokenObtainPairView.as_view()),
               path('token/refresh/', TokenRefreshView.as_view()),
               path('registration/', base_views.CustomUserRegistrateView.as_view()),
               path('follow/', base_views.FollowsViewSet.as_view())
               ]
