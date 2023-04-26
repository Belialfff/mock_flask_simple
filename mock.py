# импорты
from flask import Flask, jsonify, request
from datetime import datetime
import uuid
import string
import random

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# обработчик запросов по методам GET и POST и PATH /api/json/
@app.route('/api/json/<id>', methods=['POST'])
def json_post(id):

    request_data = request.get_json()
    friends = request_data["friends"]
    guid = uuid.uuid1()   # для POST запроса парсим каждое поле, запиысывая его в отдельные переменные
    debitBalance = request_data["debitBalance"]
    creditBalance = request_data["creditBalance"]
    phone = request_data ["phone"]
    registered = request_data["registered"]
    is_active = bool(request_data)


    response = {
         "id": id,
         "guid": guid,
         "balance": debitBalance + creditBalance,
         "numberOfFriends": len(friends),
         "registered": registered,
         "lastActive": time_now()
                }
    return jsonify(response)                    # возвращаем тело ответа в формате JSON

# обработчик запросов по методам GET и POST и PATH /api/json/
@app.route('/api/json/', methods=['GET'])
def json_get():
    action = request.args.get('id')
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