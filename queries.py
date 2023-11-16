import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["gameinfo"]
collection = db["games"]

# Функция для отбора игр по жанру "Indie"
def get_indie_games():
    result_games = collection.find({"Жанры": {"$regex": "Indie"}})
    return result_games

# Функция для отбора игр по издателю "Electronic Arts"
def get_EA_games():
    result_games = collection.find({"Издатель": {"$regex": "Electronic Arts"}})
    return result_games

# Функция для сортировке по цене (по убыванию)
def sort_games_by_price_desc():
    games=collection.find()
    sorted_games = sorted(games, key=lambda x: x["Цена в США"], reverse=True)
    return sorted_games

# Функция для получения количества игр с ценой 19.99 и поддержкой русского языка
def count_games_with_price_and_language():
    count = collection.count_documents({"Цена в США": 19.99, "Языки": {"$regex": "Russian"}})
    return count
 
# Функция для получения количество бесплатных игры от издателя Valve
def count_games_with_freee_and_Valve():
    count = collection.count_documents({"Цена в США": 0.0, "Издатель": "Valve"})
    return count
 
 
 
# Основная функция
def main():
    indie_games = get_indie_games()
    print(list(indie_games))
    
    ea_games = get_EA_games()
    print(list(ea_games))
        
    sorted_game = sort_games_by_price_desc()  
    print(list(sorted_game))
        
    count1 = count_games_with_price_and_language()
    print(count1)
    count2 = count_games_with_freee_and_Valve()
    print(count2)

if __name__ == "__main__":
    main()
