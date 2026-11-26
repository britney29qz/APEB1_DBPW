from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica
from sqlalchemy import or_

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Buscar historia clínicas con diagnóstico "infección urinaria" o "fractura de pata"
historias = session.query(HistoriaClinica).filter(
    or_(
        HistoriaClinica.diagnostico_principal.contains("infección urinaria"),
        HistoriaClinica.diagnostico_principal.contains("fractura de pata")
    )
).all()

print("\nLISTADO DE HISTORIAS CLÍNICAS CON DIAGNÓSTICO 'INFECCIÓN URINARIA' O 'FRACTURA DE PATA':\n")

# Mostrar resultado
for historia in historias:
    print(historia)
    print("--------------------------------------------------")

# Cerrar la sesión 
session.close()  