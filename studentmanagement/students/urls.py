from django.urls import path
from .views import *

urlpatterns=[
    path('signup',SignUpview.as_view(),name='signup'),
    path('landing',LandingView.as_view(),name='landing'),
    path('add',AddStudentView.as_view(),name='add'),
    path('view',ViewStudentsView.as_view(),name='view'),
    path('edit/<int:id>',EditStudentView.as_view(), name='edit'),
    path('delete/<int:id>',DeleteStudentView.as_view(), name='delete'),
]