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
  # Ghassen ajoutera ses 5 questions ici 
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