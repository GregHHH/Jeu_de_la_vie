import string

def update_base(word, base):
    base = list(base)
    # tant que la base est plus courte que le mot-clé, on ajoute l'élement suivant de la base à la fin    
    for i in range(len(word) - len(base)):
        base.append(base[i % len(base)])
    return("" . join(base))	

def Encryption(word, base):
    encrypted_word = []
    # On met le mot en minuscule pour éviter les problèmes
    word = word.lower()
    # On recupère le code ascii de la première lettre du mot à crypter.
    start = ord('a')

	# grace à zip, on crée un dictionnaire où chaque n.ieme lettre du mot est lié à celle de la base au même rang
    for i, j in zip(word, base):

        # On garde la trace de notre progression dans le dictionnaire
        ptr = ord(i) - start
        pos = start + (ord(j) - start + ptr) % 26

        encrypted_word.append(chr(pos))
    return ''.join([j for j in encrypted_word])

# Le mot à crypter
word = "testa"
# La base utilisée pour crypter le mot
base = "abcd"

# Pour fonctionner, on a besoin que le nombre de caractères dans le mot à chiffrer soit le même que celui de la base dont on se sert pour decoder
# Pour le mot "banane" et la clé "abc", il faudrait que la clé devienne "abcabc"
if len(word) != len(base):
	base = update_base(word, base)

print(f"{word}, {base}") 
encrypted = Encryption(word, base) 