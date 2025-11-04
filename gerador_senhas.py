import random
import string

def gerar_senha(tamanho=10):
  caracteres = string.ascii_letters + string.digit + string.punctuation
  senha = ''.join(random.choices(caracteres) for i in range(tamanho))
  return senha

print("Sua senha gerada é:", gerar_senha())
