from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar historias clinicas ordenadas por fecha de manera descendente
historias = session.query(HistoriaClinica).order_by(
    HistoriaClinica.fecha.desc()
).all()

print("\nLISTADO DE HISTORIAS CLÍNICAS ORDENADAS POR LA FECHA MÁS RECIENTE :\n")

# Mostrar resultado
for historia in historias:
    print(historia)
    print("--------------------------------------------------")
