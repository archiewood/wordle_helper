# this seems to be a file to put the routes in
import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# @app.route("/")
# def home_view():
#     return "<h1>Welcome to Wordle Helper!</h1>"

# dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

wordle_words = pd.read_csv('data/wordle_words.csv')
word_frequency = pd.read_csv('data/unigram_freq.csv')

wordle_words = wordle_words.merge(
    word_frequency).sort_values(by='count', ascending=False)


app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            brand="Wordle Helper",
            brand_href="#",
            color="primary",
            dark=True
        ),
        dbc.Container(
            [
                dbc.Row(

                    dbc.Col(children=[
                        html.Br(),
                        
                        html.Div(children='Beat your friends at Wordle.')],width=6),
                        justify='center'
                ),
                dbc.Row(
                    children=[
                        html.Div(children='Enter your first guess:'),

                        html.Br(),
                        dbc.Col(dbc.Input(id='letter0', placeholder='a',
                                          type='text', size="lg", className="mb-3", maxlength=1),width={"size": 1}), 
                        dbc.Col(dbc.Input(id='letter1', placeholder='a',
                                          type='text', size="lg", className="mb-3", maxlength=1),width={"size": 1}),
                        dbc.Col(dbc.Input(id='letter2', placeholder='a',
                                          type='text', size="lg", className="mb-3", maxlength=1),width={"size": 1}),
                        dbc.Col(dbc.Input(id='letter3', placeholder='a',
                                          type='text', size="lg", className="mb-3", maxlength=1),width={"size": 1}),
                        dbc.Col(dbc.Input(id='letter4', placeholder='a',
                                          type='text', size="lg", className="mb-3", maxlength=1),width={"size": 1})
                    ],
                    justify='center'
                ),
                dbc.Row(
                    children=[
                        html.Div(children='Select the colour of each letter:'),
                        html.Br(),
                        dbc.Col(dbc.DropdownMenu(id='result0',
                                                 label="Result",
                                                 children=[dbc.DropdownMenuItem("Green"), dbc.DropdownMenuItem("Yellow"), dbc.DropdownMenuItem("Grey")],),width={"size": 1}),
                        dbc.Col(dbc.DropdownMenu(id='result1',
                                                 label="Result",
                                                 children=[dbc.DropdownMenuItem("Green"), dbc.DropdownMenuItem("Yellow"), dbc.DropdownMenuItem("Grey")],),width={"size": 1}),
                        dbc.Col(dbc.DropdownMenu(id='result2',
                                                 label="Result",
                                                 children=[dbc.DropdownMenuItem("Green"), dbc.DropdownMenuItem("Yellow"), dbc.DropdownMenuItem("Grey")],),width={"size": 1}),
                        dbc.Col(dbc.DropdownMenu(id='result3',
                                                 label="Result",
                                                 children=[dbc.DropdownMenuItem("Green"), dbc.DropdownMenuItem("Yellow"), dbc.DropdownMenuItem("Grey")],),width={"size": 1}),
                        dbc.Col(dbc.DropdownMenu(id='result4',
                                                 label="Result",
                                                 children=[dbc.DropdownMenuItem("Green"), dbc.DropdownMenuItem("Yellow"), dbc.DropdownMenuItem("Grey")],),width={"size": 1}),
                    ],
                    justify='center'
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Table.from_dataframe(
                            wordle_words.head(),
                            id='table',
                            striped=True, bordered=True, hover=True
                        )))

            ],
            fluid=False,
            className="dbc"
        )
    ]
)
