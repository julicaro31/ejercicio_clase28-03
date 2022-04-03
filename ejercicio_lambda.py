encriptar_letra = lambda x: chr(ord(x)+1) # le suma 1 al valor ascii y luego lo vuelve a convertir en carcater

def encripto(palabra):
    cod =''
    for i in palabra:
        cod += encriptar_letra(i) #se va concatenando cada letra encriptada
    return cod