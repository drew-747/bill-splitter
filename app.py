from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    bill_amount = float(data['billAmount'])
    num_people = int(data['numPeople'])
    service_charge = float(data['serviceCharge'] or 0)

    total_with_charge = bill_amount + service_charge
    per_person = total_with_charge / num_people

    return jsonify({
        'amountPerPerson': round(per_person, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)