import requests  # Send request and get data back from API
from flask import Flask, render_template, request

url = 'https://api.fortnitetracker.com/v1/profile/pc/{}'  # API

headers = {'TRN-Api-Key': '11a816b0-ed9c-462d-a50d-2970e1164a58'}

# res = requests.get(url, headers=headers)  # Send a request to fortnite tracker and the result are returned in r
# result = (res.json()['lifeTimeStats'])  # returning json data to further convert them into list and dictionary

app = Flask(__name__, template_folder='C:\\Data Science\\python\\python_projects\\Fortnite_Stats_Comparison\\templates')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    player1 = None
    player2 = None
    player1_stats = {}
    player2_stats = {}

    if request.method == "POST":
        player1 = request.form.get('player1name')
        if player1:
            player2 = request.form.get('playername')
        else:
            player1 = request.form.get('playername')

        player1_result = requests.get(url.format(player1), headers=headers).json()['lifeTimeStats']
        player1_stats = player_data(player1_result)

        if player2:
            player2_result = requests.get(url.format(player2), headers=headers).json()['lifeTimeStats']
            player2_stats = player_data(player2_result)

    return render_template('home.html', player1=player1, player2=player2, player1_stats=player1_stats, player2_stats=player2_stats)


def player_data(api_data):
    temp_dict = {}

    for i in api_data:
        if i['key'] == 'Wins':
            temp_dict['Wins'] = i['value']
        if i['key'] == 'Win%':
            temp_dict['Win%'] = i['value']
        if i['key'] == 'Kills':
            temp_dict['Kills'] = i['value']
        if i['key'] == 'K/d':
            temp_dict['K/D'] = i['value']
        if i['key'] == 'Matches Played':
            temp_dict['Matches Played'] = i['value']

    return temp_dict

# print(player_data(result))


if __name__== '__main__':
    app.run(debug=True)
