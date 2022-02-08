# this seems to be a file to put the routes in
import dash
from dash import dcc, html, dash_table, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import logging
from app.data_operations import *


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SUPERHERO],
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1"}],
                title="Wordle Companion",
                update_title=None)

app.css.config.serve_locally = True

wordle_words = pd.read_csv(
    'data/wordle_words.csv').sort_values(by='Frequency', ascending=False)

app.layout = html.Div(
    children=[
        dbc.NavbarSimple(
            brand="Wordle Companion",
            brand_href="#",
            color="primary",
            dark=True,
            className="mb-4"

        ),
        dbc.Container(
            [
                dbc.Row(

                    dbc.Col(children=[
                        html.H3(children='Beat your friends at Wordle'),
                    ], width='auto', class_name='mb-3'),

                    justify='center'
                ),

                dbc.Row(children=[
                    dbc.Col(
                        children=[
                            dbc.Row(
                                html.H4(children='First Guess', className='mb-1')),
                            dbc.Row(html.Div(
                                children='Enter your word, and the color for each letter below', className='mb-1')),
                            dbc.Row(
                                children=[
                                    dbc.Col(dbc.Input(id='letter'+str(i), placeholder='_',
                                                      type='text', size="lg", maxlength=1),) for i in range(5)
                                ],
                                justify='between', class_name='mb-1 g-2'
                            ),

                            dbc.Row(
                                children=[

                                    dbc.Col(dcc.Dropdown(id='result'+str(i)+'select',
                                                         options=[
                                                             {'label': 'Green',
                                                              'value': 'Green'},
                                                             {'label': 'Yellow',
                                                              'value': 'Yellow'},
                                                             {'label': 'Grey', 'value': 'Grey'}],
                                                         value='', className='dbc', placeholder='Pick', searchable=False)) for i in range(5)
                                ],
                                justify='center', class_name='mb-5 g-2'
                            )],


                        class_name='col-12 col-md-6'
                    ),

                    dbc.Col(
                        children=[html.H4('Remaining Words'),
                                  dbc.Alert([
                                      html.H4(
                                          format(wordle_words.shape[0], ','), id='num_words_remaining'),
                                      html.P(" possible words remaining")], color="secondary"),
                                  html.Div(id='table1')
                                  ],
                        class_name='col-12 col-md-6'
                    ),
                ]),


            ],
            fluid='sm',

            className="dbc"
        )
    ]
)


@ app.callback(
    [Output('table1', 'children'), Output('num_words_remaining', 'children')],
    [Input('letter0', 'value'),
     Input('letter1', 'value'),
     Input('letter2', 'value'),
     Input('letter3', 'value'),
     Input('letter4', 'value'),
     Input('result0select', 'value'),
     Input('result1select', 'value'),
     Input('result2select', 'value'),
     Input('result3select', 'value'),
     Input('result4select', 'value')]
)
def update_words_remaining(letter0, letter1, letter2, letter3, letter4, result0, result1, result2, result3, result4):
    if result0 == '':
        return [None, format(wordle_words.shape[0], ',')]
    guess=(str(letter0)+str(letter1)+str(letter2) +
             str(letter3)+str(letter4)).lower()
    result=[result0, result1, result2, result3, result4]
    filtered_df=update_possible_words(wordle_words, guess, result)
    return [dbc.Table.from_dataframe(filtered_df.iloc[:, 0:1].head(100)), format(filtered_df.shape[0], ',')]
