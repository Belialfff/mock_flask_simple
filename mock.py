# импорты
from flask import Flask, jsonify, request
from datetime import datetime
import uuid
import string
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # выключаем сортировку ключей по алфавиту

# обработчик запросов по методу POST и PATH /api/json/
@app.route('/api/json/<id>', methods=['POST'])
def json_post(id):
    # для POST запроса парсим каждое поле, запиысывая его в отдельные переменные
    request_data = request.get_json() # вытаскиваем в переменную наш запрос
    friends = request_data["friends"] # отдельно достаём список друзей
    guid = uuid.uuid1() # рандомный uuid
    debitBalance = request_data["debitBalance"] # баланс1
    creditBalance = request_data["creditBalance"] # баланс2
    phone = request_data ["phone"] # номер телефона
    registered = request_data["registered"] # регистрация
    is_active = bool(request_data) # состояние
    # многие переменные тут НЕОБЯЗАТЕЛЬНЫ, но пригодятся в случае масштабирования кода. Код интерпретируется и неиспользуемые переменные не занимают память
        
    # собираем ответ из ключей и их значений
    response = {
         "id": id,
         "guid": guid,
         "balance": debitBalance + creditBalance,
         "numberOfFriends": len(friends),
         "registered": registered,
         "lastActive": time_now()
                }
    return jsonify(response) # возвращаем тело ответа в формате JSON

# обработчик запросов по методу GET и PATH /api/json/
@app.route('/api/json/', methods=['GET'])
def json_get():
    action = request.args.get('id') # добавляем параметр для запроса
    response = {"id": action,  # передаем id клиета из PATH
                "guid": uuid.uuid1(),  # рандомный giud
                "balance": random.randrange(9999),  # рандомное 4-значное число
                "address": address_generator(),  # вызов функции рандомной строки для адреса
                "registered": time_now()}  # вызов функции текущего времени
    return jsonify(response)  # возвращаем тело ответа в формате JSON
# генератор строки адреса
def address_generator(size=200, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# генератор текущего времени по формату iso
def time_now():
    current_time = datetime.now().isoformat(sep="T", timespec="seconds")
    return current_time

if __name__ == '__main__':   
    app.run()           # запуск приложения
