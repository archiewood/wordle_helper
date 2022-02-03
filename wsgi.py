#whereas this file seems to be where you put any code / functions
import dash
from dash import dcc, html, dash_table, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import logging
from app.data_operations import *


from app.main import app
server = app.server     

if __name__ == "__main__":
        app.run_server(debug=True)

        
