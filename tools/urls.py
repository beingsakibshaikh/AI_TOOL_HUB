from django.urls import path
from . import views

urlpatterns = [
    path('', views.tool_list,name='tool_list'),
    path('tool/<int:tool_id>/', views.tool_detail, name='tool_detail'),
    path('categories/', views.categories_page, name='categories_page'),
    path('categories/<slug:slug>/', views.tools_by_category, name='category_tools'),
    path('tutorials/', views.tutorials_page, name='tutorials_page'),
    path('tutorials/<int:pk>/', views.tutorial_detail, name='tutorial_detail'),
    path('about/', views.about_page, name='about_page'),
]



