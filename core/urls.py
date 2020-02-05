from django.urls import path
from core.views import index
from core.views import contato


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contato',contato,name='contato'),
    
]