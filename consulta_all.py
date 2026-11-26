from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar todas las clínicas
clinicas = session.query(Clinica).all()

print("\nLISTADO DE CLÍNICAS VETERINARIAS Y SU CANTIDAD DE HISTORIAS CLÍNICAS ASOCIADAS:\n")

# Mostrar las clínicas y sus historias clínicas
for clinica in clinicas:
    cantidad_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            cantidad_historias += len(veterinario.historias_clinicas)   
    
    print(clinica)
    print("Cantidad de historias clínicas:", cantidad_historias)
    print("--------------------------------------------------")

# Cerrar la sesión 
session.close()  

