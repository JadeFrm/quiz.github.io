# Quizz

name = input("Quel est votre nom ? ")

print("Bienvenu,"+name+"! Le questionnaire va commencer. Contentez vous de répondre A, B ou C !")
print("Première question :")

print("Quelle est la définition du mot, 'lapalissade' ?")
print("A : Un endroit encerclé de palissade.")
print("B : Une vérité trop évidente.")
print("C : Boire d'un seul trait.")
answer1 = input("Réponse : ")

if answer1 == "B":
    print("Exact ! Je vous donne un exemple, 'Je suis faite pour votre établissement !'")
elif answer1 == "b":
    print("Exact ! Je vous donne un exemple, 'Je suis faite pour votre établissement !'")
else:
    print("Loupé ! Une lapalissade est une vérité trop évidente. Par exemple : 'Je suis faite pour votre établissement !'")

print("Quel est le prénom de votre future étudiante ?")
print("A : Marie")
print("B : Lola")
print("C : Jade")
answer2 = input("Réponse : ")

if answer2 == "C":
    print("Vous êtes malin vous !")
elif answer2 == "c":
    print("Vous êtes malin vous !")
else:
    print("... C'était pas vraiment la réponse attendu... Enfin bon, passons...")

print("Dernière question")
print("Parmis les 3 qualitées suivantes, qu'elle est celle que vous attendez le plus chez vos élèves ?")
print("A : Persévérance")
print("B : Curiosité")
print("C : Autonomie")
answer3 = input("Réponse : ")

if answer3 == "A":
    print("Quelle coincidence ! Persévérance est mon deuxième prénom.")
if answer3 == "a":
    print("Quelle coincidence ! Persévérance est mon deuxième prénom.")
if answer3 == "B":
    print("C'est génial, justement la curiosité est l'un de mes défauts !")
if answer3 == "b":
    print("C'est génial, justement la curiosité est l'un de mes défauts !")
if answer3 == "C":
    print("Ca tombe bien, il arrive que j'aime travailler seule !")
if answer3 == "c":
    print("Ca tombe bien, il arrive que j'aime travailler seule !")


print("Merci d'avoir joué "+name+"! J'éspère pouvoir dire à bientôt dans votre établissement !")