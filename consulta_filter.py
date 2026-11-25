from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Veterinario

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Buscar un veterinario por su licencia profesional
veterinarios = session.query(Veterinario).filter(
    Veterinario.licencia_profesional == 'VET369'
).all()

print("\nLISTADO DE VETERINARIOS CON LICENCIA PROFESIONAL 'VET369':\n")

# Mostrar resultado
for veterinario in veterinarios:
    print(veterinario.nombres, veterinario.apellidos)


print(veterinario)
