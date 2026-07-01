from flask import Blueprint, request, redirect, url_for, render_template
from table.models import CarDealer
from table.database import session

car_bp = Blueprint('cars', __name__, template_folder='templates')

@car_bp.route('/add_auto', methods=['GET', 'POST'])
def add_auto():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        address = request.form.get('address')
        dealer = CarDealer(name=name, city=city, address=address)
        session.add(dealer)
        session.commit()
        return redirect(url_for('main'))
    return render_template('add_dealers.html')


@car_bp.route('/delete/<int:id>', methods=['POST'])
def auto_delete(id):
    auto = CarDealer.query.filter_by(id=id).first()
    session.delete(auto)
    session.commit()
    return redirect(url_for('main'))
