# this seems to be a file to put the routes in
from pydoc import classname
from click import style
import dash
from dash import dcc, html, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import logging
from app.data_operations import *

meta_tags = [
    {"name": "viewport",
        "content": "width=device-width, initial-scale=1"
     },
    {
        "name": "author",
        "content": "Archie Wood"
    },
    {
        "name": "description",
        "content": "An app to help you win Wordle in fewer guesses.",
    },
    {
        "property": "og:type",
        "content": "website"
    },
    {
        "property": "og:title",
        "content": "Beat your friends at Wordle"
    },
    {
        "property": "og:description",
        "content": "An app to help you win Wordle in fewer guesses.",
    },
    {
        "property": "og:image",
        "content": "https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fbd080d8-eeb3-485c-9a13-87bcec77647e_603x599.png"
    },
    {
        "property": "twitter:title",
        "content": "Beat your friends at Wordle"
    },
    {
        "property": "twitter:description",
        "content": "An app to help you win Wordle in fewer guesses.",
    },
    {
        "property": "twitter:image",
        "content": "https://bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/fbd080d8-eeb3-485c-9a13-87bcec77647e_603x599.png",
    },
]


app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SANDSTONE],
                meta_tags=meta_tags,
                title="Wordle Companion",
                update_title=None,
                )

app.css.config.serve_locally = True


app.index_string = '''<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-1XTZ6F0JH1"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            
            gtag('config', 'G-1XTZ6F0JH1', { 'anonymize_ip': false });
        </script>
        <script>
            !function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"];analytics.factory=function(e){return function(){var t=Array.prototype.slice.call(arguments);t.unshift(e);analytics.push(t);return analytics}};for(var e=0;e<analytics.methods.length;e++){var key=analytics.methods[e];analytics[key]=analytics.factory(key)}analytics.load=function(key,e){var t=document.createElement("script");t.type="text/javascript";t.async=!0;t.src="https://cdn.segment.com/analytics.js/v1/" + key + "/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(t,n);analytics._loadOptions=e};analytics._writeKey="5Sc81VlUXwW6TO3EuJbW7MBb8DdSxJCw";;analytics.SNIPPET_VERSION="4.15.3";
            analytics.load("5Sc81VlUXwW6TO3EuJbW7MBb8DdSxJCw");
            analytics.page();
            }}();
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>'''

wordle_words = pd.read_csv(
    'data/wordle_words_short.csv').sort_values(by='Frequency', ascending=False)


def create_guess_input(guess_number):
    return dbc.Col(
        children=[
            dbc.Row(children=[
                html.Div(children=[
                    html.H4(children=['Guess '+str(guess_number)],
                            className='mb-1'),
                    html.H6(' (Optional)') if guess_number > 1 else None], className='mb-1'
                ),

            ], ),

            dbc.Row(
                children=[
                    # dbc.Col(dbc.Input(id='letter'+str(i)+'_guess'+str(guess_number), placeholder='A',
                    dbc.Col(dbc.Input(id={'component': 'guess_input', 'letter_position': i, 'guess_number': guess_number}, placeholder='A',
                                      type='text', size="lg", maxlength=1, value='')) for i in range(5)
                ],
                justify='between', class_name='mb-1 g-2'
            ),

            dbc.Row(
                children=[

                    dbc.Col(dcc.Dropdown(id={'component': 'result_selector', 'letter_position': i, 'guess_number': guess_number},
                                         # dbc.Col(dcc.Dropdown(id='result'+str(i)+'select_guess'+str(guess_number),

                                         options=[
                            {'label': 'Green',
                             'value': 'Green'},
                            {'label': 'Yellow',
                             'value': 'Yellow'},
                            {'label': 'Grey', 'value': 'Grey'}],
                        value='', className='dbc', placeholder='', searchable=False, clearable=False)) for i in range(5)
                ],
                justify='center', class_name='mb-3 g-2'
            )
        ],
        #class_name='col-12 col-md-6'
    )


app.layout = html.Div(
    children=[
        dbc.NavbarSimple(children=[
            dbc.NavItem(dbc.NavLink('Why Wordle Companion?',
                        href="https://archiewood.substack.com/p/how-to-win-wordle")),
            dbc.NavItem(dbc.NavLink('Github', href="https://github.com/archiewood/wordle_helper")),
            dbc.NavItem(dbc.NavLink('Request A Feature',
                        href="https://research.typeform.com/to/FV3AUx2P"))],
            brand="WORDLE COMPANION",
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
                dbc.Row(

                    dbc.Col(children=[
                        dcc.Markdown(
                            children='''
                            Enter guesses and colors below to see possible solutions. 
                            
                            **Want more from Wordle Companion?** [Let me know](https://research.typeform.com/to/FV3AUx2P) how to improve it.
                            '''),
                    ], width='auto', class_name='mb-3'),


                    justify='center'
                ),

                dbc.Row(
                    children=[

                        dbc.Col(
                            children=[
                                create_guess_input(i) for i in range(1, 6)],
                            class_name='col-12 col-md-6'),

                        dbc.Col(
                            children=[

                                dbc.Row(html.Div([html.H4('Remaining Words'), html.H6(
                                    ' (Top 50 Shown)')]), className='mb-2'),
                                dbc.Alert([
                                          html.H4(
                                              format(wordle_words.shape[0], ','), id='num_words_remaining'),
                                          html.P(" possible words remaining")], color="secondary"),
                                html.Div(id='table1'),
                                dbc.Row(html.Div([html.H4('Top Letters in Words'), html.H6(
                                    ' (Top 10 Shown)')]), className='mb-2'),
                                html.Div(id='letters_table'),
                            ],
                            class_name='col-12 col-md-6'
                        ),
                    ]),


            ],
            fluid='sm',

            className="dbc col-12 col-sm-8"
        ),
        html.Footer(
            dbc.Row(
                dbc.Col("Made with ?????? in Toronto", width='auto', class_name='mb-1 mt-1'), justify='center'), className='bg-light'
        )
    ]
)


@app.callback(
    Output({'component': 'guess_input', 'letter_position': MATCH,
           'guess_number': MATCH}, 'style'),
    Input({'component': 'result_selector',
          'letter_position': MATCH, 'guess_number': MATCH}, 'value')
)
def update_color(result_selector):
    if result_selector == '':
        return {'background-color': result_selector, 'color': 'black'}
    elif result_selector == 'Green':
        return {'background-color': '#6aaa64', 'color': 'white'}
    elif result_selector == 'Yellow':
        return {'background-color': '#c9b458', 'color': 'white'}
    elif result_selector == 'Grey':
        return {'background-color': '#86888a', 'color': 'white'}


@ app.callback(
    [Output('table1', 'children'), Output('num_words_remaining', 'children')],
    [Input({'component': 'guess_input', 'letter_position': ALL, 'guess_number': ALL}, 'value'),
     Input({'component': 'result_selector', 'letter_position': ALL, 'guess_number': ALL}, 'value')]
)
def update_words_remaining(guess_input, result_selector):
    current_word_list = wordle_words

    guess = []
    for letter in guess_input:
        if letter == '':
            guess.append('*')
        else:
            guess.append(letter.lower())

    filtered_df = update_possible_words(wordle_words, guess, result_selector)
    return [dbc.Table.from_dataframe(filtered_df.iloc[:, 0:1].head(50), striped=True), format(filtered_df.shape[0], ',')]


@ app.callback(
    Output('letters_table', 'children'),
    [Input({'component': 'guess_input', 'letter_position': ALL, 'guess_number': ALL}, 'value'),
     Input({'component': 'result_selector', 'letter_position': ALL, 'guess_number': ALL}, 'value')]
)
def update_letters_remaining(guess_input, result_selector):
    current_word_list = wordle_words

    guess = []
    for letter in guess_input:
        if letter == '':
            guess.append('*')
        else:
            guess.append(letter.lower())

    filtered_df = update_possible_words(wordle_words, guess, result_selector)
    return dbc.Table.from_dataframe(count_most_frequent_letters(filtered_df).head(10), index=True, striped=True)
