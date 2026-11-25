from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

#Importar las clases
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

#Importar el motor de conexion a la base de datos
from configuracion import cadena_base_datos

#Crear el motor de conexion a la base de datos
engine = create_engine(cadena_base_datos, echo=True)

#Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

#Crear objetos de tipo Clinica
clinica1 = Clinica(nombre='Clínica Veterinaria Patitas Alegres', direccion='Av. 19 de Mayo, Ciudad La Maná', nombre_responsable='Dra. Ana Pérez')
clinica2 = Clinica(nombre='Clínica Veterinaria Huellitas', direccion='Calle Bolívar, Ciudad Latacunga', nombre_responsable='Dr. Juan Gómez')

#Crear objetos de tipo Consultorio
consultorio1 = Consultorio(nombre='Consultorio A', especialidad='Medicina general', clinica=clinica1)
consultorio2 = Consultorio(nombre='Consultorio B', especialidad='Cirugía veterinaria', clinica=clinica2)
consultorio3 = Consultorio(nombre='Consultorio C', especialidad='Dermatología', clinica=clinica1)

#Crear objetos de tipo Veterinario
veterinario1 = Veterinario(nombres='María Fernanda', apellidos='González López', correo='mariagonzales@gmail.com', licencia_profesional='VET147', consultorio=consultorio1)
veterinario2 = Veterinario(nombres='Carlos Eduardo', apellidos='Ramírez Torres', correo='carlosramirez@gmail.com', licencia_profesional='VET258', consultorio=consultorio2)
veterinario3 = Veterinario(nombres='Lucía Isabel', apellidos='Mendoza Rojas', correo='luciamendoza@gmail.com', licencia_profesional='VET369', consultorio=consultorio3)
veterinario4 = Veterinario(nombres='Andrés Felipe', apellidos='Vásquez Paredes', correo='andresvasquez@gmail.com', licencia_profesional='VET741', consultorio=consultorio1)
veterinario5 = Veterinario(nombres='Isabel Sofía', apellidos='Cruz Herrera', correo='isabelcruz@gmail.com', licencia_profesional='VET852', consultorio=consultorio2)
veterinario6 = Veterinario(nombres='Diego Alejandro', apellidos='Ramos Castillo', correo='diegoramos@gmail.com', licencia_profesional='VET963', consultorio=consultorio3)

#Crear objetos de tipo Historia Clinica
historia1 = HistoriaClinica(fecha=date(2026, 11, 10), diagnostico_principal='Gastroenteritis', tratamiento_prescrito='Dieta blanda y medicación', nombre_mascota='Toby', veterinario=veterinario1)
historia2 = HistoriaClinica(fecha=date(2026, 10, 22), diagnostico_principal='Fractura de pata', tratamiento_prescrito='Cirugía y reposo', nombre_mascota='Max', veterinario=veterinario2)
historia3 = HistoriaClinica(fecha=date(2026, 11, 15), diagnostico_principal='Infección urinaria', tratamiento_prescrito='Antibióticos y cambios de dieta', nombre_mascota='Luna', veterinario=veterinario1)
historia4 = HistoriaClinica(fecha=date(2026, 11, 8), diagnostico_principal='Alergia cutánea', tratamiento_prescrito='Baños medicados y antihistamínicos', nombre_mascota='Rocky', veterinario=veterinario3)
historia5 = HistoriaClinica(fecha=date(2026, 11, 20), diagnostico_principal='Obesidad', tratamiento_prescrito='Dieta controlada y ejercicio', nombre_mascota='Bella', veterinario=veterinario4)
historia6 = HistoriaClinica(fecha=date(2026, 11, 4), diagnostico_principal='Fractura de pata', tratamiento_prescrito='Cirugía y reposo', nombre_mascota='Simba', veterinario=veterinario5)

#Agregar los objetos a la sesión
session.add_all([
    clinica1, clinica2, 
    consultorio1, consultorio2, consultorio3, 
    veterinario1, veterinario2, veterinario3, veterinario4, veterinario5, veterinario6,
    historia1, historia2, historia3, historia4, historia5, historia6
])

#Guardar los cambios en la base de datos
session.commit()

print("Datos ingresados correctamente")