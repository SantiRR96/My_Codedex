import imageio.v3 as iio

nombreArchivos = ['imagen1.png' , 'imagen2.png'] #Nombre de los archivs, recordar estar en la misma carpeta del proyecto
imagenes = [ ] #Lista vacia para que luego alojen los datos de las imagenes

for nombreArchivo in nombreArchivos:
    imagenes.append(iio.imread(nombreArchivo))  #En este bucle se cargan las imagenenes a la variable

iio.imwrite('imagen.gif', imagenes, duration = 500, loop = 0) #Convierto las imagenes en GIF
