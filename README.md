# Projet

## But et interet du projet

Ce projet est un répondeur automatique d'email prenant appui sur la compréhension du langage naturelle des LLM (large language model) pour fournir des première version de mail automatiquement pour gagner du temps lors des réponse aux mails. L'intérêt personel dans ce projet était de ma familiariser avec l'utilisation de LLM via API, le prompt engeneering et autres concepts important lors de l'utilisation des LLM. 

## Fonctionalité du projet

Ce projet a été coder en python et se compose de quatres scripts principaux :
- **emailrecup.py** contient les fonctions qui permettent de se connecter à la boite mail de l'utilisateur via le protocol IMAP et y récupperer les messages non lu ainsi que celle qui traite ces mail pour en extraire les informations utiles (sujet du mail, envoyeur, corps du mail, et pièce jointe) et les formater dans un format JSON.

- **llmresponse** contient la fonction qui recoit le JSON d'un mail et qui, via l'API d'openrouter, utilise le modèle Gemma 3n4B de Google pour générer une réponse. Le prompt a été optimisé pour donner un maximum d'information sur le contexte et le format du mail qui lui est fourni et sur les consigne de ce qu'il doit rendre en retour. Le prompt utilisé permet également au LLM de laisser des placeholder que l'utilisateur peut remplir par exemple pour indiquer ses disponibilités ou ce qu'il a pensé d'un produit(le LLM ne pouvant évidement pas connaitre ces informations)

- **emailanswerer.py** contient la fonction pour envoyer automatiquement le mail en utilisant le protocole SMTP. 

- **main.py** est le script principal qui appel des fonctions précedement présentées. Il gère tout de la reception des email à leur envoi un fois traité. Il fonctionne ainsi : un while TRUE lui permet de tourner en continu si désiré avec une pause d'une durée réglable afin de ne pas saturé les serveurs mails. Il commence par aller récuperer les mails marqué 'non lu' dans la boite mail puis les traite automatiquement pour en extraire les informations impotantes. Tous les nouveaux emails sont ajouté à une liste puis chaque email de la liste est envoyé au LLM afin qu'il fournisse une première réponse. S'il a laissé des placeholders alors il est demandé à l'utilisateur de completer la phrase avec les informations qu'il est le seul a connaitre. Ensuite la réponse final prête à être envoyé est proposé et si l'utilisateur est satisfait elle est envoyé. Le programme attend ensuite la durée indiqué dans le time.sleep avant de checker pour de nouveaux email.


## Notes 

- Une adresse mail générique Mailo a été utilisé pour le développement de ce projet car il s'agit de l'option la plus simple, les boites gmail demandant plus d'autorisation afin de pouvoir s'y connecter automatiquement, c'est pourquoi il aura surement qelques légère modification si on veut l'utiliser pour une boite mail autre que Mailo (cependant la majorité des boite mail accèpte le protocole de connexion IMAP donc le code devrait être facilement adaptable).
- Pour réutiliser le code il vous faudra également crée votre propre API Key et setup votre .env.
- De nombreuse piste d'amélioration sont envisagées par exemple intégré des fonctionalités de text to speach afin que le programme nous lise les email recu ou les réponses du LLM et du speach to text poir ajouter oralement les informations de l'utilisateur dans les placeholder afin de completement libérer l'utilisateur pendant sa session de mail et qu'il puisse le faire en marchant par exemple. 

## Exemple d'utilisation

