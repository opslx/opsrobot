from django.urls import path,include
from backend.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path(r'add_book', BookViewSet.as_view(), ),
    path(r'book/<str:book_name>', BookView.as_view(), ),
    path(r'show_books', ShowBooksViewSet.as_view(), ),
    # 认证令牌
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新令牌
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]