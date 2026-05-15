import os

def renombrar_fotos_img(ruta_base):
    # Carpeta principal donde están las subcarpetas (anim, Corriente, etc.)
    carpetas = [d for d in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, d))]
    
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta_base, carpeta)
        
        # Filtramos por imágenes (añadí .png y .jpeg por si acaso, puedes ajustarlo)
        fotos = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        fotos.sort()  # Ordena para que el renombrado sea consistente
        
        for idx, foto in enumerate(fotos, 1):
            # Extraer la extensión original del archivo (.jpg, .png, etc.)
            _, extension = os.path.splitext(foto)
            
            # El nuevo nombre será: NombreDeLaCarpeta_1.jpg, NombreDeLaCarpeta_2.jpg...
            nuevo_nombre = f"{carpeta}_{idx}{extension}"
            
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