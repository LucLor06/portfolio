from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('library+framework/<pk>/', views.LibraryFrameworkDetail.as_view(), name='library_framework'),
    path('language/<pk>/', views.LanguageDetail.as_view(), name='language'),
    path('project/<pk>/', views.ProjectDetail.as_view(), name='project')
]