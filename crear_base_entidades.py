from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

#Importar la cadena de conexión desde el archivo de configuración
from configuracion import cadena_base_datos

#Crear el motor de conexion a la base de datos
engine = create_engine(cadena_base_datos)

#Crear la clase base
Base = declarative_base()

#Definir la entidad Clinica
class Clinica(Base):
    __tablename__ ='clinica'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(200))
    nombre_responsable = Column(String(100))

    def __repr__(self):
        return "Clínica: %s, dirección: %s, responsable: %s" % (
            self.nombre, self.direccion, self.nombre_responsable)

    #Relación con Consultorio
    consultorios = relationship('Consultorio', back_populates='clinica')

#Definir la entidad Consultorio
class Consultorio(Base):
    __tablename__ = 'consultorio'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    especialidad = Column(String(100))
    clinica_id = Column(Integer, ForeignKey('clinica.id'))

    #Relación con Clinica y Veterinario
    clinica = relationship('Clinica', back_populates='consultorios')
    veterinarios = relationship('Veterinario', back_populates='consultorio')

    def __repr__(self):
        return "Consultorio: %s, especialidad: %s" % (
            self.nombre, self.especialidad)
    

#Definir la entidad Veterinario
class Veterinario(Base):
    __tablename__ = 'veterinario'

    id = Column(Integer, primary_key=True)
    nombres= Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100))
    licencia_profesional = Column(String(50))
    consultorio_id = Column(Integer, ForeignKey('consultorio.id'))
    
    #Relación con Consultorio e Historia Clinica
    consultorio = relationship('Consultorio', back_populates='veterinarios')
    historias_clinicas = relationship('HistoriaClinica', back_populates='veterinario')

    def __repr__(self):
        return "Veterinario: %s %s, correo: %s, licencia profesional: %s" % (
            self.nombres, self.apellidos, self.correo, self.licencia_profesional)
    

#Definir la entidad Historia Clinica
class HistoriaClinica(Base):
    __tablename__ = 'historia_clinica'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    diagnostico_principal = Column(Text)
    tratamiento_prescrito = Column(Text)
    nombre_mascota = Column(String(100))
    veterinario_id = Column(Integer, ForeignKey('veterinario.id'))
    
    #Relación con Veterinario
    veterinario = relationship('Veterinario', back_populates='historias_clinicas')

    def __repr__(self):
        return "Historia Clinica: %s, diagnostico principal: %s, tratamiento prescrito: %s, nombre de la mascota: %s" % (
            self.fecha, self.diagnostico_principal, self.tratamiento_prescrito, self.nombre_mascota)


#Crear las tablas en la base de datos
Base.metadata.create_all(engine)