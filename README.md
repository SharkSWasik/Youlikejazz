# BeeWingIntersection
### Ce projet a été réalisé par Julien Cardon et Apolline Wasik


## Rappel du projet

Nous devons trouver les intersections des nervures d'ailes d'abeilles.

## Interprétation

Pour interpréter le code, il faut se placer à la racine du projet.

## Avec jupyter notebook

Il suffit d'éxécuter les cellules dans le fichiers main.ipynb et de remplacer les valeurs des variables src_dir et dst_dir qui correspondent respectivement aux dossiers contenant les images à segmenter et le dossier ou les résultat (csv) doivent être enregistrés.

## Sans jupyter notebook

Il faut se placer à la racine du projet. Il y a deux arguments pour spécifier le dossier contenant les images à segmenter (--src) et un autre (--dst) pour spécifier le dossier dans lequel les csv doivent être enregistrés.

```
python3 src/main.py --dst dst_path --src src_path

```
