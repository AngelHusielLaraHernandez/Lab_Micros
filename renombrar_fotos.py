import os

def renombrar_fotos_img(ruta_base):
    # Carpeta principal donde están las subcarpetas de actividades
    actividades = [d for d in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, d))]
    for carpeta in actividades:
        if carpeta in ["Actividad6", "Actividad7"]:
            continue
        ruta_carpeta = os.path.join(ruta_base, carpeta)
        fotos = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith('.jpg')]
        fotos.sort()  # Ordena para que el renombrado sea consistente
        # Extraer el número de la actividad
        num_act = ''.join(filter(str.isdigit, carpeta))
        for idx, foto in enumerate(fotos, 1):
            nuevo_nombre = f"Act{num_act}_{idx}.jpg"
            ruta_vieja = os.path.join(ruta_carpeta, foto)
            ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
            if ruta_vieja != ruta_nueva:
                print(f"Renombrando: {ruta_vieja} -> {ruta_nueva}")
                os.rename(ruta_vieja, ruta_nueva)

if __name__ == "__main__":
    # Cambia esta ruta si tu estructura cambia
    ruta_img = os.path.join(os.path.dirname(__file__), "img")
    renombrar_fotos_img(ruta_img)
    print("Renombrado completado.")
