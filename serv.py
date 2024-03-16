from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Хранилище данных о билетах (в реальном приложении это может быть база данных)
tickets = []

@app.route('/register_ticket', methods=['POST'])
def register_ticket():
    data = request.json
    ticket_id = generate_ticket_id()
    data['ticket_id'] = ticket_id
    tickets.append(data)
    return jsonify({"message": "Ticket registered successfully", "ticket_id": ticket_id})

@app.route('/verify_ticket', methods=['POST'])
def verify_ticket():
    data = request.json
    ticket_id = data.get('ticket_id')
    for ticket in tickets:
        if ticket.get('ticket_id') == ticket_id:
            return jsonify({"message": "Ticket is valid"})
    return jsonify({"message": "Ticket is invalid"})

def generate_ticket_id():
    return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))

if __name__ == '__main__':
    app.run(debug=True)
