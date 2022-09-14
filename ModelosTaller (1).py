import db
from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey, Float
from sqlalchemy.orm import relationship

#['DEPARTAMENTO', 'MUNICIPIO', 'CODIGO DANE', 'CLASE BIEN', 'FECHA HECHO', 'CANTIDAD']


class Departamentos(db.Base):
    __tablename__='departamentos'
    id=Column(Integer,primary_key=True)
    departamentos=Column('departamentos', Text)
    municipios = relationship('Municipios')

class Municipios(db.Base):
    __tablename__='municipios'
    codigodane  = Column('codigodane', String(20) ,primary_key=True)
    municipios =Column('municipios',Text)
    id_dept=Column(Integer,ForeignKey('departamentos.id'))
    incautacion = relationship('Incautacion')

class Incautacion(db.Base):
    __tablename__='incautacion'
    id=Column(Integer,primary_key=True)
    clasebien = Column('clasebien',Text)
    fecha = Column('fecha',Text)
    cantidad = Column('cantidad',Text)
    id_mnp = Column(String(20), ForeignKey('municipios.codigodane'))
