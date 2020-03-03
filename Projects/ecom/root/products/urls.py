from django.urls import path
from .views import *

urlpatterns = [
    #function based view call
    path('list/',productlistview,name='list'),
    #class based view call
    path('cbvlist/',ProductListViewcbv.as_view(),name='cbv'),
    #function based detail view
    # path('<int:pk>/',productdetailview,name='detail'),
    #class based detail view
    path('cb/<int:pk>/',ProductListViewcb.as_view(),name='cbdetail'),
    #functoin based detail view with slug generation
    path('<str:slug>/',productdetailview,name='detail'),
    #class based detail view with auto slug generation
    path('cb/<str:slug>/',ProductListViewcb.as_view(),name='cbdetail'),
    path('featured',featuredlist,name='featuredlist')
 
]