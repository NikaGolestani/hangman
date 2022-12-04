import random
a=random.randint(0,147)
b=random.randint(0,16)
f = open("words4.txt", "r")
c=f.readlines()[a]
c=c[:84]
d=c.split(" ")
word=d[b]
emptyword=["_ "]*len(word)
guessed=[]
i=0
prints=["______\n |    | \n |     \n |   \n |    \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |    \n |    \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   / \n |    \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   /| \n |    \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   /|\ \n |    \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   /|\ \n |    | \n |    \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   /|\ \n |    | \n |   /  \n_|_\n|   |______\n|          |\n|__________|",
        "______\n |    | \n |    O \n |   /|\ \n |    | \n |   / \ \n_|_\n|   |______\n|          |\n|__________|"]
while True:
    print(prints[i])
    if i ==7 or "_ " not in emptyword:
        break
    print("".join(emptyword)," | ",guessed)
    guess=input("Type letter:")
    if len(guess)==1 and guess not in guessed:
        if guess in word:
            for e in range(len(word)):
                if word[e]==guess:
                    emptyword[e]=guess
        else:
            guessed.append(guess)
            i+=1
if i<7:
    print("You WON!!!")
else:
    print("Maybe next time:(")
print("The word is",word.upper())
    
