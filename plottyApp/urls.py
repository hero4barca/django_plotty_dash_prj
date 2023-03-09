from django.urls import path
from . views import simple, scatter_graph, product_bar
from django.views.generic import TemplateView


urlpatterns = [

    path('home/', simple, name='home' ),
    path('plot_2/', scatter_graph, name='plot_2' ),
    path('plot_3/', product_bar , name='plot_3' ),
    path('plot_4/', TemplateView.as_view(template_name="plottyApp/interval_update.html"), name='plot_4'),

]