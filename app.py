from flask import Flask, render_template
from flask_login import current_user
from table.database import session
from table.models import CarDealer, Car

app = Flask(__name__)


@app.route('/')
def mainO():
    dealers = session.query(CarDealer).all()
    return render_template('index.html', current_user=current_user, dealers=dealers)


@app.route('/add_dealer')
def add_dealer():
        dealer = CarDealer(name='АвтоСалон Грозный', city='Грозный', address='ул. Ленина, 5')
        session.add(dealer)
        session.commit()
        return f'Добавлен диллер: {dealer.name}'


if __name__ == '__main__':
    app.run(debug=True)