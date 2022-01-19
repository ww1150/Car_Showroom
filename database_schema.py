from sqlalchemy import Column, Integer, Float, String, Text, Date, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Position(Base):
    __tablename__ = 'position'
    __table_args__ = {
        'comment': 'Должности'
    }

    position_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    position_name = Column(String(50), comment='Наименование должности')
    salary = Column(Float, comment='Оклад')
    responsibilities = Column(String, comment='Обязанности')
    requirements = Column(String, comment='Требования')


class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {
        'comment': 'Сотрудники'
    }

    employee_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    full_name = Column(String(50), comment='ФИО')
    age = Column(Integer, comment='Возраст')
    gender = Column(Boolean, comment='Пол')
    address = Column(String, comment='Адрес')
    phone_number = Column(String(12), comment='Телефон')
    passport = Column(Integer, comment='Паспортные данные')
    position_id = Column(Integer, ForeignKey('position.position_id'), comment='Код должности')

    position = relationship('Position', backref='quote_position', lazy='subquery')


class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    __table_args__ = {
        'comment': 'Производитель'
    }

    manufacturer_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    name = Column(String(50), comment='Наименование')
    country = Column(Integer, comment='Страна')
    address = Column(String, comment='Адрес')
    description = Column(Text, comment='Описание')
    employee_id = Column(Integer, ForeignKey('employee.employee_id'), comment='Код сотрудника')

    employee = relationship('Employee', backref='quote_employee', lazy='subquery')


class AdditionalEquipment(Base):
    __tablename__ = 'equipment'
    __table_args__ = {
        'comment': 'Дополнительное оборудование'
    }

    equipment_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    name = Column(String(50), comment='Наименование')
    specifications = Column(String, comment='Характеристики')
    price = Column(Float, comment='Цена')


class CarType(Base):
    __tablename__ = 'car_type'
    __table_args__ = {
        'comment': 'Тип кузова'
    }

    car_type_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    name = Column(String(50), comment='Название')
    description = Column(Text, comment='Описание')


class Car(Base):
    __tablename__ = 'car'
    __table_args__ = {
        'comment': 'Автомобили'
    }

    car_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    model = Column(String(50), comment='Марка')
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.manufacturer_id'), comment='Код производителя')
    car_type_id = Column(Integer, ForeignKey('car_type.car_type_id'), comment='Код типа кузова')
    production_date = Column(Date, comment='Дата производства')
    color = Column(String, comment='Цвет')
    vin = Column(String, comment='Номер кузова')
    engine_number = Column(String, comment='Номер двигателя')
    specifications = Column(String, comment='Характеристики')
    equipment_id_1 = Column(Integer, ForeignKey('equipment.equipment_id'), comment='Код оборудования 1')
    equipment_id_2 = Column(Integer, ForeignKey('equipment.equipment_id'), comment='Код оборудования 2')
    equipment_id_3 = Column(Integer, ForeignKey('equipment.equipment_id'), comment='Код оборудования 3')
    price = Column(Float, comment='Цена')
    employee_id = Column(Integer, ForeignKey('employee.employee_id'), comment='Код сотрудника')

    manufacturer = relationship('Manufacturer', backref='quote_manufacturer', lazy='subquery')
    car_type = relationship('CarType', backref='quote_car_type', lazy='subquery')
    equipment = relationship('Equipment', backref='quote_equipment', lazy='subquery')
    employee = relationship('Employee', backref='quote_employee', lazy='subquery')


class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = {
        'comment': 'Заказчики'
    }

    customers_id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
        comment='Код'
    )
    full_name = Column(String(50), comment='ФИО')
    address = Column(String, comment='Адрес')
    phone_number = Column(String(12), comment='Телефон')
    passport = Column(Integer, comment='Паспортные данные')
    car_id = Column(Integer, ForeignKey('car.car_id'), comment='Код автомобиля')
    order_date = Column(Date, comment='Дата заказа')
    sale_date = Column(Date, comment='Дата продажи')
    complete_mark = Column(Boolean, comment='Отметка о выполнении')
    payment_mark = Column(Boolean, comment='Отметка об оплате')
    prepayment_percentage = Column(Integer, comment='Процент предоплаты')
    employee_id = Column(Integer, ForeignKey('employee.employee_id'), comment='Код сотрудника')

    car = relationship('Car', backref='quote_car', lazy='subquery')
    employee = relationship('Employee', backref='quote_employee', lazy='subquery')


if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
