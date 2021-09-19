from django.urls import path
from . import views

app_name = 'formschapter'

urlpatterns = [
    path('cbv-form/',
         views.ClassBasedFormView.as_view(),
         name= 'cbv-form'),
    path('gcbv-form/',
         views.GenericFormView.as_view(),
         name= 'gcbv-form'),
    path('sub-unsub/',
         views.NewsletterView.as_view(),
         name='sub-unsub'),

    path('impdates/<int:pk>/',
         views.ImpDateDetail.as_view(),
         name="impdate-detail"),

    path('impdates/create/',
         views.ImpDateCreate.as_view(),
         name="impdate-create"),

    path('impdates/<int:pk>/edit/',
         views.ImpDateUpdate.as_view(),
         name="impdate-update"),

    path('impdates/<int:pk>/delete/',
         views.ImpDateDelete.as_view(),
         name="impdate-delete"),

    path('impdates/',
         views.ImpDateList.as_view(),
         name="impdate-list"),
]
