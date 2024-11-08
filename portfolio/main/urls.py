from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('library-framework/<slug>/', views.LibraryFrameworkDetailView.as_view(), name='library-framework'),
    path('language/<slug>/', views.LanguageDetailView.as_view(), name='language'),
    path('project/<slug>/', views.ProjectDetailView.as_view(), name='project')
]