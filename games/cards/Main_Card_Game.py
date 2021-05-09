from games.cards.Class_Card_Game import Card_Game
from games.cards.Class_Player import Player

player1 = Player(input("player 1 name: "))
player2 = Player(input("player 2 name: "))
game1 = Card_Game(player1.name,player2.name)
print(game1.player1.show())
print(game1.player2.show())

for i in range(10):
    card1 = game1.player1.get_card()
    card2 = game1.player2.get_card()
    print(card1)
    print(card2)

    if card1 < card2:
        game1.player2.add_card(card1)
        game1.player2.add_card(card2)
        print(f"{player2.name} has won")
    else:
        card2 < card1
        game1.player1.add_card(card1)
        game1.player1.add_card(card2)
        print(f"{player1.name} has won")
