from django.urls import path, include
from . import views
from .views import GoogleLogin

app_name = 'accounts'

# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 번형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset/

urlpatterns = [
    path('profile/', views.user_information),
    path('profile/<username>/', views.information),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
