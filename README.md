# YOULIKEJAZZ
https://www.youtube.com/watch?v=mqDOQzfM5Kc

### Ce projet a été réalisé par Julien Cardon et Apolline Wasik

## Rappel du projet

Nous devons trouver les intersections des nervures d'ailes d'abeilles.

# Pour utiliser docker
Pour build l'image
```
docker build -t "youlikejazz" .
```
Le dossier messources correspond aux dossier contenant les images des nervures à détecter, libre à vous de monter un dossier d'un autre nom.

```
docker run -v "$PWD"/messources/:/DATA/ -v "$PWD"/RESULTS/:/RESULTS/ --rm youlikejazz
```

Les csv seront automatiquement sauvegardés dans le dossiers RESULTS.

# Sans Docker

Le fichier requirements.txt contient toutes les dépendances nécessaires du projet.

## Interprétation

Pour interpréter le code, il faut se placer à la racine du projet.

## Avec jupyter notebook

Il suffit d'éxécuter les cellules dans le fichiers main.ipynb et de remplacer les valeurs des variables src_dir et dst_dir qui correspondent respectivement au dossier contenant les images à segmenter et le dossier où les résultats (csv) doivent être enregistrés.

## Sans jupyter notebook

Il faut se placer à la racine du projet. Il y a deux arguments pour spécifier le dossier contenant les images à segmenter (--src) et un autre (--dst) pour spécifier le dossier dans lequel les csv doivent être enregistrés.

```
python3 src/main.py --dst dst_path --src src_path

```
![maxresdefault](https://user-images.githubusercontent.com/36293875/129480394-6b7008bd-fda7-4214-9c03-201aff9d9e20.png)
