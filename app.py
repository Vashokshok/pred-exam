from flask import Flask, render_template
from flask_login import current_user
from table.database import session
from table.models import CarDealer, Car
from auto.routes import car_bp


app = Flask(__name__)

app.register_blueprint(car_bp, url_prefix='/cars')


@app.route('/')
def main():
    dealers = session.query(CarDealer).all()
    return render_template('index.html', current_user=current_user, dealers=dealers)


if __name__ == '__main__':
    app.run(debug=True)