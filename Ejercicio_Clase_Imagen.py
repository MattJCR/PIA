# python -m pip install --upgrade Pillow numpy requests
from PIL import Image
import numpy as np
from random import randint

class ImageManager:
    
    def create_image_array(w,h,rgb):
        data = np.zeros((w, h, 3), dtype = np.uint8 )
        for i in range(0, data.shape[0]):
            for j in range(0, data.shape[1]):
                data[i, j] = rgb
        return data
    
    def generate_random_color():
        return [randint(0, 255), randint(0, 255), randint(0, 255)]
    
    def create_image(w,h,rgb):
        '''
         a) Implementa un método al que se le pase el ancho
         y el alto de la imagen y el color de la misma. 
         El método debe devolver la imagen creada.
        '''
        
        return Image.fromarray(ImageManager.create_image_array(w,h,rgb))
    
    def create_random_image_colored(x,y,w,h):
        '''
         b) Implementa un método al que se le pasa el número de elementos 
         horizontales y verticales, así como el ancho y el alto de los 
         elementos horizontales y verticales y que devuelva la imagen 
         creada con un color de fondo diferente para cada elemento.
        '''
        for a in range(0,y):
            for b in range(0,x):
                if(b == 0):
                    fila = ImageManager.create_image_array(w,h,ImageManager.generate_random_color())
                else:
                    fila = np.hstack([fila, ImageManager.create_image_array(w,h,ImageManager.generate_random_color())])
            if(a == 0):
                matrix = fila
            else:
                matrix = np.vstack([matrix, fila])
        return Image.fromarray(matrix)
    
    def resize_image(w,h,img):
        '''
         c) Implementa un método que redimensiona una imagen al ancho 
         y alto especificado, este método deforma la imagen si la relación 
         de aspecto no es la misma.
        '''
        return img.resize((w, h))
    
    def resize_image_width(w,img):
        '''
          d) Implementa un método que redimensiona una imagen al ancho 
          especificado, sin deformar la imagen.
        '''
        percent = (w / float(img.size[0]))
        h = int((float(img.size[1]) * float(percent)))
        print('resize width',w,h)
        return img.resize((w, h))
    
    def resize_image_height(h,img):
        '''
          e) Implementa un método que redimensiona una imagen al ancho 
          especificado, sin deformar la imagen.
        '''
        percent = (h / float(img.size[1]))
        w = int((float(img.size[0]) * float(percent)))
        print('resize height',w,h)
        return img.resize((w, h))
    
    def cut_image(x,y,w,h,img):
        '''
         f) Implementa un método que devuelva un trozo de una imagen 
         especificando la posición horizontal y vertical y el ancho 
         y el alto, si las dimensiones especificadas son superiores 
         a la imagen original, debe devolver el recorte disponible.
        '''
        width = img.size[0]
        height = img.size[1]
        if(x > width): x >= width - 1
        if(w > width): w >= width - 1
        if(y > height): y >= height - 1
        if(h > height): h >= height - 1
        arr = np.asarray(img)
        arr = arr[y:h, x:w]
        return Image.fromarray(arr)
    
    def stack_image(img_a,img_b):
        '''
        g) Implementa un método que apile dos imágenes horizontal o 
        verticalmente, sin deformarlas. El método debe especificar 
        en sus argumentos qué dimensiones son las que se deben adaptar.
        '''
        if(img_a.size > img_b.size and img_a.size[0] > img_b.size[0]):
            img_b = ImageManager.resize_image_width(img_a.size[0],img_b)
            print('a',img_a.size,img_b.size)
            return Image.fromarray(np.vstack([np.asarray(img_a), np.asarray(img_b)]))
        if(img_a.size > img_b.size and img_a.size[1] > img_b.size[1]):
            img_b = ImageManager.resize_image_width(img_a.size[0],img_b)
            print('b',img_a.size,img_b.size)
            return Image.fromarray(np.hstack([np.asarray(img_a), np.asarray(img_b)]))
        if(img_a.size < img_b.size and img_a.size[0] < img_b.size[0]):
            img_a = ImageManager.resize_image_width(img_b.size[0],img_a)
            print('c',img_a.size,img_b.size)
            return Image.fromarray(np.vstack([np.asarray(img_a), np.asarray(img_b)]))
        if(img_a.size < img_b.size and img_a.size[1] < img_b.size[1]):
            img_a = ImageManager.resize_image_width(img_b.size[0],img_a)
            print('d',img_a.size,img_b.size)
            return Image.fromarray(np.hstack([np.asarray(img_a), np.asarray(img_b)]))
  
    def stack_image_full(img_a,img_b):
        '''
        h) Implementa un método que apile dos imágenes horizontal o 
        verticalmente, si las dimensiones de las imágenes no coinciden, 
        debe adaptarlas a la imagen más ancha o más alta, deformándolas 
        si fuera necesario.
        '''
        if(img_a.size > img_b.size):
            img_b = ImageManager.resize_image(img_a.size[0],img_a.size[1],img_b)
            return Image.fromarray(np.vstack([np.asarray(img_a), np.asarray(img_b)]))
        else:
            img_a = ImageManager.resize_image(img_b.size[0],img_b.size[1],img_a)
            return Image.fromarray(np.hstack([np.asarray(img_a), np.asarray(img_b)]))
    
    def insert_image(img_a,img_b, x,y):
        '''
        i) Implementa un método que inserte una imagen dentro de otra imagen 
        en la posición horizontal y vertical especificada. Si la imagen que 
        se va a insertar no cabe entera, debe recortarla. Ejemplo: La primera 
        imagen se inserta en dos imágenes diferentes. En la primera imagen, la 
        posición de inserción especificada no permite insertar la imágen completa. 
        En la segunda imagen, la posición de inserción permite insertar la imagen de forma completa.
        '''
        if(x < 0):
            x = 0
        if(y < 0):
            y = 0
        arr_a = np.copy(np.asarray(img_a))
        arr_b = np.asarray(img_b)
        shape_x_a = x + arr_b.shape[0]
        shape_y_a = y + arr_b.shape[1]
        shape_x_b = arr_a.shape[0] - x
        shape_y_b = arr_a.shape[1] - y
        if(shape_x_a > arr_a.shape[0]):
            shape_x_a = arr_a.shape[0]
        if(shape_y_a > arr_a.shape[1]):
            shape_y_a = arr_a.shape[1]
        print(shape_x_a,shape_y_a,shape_x_b,shape_y_b)

        arr_a[x:shape_x_a,y:shape_y_a] = arr_b[0:shape_x_b,0:shape_y_b]
        return Image.fromarray(arr_a)
    def insert_image_and_resize(img_a,img_b, x,y,w,h):
        '''
        j) Implementa un método que inserte dentro de una imagen otra imagen en la 
        posición horizontal y vertical especificada con el ancho y el alto especificado. 
        Si la imagen que se va a insertar no cabe entera, debe recortarla.
        '''
        img_b = ImageManager.resize_image(w,h,img_b)
        return ImageManager.insert_image(img_a,img_b,x,y)
        

        
    
    
# ImageManager.create_image(128,128,[255,128,0]).show()
img =  ImageManager.create_random_image_colored(4,4,100,100)
# ImageManager.resize_image(700,300,img).show()
# ImageManager.resize_image_width(100,img).show()
# ImageManager.resize_image_height(600,img).show()
img2 = ImageManager.cut_image(100,90,300,100,img)
# ImageManager.stack_image(img2,img).show()
# ImageManager.stack_image_full(img2,img).show()
# ImageManager.insert_image(img,img2,100,300).show()
ImageManager.insert_image_and_resize(img,img2,100,100,100,100).show()