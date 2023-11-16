import pymongo
import json

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["gameinfo"]
collection = db["games"]

# Чтение данных из JSON
def read_from_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Запись данных в MongoDB
def write_to_mongodb(data):
    collection.insert_many(data)
    print("Данные успешно записаны в MongoDB")

# Основная функция
def main():
    file = "game_info.json"
    data = read_from_json(file)
    write_to_mongodb(data)

if __name__ == "__main__":
    main()
