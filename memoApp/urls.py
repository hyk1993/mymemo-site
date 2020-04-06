from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="mainPage"),
    path('control/', views.control, name="controlPage"),
    path('control/create', views.create, name="createHabbit"),
    path('control/delete', views.delete, name="deleteHabbit"),
    path('control/order', views.order),
    path('order/', views.ordered),
    path('check/', views.check),
    path('control/fix', views.fix),
    path('refresh/', views.refresh),
    path('record/', views.record, name='recordPage'),
    path('record/deleteRecord/', views.deleteRecord),
    path('<str:habbit_id>/', views.memo, name='memoPage'),
    path('<str:habbit_id>/memoPage/', views.memoPage),
    path('<str:habbit_id>/delete/', views.deleteMemo)
]