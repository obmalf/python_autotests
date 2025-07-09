import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '77a42aecc770845d119bbe67e21463b8'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_creation = {
    "name": "generate",
    "photo_id": -1
}

# 1. Создаем покемона
response_post = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=body_creation)
print("POST /pokemons response:", response_post.text)

if response_post.status_code in (200, 201):
    try:
        data_post = response_post.json()
        pokemon_id = data_post.get('id') or data_post.get('pokemon_id')
        if not pokemon_id:
            print("Не удалось получить pokemon_id из ответа POST /pokemons")
        else:
            # 2. Изменяем покемона (PUT)
            body_change = {
                "pokemon_id": pokemon_id,
                "name": "generate",
                "photo_id": 2
            }
            response_put = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=body_change)
            print("PUT /pokemons response:", response_put.text)

            if response_put.status_code in (200, 201):
                try:
                    data_put = response_put.json()
                    # Предполагаем, что pokemon_id в ответе PUT такой же
                    pokemon_id_put = data_put.get('id') or data_put.get('pokemon_id') or pokemon_id
                    # 3. Добавляем покемона в покебол
                    body_add_pokeball = {
                        "pokemon_id": pokemon_id_put
                    }
                    response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_add_pokeball)
                    print("POST /trainers/add_pokeball response:", response_add_pokeball.text)

                except ValueError:
                    print("Ответ на PUT /pokemons не является JSON")
            else:
                print(f"Ошибка при изменении покемона: {response_put.status_code}")
    except ValueError:
        print("Ответ на POST /pokemons не является JSON")
else:
    print(f"Ошибка при создании покемона: {response_post.status_code}")

