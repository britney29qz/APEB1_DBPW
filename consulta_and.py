from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica, Veterinario
from sqlalchemy import and_

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Buscar historias clínicas de Bella y Max
historias = session.query(HistoriaClinica).join(Veterinario).filter(
    and_(
        HistoriaClinica.diagnostico_principal.contains("fractura de pata"),
        Veterinario.nombres == 'Carlos Eduardo'
    )).all()

print("\nLISTADO DE HISTORIAS CLÍNICAS CON DIAGNÓSTICO DE FRACTURA DE PATA ATENDIDAS POR CARLOS EDUARDO:\n")

# Mostrar resultado
for historia in historias:
    print(historia)
    print("--------------------------------------------------")

