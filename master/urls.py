from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('datatable', views.datatable_view, name='datatable'),
    path('institution_add', views.institution_add_view, name='institution_add'),
    path('institution_edit/<int:id>', views.institution_edit_view, name='institution_edit'),
    path('data_delete/<int:id>', views.data_delete_view, name='data_delete'),
    path('cource_view', views.cource_view, name='cource_view'),
    path('cource_add', views.cource_add_view, name='cource_add'),
    path('cource_edit/<int:id>', views.cource_edit_view, name='cource_edit'),
    path('cource_delete/<int:id>', views.cource_delete_view, name='cource_delete'),
    path('training_view', views.training_view, name='training_view'),
    path('training_add', views.training_add_view, name='training_add'),
    path('training_edit/<int:id>', views.training_edit_view, name='training_edit'),
    path('training_delete/<int:id>', views.training_delete_view, name='training_delete'),
    path('traininglead_view', views.traininglead_view, name='traininglead_view'),
    path('traininglead_add', views.traininglead_add_view, name='traininglead_add'),
    path('traininglead_edit/<int:id>', views.traininglead_edit_view, name='traininglead_edit'),
    path('traininglead_delete/<int:id>', views.traininglead_delete_view, name='traininglead_delete'),
    path('traininglead_followup/<int:id>', views.traininglead_followup_view, name='traininglead_followup'),

]
