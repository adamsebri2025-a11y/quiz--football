questions = [
  {
    "question": "Combien de joueurs dans une equipe ?",
    "choix": ["A) 9", "B) 10", "C) 11", "D) 12"],
    "reponse": "C"
  },
  {
    "question": "Vainqueur Coupe du Monde 2022 ?",
    "choix": ["A) France", "B) Bresil", "C) Allemagne", "D) Argentine"],
    "reponse": "D"
  },
  {
    "question": "Duree d'un match de football ?",
    "choix": ["A) 80 min", "B) 90 min", "C) 100 min", "D) 120 min"],
    "reponse": "B"
  },
  {
    "question": "Distance d'un penalty ?",
    "choix": ["A) 9m", "B) 11m", "C) 13m", "D) 16m"],
    "reponse": "B"
  },
  {
    "question": "Club avec le plus de Ligues des Champions ?",
    "choix": ["A) Barcelona", "B) Bayern", "C) Real Madrid", "D) Liverpool"],
    "reponse": "C"
  },
{
    "question": "Combien de Ballons d'Or pour Messi ?",
    "choix": ["A) 5", "B) 6", "C) 7", "D) 8"],
    "reponse": "D"
  },
  {
    "question": "Quel pays a invente le football ?",
    "choix": ["A) France", "B) Espagne", "C) Angleterre", "D) Bresil"],
    "reponse": "C"
  },
  {
    "question": "Combien de cartons jaunes = expulsion ?",
    "choix": ["A) 1", "B) 2", "C) 3", "D) 4"],
    "reponse": "B"
  },
  {
    "question": "Coupe du Monde 2026 : quel pays ?",
    "choix": ["A) Espagne", "B) USA/Canada/Mexique", "C) Qatar", "D) Australie"],
    "reponse": "B"
  },
  {
    "question": "Meilleur buteur Coupe du Monde histoire ?",
    "choix": ["A) Pele", "B) Messi", "C) Ronaldo", "D) Klose"],
    "reponse": "D"
  },
]

def jouer():
  print("=" * 42)
  print(" QUIZ FOOTBALL - Adam et Ghassen")
  print("=" * 42)
  nom = input("Ton prenom : ")
  score = 0
  for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}/10 : {q['question']}")
    for c in q["choix"]:
      print(c)
    rep = input("Reponse (A/B/C/D) : ").upper()
    if rep == q["reponse"]:
      print("Bonne reponse !")
      score += 1
    else:
      print(f"Mauvaise ! Bonne reponse : {q['reponse']}")
  print(f"\nScore de {nom} : {score}/10")

jouer()