import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '77a42aecc770845d119bbe67e21463b8'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '36554'  # замените на ваш trainer_id

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', headers=HEADERS, params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url=f'{URL}/pokemons', headers=HEADERS, params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == Obmalf