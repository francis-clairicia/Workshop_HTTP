# Workshop HTTP requests
## Des requêtes HTTP en Python ?
Tout à fait ! Ce n'est pas réservé aux amateurs de PHP et JavaScript. Le protocole HTTP étant une norme standard et documentée via [la RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616) est implémentable dans tout langage supportant le réseau ! (Oui oui, même le C)

Par conséquent on peut faire des requêtes HTTP dès que le protocole est respecté.

> Donc on devra réimplémenter le protocole ?

Certainement pas ! En C oui on aurait du le faire, mais Python lui contient déjà une implémentation dans sa bibliothèque standard (le module [http](https://docs.python.org/3/library/http.html) pour l'implémentation de la RFC, et [urllib](https://docs.python.org/3/library/urllib.html) pour faire des requêtes via une URL)

> La documentation est complexe quand même...

Oui. C'est un peu galère quand on est nouveau dans le domaine. Mais heureusement, des développeurs indépendants ont conçu un module python du nom de [`requests`](https://docs.python-requests.org/en/latest/) permettant de faire des requêtes HTTP très facilement.

## Installation
Tout d'abord, vérifiez que Python 3 (de préférence >= 3.8) soit installé
```sh
python --version
```
Ensuite installez le package `requests`
```sh
python -m pip install --user --upgrade requests
```

## Une requête HTTP ?
Oui j'aurais peut-être dû commencer par là X)

Une requête HTTP consiste à faire une action sur un serveur distant via un URL. Ce dernier nous renvoie une réponse appoprié selon la situation.

Le plus banal est tout simplement votre navigateur qui a fait une requête HTTP à Github pour vous renvoyer le README.md que vous êtes en train de lire actuellemennt, et ce dans un joli HTML/CSS :)

### Les méthodes HTTP
> HTTP définit un ensemble de méthodes de requête qui indiquent l'action que l'on souhaite réaliser sur la ressource indiquée. Bien qu'on rencontre également des noms (en anglais), ces méthodes sont souvent appelées verbes HTTP. Chacun d'eux implémente une sémantique différente mais certaines fonctionnalités courantes peuvent être partagées par différentes méthodes (e.g. une méthode de requête peut être sûre (safe), idempotente ou être mise en cache (cacheable)).
> 
> -- <cite>https://developer.mozilla.org/fr/docs/Web/HTTP/Methods</cite>

Il en existe plusieurs, et je vous invite à aller sur le site de Mozilla pour les details. Mais en résumé il y en a 4 pour que vous utiliserez la plus part du temps, dont 2 _tout le temps_ :
- `GET` : Demander une ressource au serveur (indispensable)
- `POST` : Ajouter une ressource dans le serveur (Difficile de faire les 2 autres sans voir fait celui-ci au moins une fois)
- `PATCH` : Modifier une ressource **déjà présente** dans le serveur
- `DELETE` : Supprimer une ressource du serveur

(Certains utilisent `PUT` mais ce n'est pas toujours le cas)

Les autres méthodes sont beaucoup plus spécifiques. Je vous laisse faire vos recherches dessus.

### Les paramètres de requêtes (ou Query params)
Vous avez déjà une URL, comme celui-ci : https://github.com/francis-clairicia/PyDiamond

Ou encore comme celui-ci : https://github.com/francis-clairicia/Py-Game-Case

Ou bien même celui-là : https://github.com/francis-clairicia/Traffic_Racing_2D

Bon ok je force X)  (Mettez des stars svp)

Ça se décompose en :
- Schema : `http` ou `https` (Mais il en existe plein)
- Addresse : `github.com` (dans notre cas)
- Route : Litteralement tout ce qu'il y a après le `/`

Mais il se peut que vous ayez déjà vu ceci : https://github.com/search?q=pygame  (Bon ok ça fait beaucoup)

le `?q=pygame` vous dit quelque chose ? Cette partie de l'URL est le `query parameter`. On les reconnais quand on mets un `?` dans une URL. S'en suivent des paires de clé/valeurs à traiter durant la requête.

Dans cet exemple, il n'y en a qu'un seul (`q=pygame`) mais il peut bien évidemment en avoir plusieurs comme ça : https://github.com/search?q=pygame&type=topics

On se sert de `&` pour séparer les différentes assignations dans l'URL.

### Les corps de requêtes (ou request body)
Dans le cas des méthodes `POST` et `PATCH` (et `PUT` mais t'inquiètes il n'existe pas), les requêtes devront avoir un _request body_. Le corps de requête est justement la donnée à envoyer au serveur.

> Pourquoi ne pas les donner en paramètres de requête ?

Pour une raison simple : http://fakesite.com/register?username=John+Doe&password=the-john-doe

Si tu ne vois pas où est le problème, je ne peux plus rien pour toi X)

## Passons au code !
Du coup comment on se sert de `requests` ?

Déjà, pour les premiers exercices, vous verrez ceci :

```py
import requests
```
C'est une bonne entame je trouve :)

J'aurais beau vous expliquer comment ça marche, je ne serai jamais aussi complet et clair que la documentation elle-même

Du coup je vous conseille vivement d'aller là : https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request

(Je préciser au cas où, tous les `>>>` en préfixe viennent du Python shell. Si vous exécutez `python` tout seul vous allez tomber dessus)

### A vous de jouer
Faites les 3 premiers exercices (de `ex00.py` à `ex02.py`). Les instructions sont au début du code. Une fois fini, passez à la suite.

## Créer un `github-cli`
Vous vous êtes jamais dit que ce serait cool d'avoir des infos de Github sans avoir constamment à ouvrir une page web ?

Ce serait cool qu'on puisse lancer un binaire/un script sur notre PC qui va automatiquement récuperer/envoyer des données, non ?

Bah c'est tout à fait possible ! Histoire de voir comment ça marche, les prochains exercices porteront sur la récupération d'informations sur Github.

### Créer votre Personal Access Token
Il y a 2 moyens de s'authentifier sur l'API Github
- via username/password : Bon a moins que vous connaissiez la cryptographie, je ne suis pas sûr que vous voulez mettre votre mdp en clair dans votre code.
- via un token : Un charabia sur 32 lettres minimum que reconnaîtra Github

Les avantages du token :
- Il peut être réglé pour être expiré au bout d'un certain temps
- On peut donner explicitement les droits d'accès quand on s'en sert.

Pour créer votre access token:
- Allez dans les paramètres de votre compte github, dans `Developer settngs`, puis dans `Personal access token`
- Faites `Generate new token`
- Mettez ce que vous voulez comme description ou temps d'expiration
- Pour les permissions, mettez au minimum `user` et `repo` (Cochez toutes les sous-cases aussi) pour les besoins du workshop
- Validez !

Pour les permissions, il est toujours possible de les modifier. Ce n'est pas à vie non plus.

Du coup votre nouveau token, copiez-le et mettez-le dans un fichier `github.token` à côté des exercices. (Faites le maintenant parce qu'après Github ne vous laissera plus jamais le voir clairement).

Au passage, faites `Configure SSO` pour donner les droits aux organisations Epitech, vous en aurez besoin pour l'exercice 05 :)

### Les Sessions
Je ne vais pas m'attarder là-dessus, mais c'est juste pour que vous compreniez pourquoi à partir de l'exercice 03, il y a un `GithubSession` qui est apparu de nul part !

Les `Session` sont des objets permettant d'avoir des valeurs par défaut à utiliser au moment d'une requête.

Vous n'alliez pas vous amuser à passer votre token en paramètre à chaque fois, si ? :)

Sachez juste que pour les prochains exercices, au lieu de ...
```py
response = requests.get("http://fakesite.com/user")
```
... vous devrez faire :
```py
response = SESSION.get("http://fakesite.com/user")
```

Et comme ça vous laissez le soin à Python (et à `requests` entre autres) de donner votre token en paramètres, histoire de ne pas se faire rejeter par Github :)

Pour plus d'infos : https://docs.python-requests.org/en/latest/user/advanced/#session-objects

### A vous de jouer
Faites les derniers exercices !

## Conclusion
Savoir faire des requêtes HTTP est devenu un _must have_ pour un développeur de nos jours, que ce soit en tant que Web Developer (ce serait dommage du contraire aussi), ou en étant développeur dans un autre domaine. Ça permet littéralement d'interagir avec Internet ! Bon nombre de scripts et d'automatisation sont basés là-dessus afin d'avoir une expérience optimale pour un service (tel que Github par exemple).

Je peu vous assurer que maitriser cet art ne vous sera que bénéfique :)
