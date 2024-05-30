from auth_user import views
from django.urls import path,include

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',views.auth_logout,name='logout'),
    path('login/',views.auth_login,name='login'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
]
