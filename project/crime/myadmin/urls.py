
from django.contrib import admin
from django.urls import path,include
from myadmin import views
urlpatterns = [
        path('dashboard/', views.dashboard, name='dashboard'),
        path('add_category/', views.add_category, name='add_category'),
        path('store_category/', views.store_category, name='store_category'),
        path('view_category/', views.view_category, name='view_category'),
        path('destroy_category/<int:id>', views.destroy_category, name='destroy_category'),
        path('edit_category/<int:id>', views.edit_category, name='edit_category'),
        path('update_category/<int:id>', views.update_category, name='update_category'),

       
        path('add_product/', views.add_product, name='add_product'),
        path('store_product/', views.store_product, name='store_product'),
        path('view_product/', views.view_product, name='view_product'),
        path('destroy_product/<int:id>', views.destroy_product, name='destroy_product'),
        path('edit_product/<int:id>', views.edit_product, name='edit_product'),
        path('update_product/<int:id>', views.update_product, name='update_product'),

        path('view_report/', views.view_report, name='view_report'),

        path('add_city/', views.add_city, name='add_city'),
        path('store_city/', views.store_city, name='store_city'),
        path('view_city/', views.view_city, name='view_city'),
        path('destroy_city/<int:id>', views.destroy_city, name='destroy_city'),
        path('edit_city/<int:id>', views.edit_city, name='edit_city'),
        path('update_city/<int:id>', views.update_city, name='update_city'),
        path('view_post_like/', views.view_post_like, name='view_post_like'),
        path('view_comment/', views.view_comment, name='view_comment'),
        path('destroy_comment/<int:id>', views.destroy_comment, name='destroy_comment'),

        path('view_user/', views.view_user, name='view_user'),
        path('destroy_user/<int:id>', views.destroy_user, name='destroy_user'),
        path('view_post/', views.view_post, name='view_post'),
        path('destroy_post/<int:id>', views.destroy_post, name='destroy_post'),

        path('destroy_post1/<int:id>', views.destroy_post1, name='destroy_post1'),
        path('view_inquiry/', views.view_inquiry, name='view_inquiry'),
        path('destroy_inquiry/<int:id>', views.destroy_inquiry, name='destroy_inquiry'),

        
        
        path('add_area/', views.add_area, name='add_area'),
        path('store_area/', views.store_area, name='store_area'),
        path('view_area/', views.view_area, name='view_area'),
        path('destroy_area/<int:id>', views.destroy_area, name='destroy_area'),
        path('edit_area/<int:id>', views.edit_area, name='edit_area'),
        path('update_area/<int:id>', views.update_area, name='update_area'),

        path('login/', views.login, name='login'),
        path('login_check/', views.login_check, name='login_check'),
        path('logout/', views.logout, name='logout'),

        path('forgot_password/', views.forgot_password, name='forgot_password'),
        path('register/', views.register, name='register'),

        path('view_Quickcontact/', views.view_Quickcontact, name='view_Quickcontact'),
        path('destroy_Quickcontact/<int:id>', views.destroy_Quickcontact, name='destroy_Quickcontact'),

        path('view_feedback/', views.view_feedback, name='view_feedback'),
        path('destroy_feedback/<int:id>', views.destroy_feedback, name='destroy_feedback'),
        # path('view_likes/', views.view_likes, name='view_likes'),
]
