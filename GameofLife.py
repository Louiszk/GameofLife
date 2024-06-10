import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

GRID_SIZE = 20

def create_board():
    return np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("Conway's Game of Life"), className="text-center mt-4")),
        dbc.Row(
            dbc.Col(
                dcc.Graph(figure = go.Figure(data = go.Heatmap(z = np.zeros((20, 20)))), id='game-board', config={'displayModeBar': False}),
                width={"size": 6, "offset": 3}
            )
        ),
        dbc.Row(
            dbc.Col(
                dbc.Button("Start", id='start-button', className="mt-4"),
                className="text-center"
            )
        ),
        dcc.Interval(id='interval', interval=500, n_intervals=0, disabled=True),
    ],
    className="mt-4"
)

@app.callback(
    Output('game-board', 'figure'),
    Input('game-board', 'clickData'),
    State('game-board', 'figure')
)
def update_board(click_data, figure):
    board = np.array(figure['data'][0]['z'])
    if click_data:
        point = click_data['points'][0]
        board[point['y']][point['x']] = 1 if board[point['y']][point['x']] == 0 else 0
    return create_figure(board)

@app.callback(
    Output('interval', 'disabled'),
    Input('start-button', 'n_clicks'),
    State('interval', 'disabled')
)
def start_game(n_clicks, interval_disabled):
    if n_clicks:
        return not interval_disabled
    return interval_disabled

@app.callback(
    Output('game-board', 'figure', allow_duplicate=True),
    Input('interval', 'n_intervals'),
    State('game-board', 'figure'),
    prevent_initial_call=True
)
def update_generation(n_intervals, figure):
    board = np.array(figure['data'][0]['z'])
    new_board = step(board)
    return create_figure(new_board)

def step(board):
    new_board = np.copy(board)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            alive_neighbors = np.sum(board[max(0, i-1):min(i+2, board.shape[0]), max(0, j-1):min(j+2, board.shape[1])]) - board[i, j]
            if board[i, j] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                new_board[i, j] = 0
            elif board[i, j] == 0 and alive_neighbors == 3:
                new_board[i, j] = 1
    return new_board

def create_figure(board):
    return {
        'data': [go.Heatmap(
            z=board,
            colorscale='Greys',
            showscale=False
        )],
        'layout': go.Layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            margin=dict(t=10, b=10, l=10, r=10)
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
