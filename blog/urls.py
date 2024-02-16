from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from baseapp import views as base_views

# router = DefaultRouter()
# router.register(r'user', base_views.CustomUserViewSet)

urlpatterns = [path('admin/', admin.site.urls),
               path('login/', TokenObtainPairView.as_view()),
               path('token/refresh/', TokenRefreshView.as_view()),
               path('registration/', base_views.CustomUserViewSet.as_view()),
               ]
