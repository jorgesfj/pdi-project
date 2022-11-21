from PIL import Image
from PIL import ImageFilter


#Carregando Imagem
imagePath   = "./69364_sat.jpg"
imageObject = Image.open(imagePath)

#Convertendo a imagem para tons de cinza
imageObject = imageObject.convert('L')

#Metodo para aplicar o filtro Maximo
def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter(size=15))

#Metodo para aplicar o filtro Minimo
def applyMinimumFilter(image):
    return image.filter(ImageFilter.MinFilter(size=15))

#Aplicando os filtros
filterApplied = imageObject
filterApplied = applyMaximumFilter(filterApplied) 
filterApplied = applyMinimumFilter(filterApplied) 

#Mostrando Imagens
imageObject.show()
filterApplied.show()