import random
import string

def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    return senha

print("Sua senha gerada é:", gerar_senha())

