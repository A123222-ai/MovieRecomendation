from django.urls import path
from . import views
urlpatterns=[

    path('signup/',views.sign_up,name="signup"),
    path('login/',views.login_page,name="login_page"),
    path('logout/',views.logout_page,name='logout_page'),
    
    # path('create/',views.create,name='create')
]