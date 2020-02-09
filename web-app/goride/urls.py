from django.contrib import admin
from django.urls import path
from . import views
from .views import (
	CurrentView, 
	RideListView, 
	RideDetailView, 
	RideCreateView, 
	RideUpdateView, 
	RideDeleteView,
	DriveListView, 
	SearchView,
	tryShare,
	JoinView,
	ShareDeleteView,
	SuccessQuitView,
	completeView,
	PickupView)
from users import views as user_views

urlpatterns = [

	#path('home/', RideListView.as_view(), name='goride-home'),
    path('current/', CurrentView, name='current'),
    path('', user_views.rider_register, name='rider_register'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('about/', views.about, name='goride-about'),
    path('ride/new/', RideCreateView.as_view(), name='ride-create'),
    path('ride/<int:pk>/update', RideUpdateView.as_view(), name='ride-update'),
    path('ride/<int:pk>/delete', RideDeleteView.as_view(), name='ride-delete'),
    path('share/<int:pk>/delete', ShareDeleteView, name='share-delete'),
    path('share/', tryShare, name='share'),
    path('drive/', DriveListView.as_view(), name='drive'),
    path('success-join/<int:pk>/', JoinView, name='join'),
    path('success-pickup/<int:pk>/', PickupView, name='pickup'),
    path('success-quit/<int:pk>/', SuccessQuitView, name='success-quit'),
    path('complete/<int:pk>/', completeView, name='complete'),
    path('user/<int:pk>/update', user_views.UserUpdateView.as_view(), name='user-update'),
    path('user/success-update', user_views.SuccessUpdateView, name='success-update'),
 
]

