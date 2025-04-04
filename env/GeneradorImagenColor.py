from PIL import Image

color_deseado = input("Ingresa el color deseado (en inglés o color hexadecimal): ")

# Crear la imagen con el color especificado por el usuario
imagen = Image.new('RGB', (500, 500), color=color_deseado)

# Guardar la imagen con un nombre descriptivo
nombre_archivo = f"imagen_{color_deseado}.png"
imagen.save(nombre_archivo)

# Imprimir un mensaje de confirmación
print(f"Imagen {nombre_archivo} creada y guardada con perfectamete ヽ(✿ﾟ▽ﾟ)ノ.")