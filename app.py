######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['happy', 'sad', 'excited', 'indifferent', 'bored', 'angry','other']
images=['happy.jpg','sad.png','excited.png','indifferent.png','bored.png','angry.png','other.png']
githublink = 'https://github.com/purnimavenkatram/chuck_norris_execution'
image1='mood.jpg'
heading1='My mood today !'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='I''m feeling'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=app.get_asset_url(image1), style={'width': '500', 'height': '500'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices],
                value='happy',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'I''m feeling {whatever_you_chose}'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
