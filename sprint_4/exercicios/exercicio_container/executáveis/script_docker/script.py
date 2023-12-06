import hashlib

def mascarar_dados(palavra):
    sha1 = hashlib.sha1()
    sha1.update(palavra.encode())
    hash_hex = sha1.hexdigest()
    return hash_hex

if __name__ == '__main__':
    palavra = input('Digite uma string: ')
    hash_hex = mascarar_dados(palavra)
    print(f"O hash da palavra '{palavra}' é: {hash_hex}")