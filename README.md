# 🔐 DICT-GENERATOR

**DICT-GENERATOR** est une application Python avec interface graphique (Tkinter) permettant de générer des dictionnaires personnalisés, utilisés dans les tests de sécurité de mots de passe via brute force.

## 🚀 Fonctionnalités

- Interface graphique élégante et intuitive (Tkinter + thème personnalisé)
- Génération de toutes les combinaisons possibles de lettres et chiffres
- Personnalisation des longueurs minimales et maximales
- Fichier `.txt` généré prêt à être utilisé avec des outils comme Hydra, John the Ripper, etc.
- Messages de statut et alertes d'erreurs claires
- Sécurité : avertissement en cas de taille de dictionnaire potentiellement trop grande

## 🖥️ Capture d’écran
<p align="center">
  <img src="gui.png" alt="Aperçu de l'application" width="500"/>
</p>

  
## 🛠️ Installation

```bash
git clone https://github.com/christianADE/dict-generator.git
cd dict-generator
pip install -r requirements.txt
python main.py
