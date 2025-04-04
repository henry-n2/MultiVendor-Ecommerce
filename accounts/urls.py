# from django.urls import path
# from . import views
# from django.conf.urls.static import static
# from django.conf import settings
# urlpatterns = [
#     path('user/register/', views.registration_view, name='registration_view'),
#     path('user/login/', views.login_view, name='user_login'),
#     path('user/dasboard/', views.user_dashboard, name='user_dashboard'),
#     path('user/profile/', views.user_profile, name='user_profile'),
#     path('user/logout/', views.user_logout, name='user_logout'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('user/register/', views.registration_view, name='registration_view'),
#     path('user/login/', views.login_view, name='user_login'),
#     path('user/dashboard/', views.user_dashboard, name='user_dashboard'),
#     path('user/profile/', views.user_profile, name='user_profile'),
#     path('user/logout/', views.user_logout, name='user_logout'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path,include
from . import views
urlpatterns = [
    path('user/register/', views.registration_view, name='registration_view'),
    path('user/login/', views.login_view, name='user_login'),
    path('user/dasboard/', views.user_dashboard, name='user_dashboard'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('',include("products.urls")),
]
