from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# router = DefaultRouter()
# router.register(r'user', base_views.FollowersViewSet)

urlpatterns = [path('admin/', admin.site.urls),
               path('', include('baseapp.urls'))
               ]
