from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd
from django_plotly_dash import DjangoDash

from .models import Product

app = DjangoDash("ProductPlot")

app.layout = html.Div(
     [
        html.Div(
            children=[
                html.Label("Products"),
                dcc.Dropdown(
                    id="pid",
                ),
            ],
            style={"padding": 10, "flex": 1},
        ),
        html.Div(id="gr_container", children=[]),
        html.Br(),
        dcc.Graph(id="pro_graph", figure={}),
    ],
)

@app.callback(
    [
        Output(component_id="pid", component_property="options"),
        Output(component_id="pro_graph", component_property="figure"),
        Output(component_id="gr_container", component_property="children"),
    ],
    [
        Input(component_id="pid", component_property="value"),
    ],
)
def update_graph(selected):
    products = Product.objects.all()
    name_list = list(products.values_list("name", flat=True))
    price_list = list(products.values_list("price", flat=True ))
    qty_list = list(products.values_list("stock_qty", flat=True ))


    dictionary = {}
    dictionary["name"] = name_list
    dictionary["price"] = price_list
    dictionary["quantity"] = qty_list
    opts = ["price", "quantity"]

    message = "Graph shows product data"
    # fig = px.bar(dictionary, x="name", y=selected)

    if selected == "price":        
        fig = px.bar(dictionary, x="name", y="price")
        message = "Graph shows product price"
    else:
        fig = px.bar(dictionary, x="name", y="quantity")
        message = "Graph shows product qunatity"

    return opts, fig, message

