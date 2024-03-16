import requests

def register_ticket(ticket_data):
    url = 'http://your_server_ip/register_ticket'  # Замените на IP-адрес вашего сервера
    response = requests.post(url, json=ticket_data)
    if response.status_code == 200:
        data = response.json()
        print("Билет успешно зарегистрирован. Номер билета:", data["ticket_id"])
    else:
        print("Ошибка при регистрации билета")

# Пример использования
ticket_data = {
    "name": "John Doe",
    "event": "Concert",
    # Другие данные о билете...
}

register_ticket(ticket_data)
