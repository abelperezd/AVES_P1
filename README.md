### Información del repositorio
En este repositorio encontramos la entrega de la práctica 1 de la asignatura SCAV (parte de vídeo). 

Tenemos 5 archivos .py y en cada de uno de ellos encontramos una explicación detallada sobre cómo utilizarlos, pero de manera general hacen lo siguiente:

- **[1] rgb_yuv.py**: convierte 3 valores RGB a YUV y viceversa.
- **[2] ex2and3.py**: recorta una imagen y el resutlado lo convierte en una nueva imagen en escala de grises (utilizando FFMPEG).
- **[3] ex3_v2.py**: pasa una imagen de color a blanco y negro (utilizando FFMPEG).
- **[4] ex4.py**: aplicamos run-lenght a una secuencia alfanumérica.
- **[5] ex5.py**: aplicamos la DFT y la IDFT a una imagen y comparamos el resultado obtenido con la imagen original.

# Resultados obtenidos
La imagen de referencia que hemos utilizado en los apartados en los que hemos requerido una imagen es la siguiente:

![](https://drive.google.com/uc?export=view&id=15GJsZnb0ugWx2UiARS7o2ENTFPopMajR
)

## [2]
Una vez ejecutamos este script, los resultados obtenido son las dos siguientes imágenes:
![](https://drive.google.com/uc?export=view&id=1RfhvISMt7ilk5uS9r1iKXoDu491TYg50)    ![](https://drive.google.com/uc?export=view&id=1iPUK-NE9_y_xJ-mhLVJ0s-BHLWvgxKO6)

En el primer caso, dado que pasamos de una imagen de 2000x2000 a una de 200x200, obtenemos una gran reducción de tamaño (de 336.6 kB a 7.3 kB).

Para el segundo caso, pasamos de la imagen de color a escala de grises y teniendo en cuenta que el formato que utilizamos es JPEG, tambien obtenemos una reducción en el tamaño del archivo (de 7.3 kB a 6.2 kB). En caso de utilizar otros formatos de salida, podríamos obtener imagenes con una mejor compresión.

## [3]
En este caso, aplicamos directamente la conversión a blanco y negro de la imagen original. Obtenemos también una imagen de menor tamaño (282 kB).

![](https://drive.google.com/uc?export=view&id=1yJruJtHCQMagkqjZKWa3IPcK3A2i_6kI)

## [5]
Tras ejecutar este script, obtenemos en pantalla la comparativa entre las dos imágenes, y a simple vista no observamos ninguna diferencia (la imagen de entrada es exactamente igual a la de salida, sin ninguna pérdida).

![](https://drive.google.com/uc?export=view&id=1i7K1cw5FssH20VqWb6ogI2XAkW9KHON0)
