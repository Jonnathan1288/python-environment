# instituto/clase.py

from estudiante import devolver_materias

def estudiante_registrado_en_materia(nombre: str, materia: str) -> bool:
    """Verifica si el estudiante está registrado en una materia.

    Args:
        nombre (str): Nombre del estudiante.
        materia (str): Nombre de la materia.

    Returns:
        bool: True si el estudiante está registrado en la materia, False en caso contrario.

    Raises:
        KeyError: Si el estudiante no está en el diccionario.
    """
    try:
        materias = devolver_materias(nombre)
        return materia in materias
    except KeyError as e:
        print(f"Error: {e}")
        return False
