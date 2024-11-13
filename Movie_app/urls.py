from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('contact/', views.contact, name='contact'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('create/',views.create1,name='create'),
    path('view/',views.view,name='view'),
    path('delete/<int:id>/', views.delete_movie, name='delete_movie'),
    
    path('update/<int:id>/', views.update_movie, name='update_movie'),
    
]
# from django.urls import path,include
# from .views import movie_list, movie_detail, watchlist, add_to_watchlist

# urlpatterns = [
#     path('', views.movie_list, name='movie_list'),
#     path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
#     path('watchlist/', views.watchlist, name='watchlist'),
#     path('add_to_watchlist/<int:movie_id>/',views. add_to_watchlist, name='add_to_watchlist'),
# ]
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('Movie_app.urls')),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('signup/', views.signup, name='signup'),  # This requires creating a signup view
# ]
