from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', view=home),
    path('sobre/', view=sobre),
    path('contato/', view=contato)
]
