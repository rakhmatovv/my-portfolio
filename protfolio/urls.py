from django.urls import path
from . import views
urlpatterns = [
    path('',views.index , name = 'home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('credentials/', views.CredentialsView.as_view(), name='credentials'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('work/<slug:slug>/', views.WorkDetailView.as_view(), name ='work_detail'),
    path('contact/', views.ContactView.as_view(),name='contact'),
    path('service/', views.ServiceView.as_view(), name = 'service'),
]
