from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("",views.homepage,name="home"),
    path("Login/",views.Login,name="login"),
    path("Register/",views.register,name="register"),
    path('add/',views.addpost,name='add'),
    path('blog/', views.PostList, name='blog'),
    path('results/',views.search,name='results'),
    path('termsandconditions/',views.terms,name='terms'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('reset/',auth_views.PasswordResetView.as_view(),name='reset'),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
