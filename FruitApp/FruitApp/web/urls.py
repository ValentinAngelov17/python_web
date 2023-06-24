from django.urls import path, include

from FruitApp.web.views import index, dashboard, fruit_edit, fruit_create, fruit_delete, fruit_details, profile_edit, \
    profile_details, profile_create, profile_delete

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', fruit_create, name='fruit create'),
    path('<int:pk>/', include([
        path('details/', fruit_details, name='fruit_details'),
        path('edit/', fruit_edit, name='fruit edit'),
        path('delete/', fruit_delete, name='fruit delete'),
    ])),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete')
    ]))
]
