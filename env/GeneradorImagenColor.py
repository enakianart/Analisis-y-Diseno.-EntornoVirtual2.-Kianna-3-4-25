from PIL import Image

color_deseado = input("Ingresa el color deseado (en inglés o color hexadecimal): ")

imagen = Image.new('RGB', (500, 500), color=color_deseado)

nombre_archivo = f"imagen_{color_deseado}.png"
imagen.save(nombre_archivo)

print(f"Imagen {nombre_archivo} creada y guardada con perfectamete ヽ(✿ﾟ▽ﾟ)ノ.")