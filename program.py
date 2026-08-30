# Fighting-game
It is an experimental project that allows me to learn to organize my ideas during programming . The hidden goal here is innovation , thanks to this contest , I can exploit my creativity to its full potential to increasingly optimize my game with new options . 
def attaquer(attacker, defender):
    degats = attacker["attaque"] - defender["defense"]
    if degats < 1:
        degats = 1
    defender["hp"] -= degats
    print(f"{attacker['nom']} frappe {defender['nom']} et inflige {degats} dégâts !")

def est_mort(p):
    return p["hp"] <= 0

def tour_joueur(player, monster):
    print("\n--- Ton tour ---")
    print("1. Attaquer")
    print("2. Se défendre")
    print("3. Potion")
    print("4. Fuir")

    choix = input("Choisis une action : ")

    if choix == "1":
        attaquer(player, monster)

    elif choix == "2":
        player["defense"] += 2
        print(f"{player['nom']} se défend ! Défense +2 pour ce tour.")

    elif choix == "3":
        if player["potion"] > 0:
            player["hp"] += 10
            player["potion"] -= 1
            print(f"{player['nom']} boit une potion ! HP +10.")
        else:
            print("Tu n'as plus de potions !")

    elif choix == "4":
        print("Tu fuis le combat !")
        return "fuite"

    return "continue"

def tour_monstre(monster, player):
    print("\n--- Le monstre attaque ! ---")
    attaquer(monster, player)

def combat(player, monster):
    print("Le combat commence !")

    while True:
        action = tour_joueur(player, monster)
        if action == "fuite":
            break

        if est_mort(monster):
            print(f"{monster['nom']} est vaincu !")
            break

        tour_monstre(monster, player)

        if est_mort(player):
            print(f"{player['nom']} est vaincu !")
            break

        print(f"\nHP de {player['nom']} : {player['hp']}")
        print(f"HP de {monster['nom']} : {monster['hp']}")
        print("-----")

player = {"nom": "Hero", "attaque": 30, "defense": 23, "hp": 40, "potion": 3}
monster = {"nom": "Titan", "attaque": 27, "defense": 28, "hp": 45}

combat(player, monster)
