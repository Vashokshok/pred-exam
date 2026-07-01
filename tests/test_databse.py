from table.models import CarDealer, Car, Base
from table.database import session, engine

Base.metadata.create_all(engine)

def test_add_dealer():
    deaker = CarDealer(name='Car_Car', city='Грозный', address='ул. Ионосани')
    session.add(deaker)
    session.commit()

    saved = session.query(CarDealer).filter_by(name='Элайтеar').first()
    assert saved is not None
    assert saved.city == 'Грозный'

    session.delete(saved)
    session.commit()