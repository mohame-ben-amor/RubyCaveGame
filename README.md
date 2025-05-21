# Jeu de la Grotte aux Rubis

Un jeu simple en Python où les joueurs collectent des rubis dans une grotte tout en évitant les pièges.

## Structure du Projet

```
.
├── constants.py           # Configuration et cartes
├── main.py               # Point d'entrée
├── models/               # Objets du jeu
│   └── player.py        # Classe Joueur
├── strategies/           # Stratégies
│   └── strategies.py    # Différentes façons de jouer
└── game/                # Logique du jeu
    └── game_manager.py  # Contrôleur principal
```

## Comment Jouer

1. Lancer le jeu:
   ```
   python main.py
   ```

2. Entrer le nombre de joueurs

3. Le jeu se joue automatiquement:
   - Joueur 1 utilise la Stratégie Basique
   - Les autres joueurs utilisent la Stratégie Aléatoire

## Règles du Jeu

- 5 manches
- Les joueurs collectent des rubis
- Les joueurs doivent décider quand quitter:
  - Sortie sûre = garde les rubis
  - Deuxième piège = perte des rubis
- Le joueur avec le plus de rubis gagne

## Types de Cartes

1. Cartes Rubis (nombres):
   - Donnent des rubis aux joueurs actifs
   - Rubis restants restent dans la grotte

2. Cartes Pièges:
   - Premier piège: aucun effet
   - Deuxième piège: perte des rubis

3. Cartes Reliques:
   - Donnent des points bonus
   - Seul le dernier joueur sortant les obtient

## Structure du Code

### Classe Joueur
- Gère les rubis et le statut
- Suit les rubis en main et en coffre
- Gère la sortie de la grotte

### Stratégies
1. Stratégie Basique:
   - Décisions basées sur:
     - Nombre de cartes jouées
     - Nombre de pièges
     - Rubis au sol

2. Stratégie Aléatoire:
   - Décisions simples basées sur:
     - Rubis en main
     - Cartes restantes
     - Numéro de la manche

### Gestionnaire de Jeu
- Contrôle le déroulement
- Gère les manches et tours
- Gère les effets des cartes
- Suit les scores

## Comment Modifier

1. Ajouter une stratégie:
   ```python
   class MaStrategie:
       def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
           if mon_sac > 10:
               return True
           return False
   ```

2. Changer les règles:
   - Modifier `constants.py`
   - Mettre à jour `game_manager.py`

3. Ajouter des fonctionnalités:
   - Ajouter des méthodes à `Player`
   - Mettre à jour `GameManager`

## Exemple de Stratégie

```python
class MyStrategy:
    def play(self, mon_coffre, mon_sac, rubis_au_sol, id_manche, les_joueurs, tas_tri, defausse):
        # Leave if we have more than 10 rubies
        if mon_sac > 10:
            return True
        # Stay otherwise
        return False
``` 