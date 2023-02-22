from django.urls import path
from . views import simple, scatter_graph, product_bar

urlpatterns = [

    path('home/', simple, name='home' ),
    path('plot_2/', scatter_graph, name='plot_2' ),
    path('plot_3/', product_bar , name='plot_3' ),

]