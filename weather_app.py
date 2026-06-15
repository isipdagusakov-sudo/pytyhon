import requests

API_KEY = "4225cc6dd5ccae3047886d98fda84369"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        if response.status_code == 401:
            return f"Ошибка: Неверный API ключ"
        
        if response.status_code == 404:
            return f"Город '{city}' не найден"
        
        if response.status_code == 200:
            data = response.json()
            
            print("\n" + "="*40)
            print(f"Погода в городе: {data['name']}")
            print("="*40)
            print(f"Температура: {data['main']['temp']}°C")
            print(f"Описание: {data['weather'][0]['description']}")
            print(f"Влажность: {data['main']['humidity']}%")
            print(f"Ветер: {data['wind']['speed']} м/с")
            print(f"Ощущается как: {data['main']['feels_like']}°C")
            print(f"Давление: {data['main']['pressure']} гПа")
            print("="*40 + "\n")
            return None
        
        return f"Ошибка HTTP {response.status_code}"
    
    except requests.exceptions.Timeout:
        return "Ошибка: Превышен таймаут запроса (5 секунд)"
    except requests.exceptions.RequestException as e:
        return f"Ошибка соединения: {str(e)}"

if __name__ == '__main__':
    print("\n" + "="*40)
    print("ПОГОДНОЕ ПРИЛОЖЕНИЕ")
    print("="*40)
    print("Команды:")
    print("  Введите название города - показать погоду")
    print("  'exit' или 'quit' - выход")
    print("  'help' - показать помощь")
    print("="*40 + "\n")
    while True:
        city = input("Введите название города").strip()
    
        if city.lower() in ['exit', 'quit', 'выйти', 'выход']:
            print("\nДо свидания!\n")
            break
        
        if city.lower() == 'help':
            print("\nПросто введите название города на английском")
            print("Примеры: Moscow, London\n")
            continue
        result = get_weather(city)
        if result:
            print(result + "\n")