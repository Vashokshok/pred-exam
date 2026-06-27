from sqlalchemy import String, Integer, Column, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class CarDealer(Base):
    __tablename__ = 'cardealers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)

    cars = relationship('Car', back_populates='dealer')


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=True)
    dealer_id = Column(Integer, ForeignKey('cardealers.id', ondelete='CASCADE'), nullable=False)

    dealer = relationship('CarDealer', back_populates='cars')
