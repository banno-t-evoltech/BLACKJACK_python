# coding: utf8

import random

# カードクラス
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"

# デッキクラス
class Deck:
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

# プレイヤークラス
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    #点数計算
    def calculate_hand(self):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        result = 0
        aces = 0
        for card in self.hand:
            result += values[card.rank]
            if card.rank == 'A':
                aces += 1
        while result > 21 and aces:
            result -= 10
            aces -= 1
        return result

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

# ブラックジャックのゲームクラス
class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

# 初期のカード配布
    def play(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

        print(f"Player's hand: {self.player.show_hand()} (Total: {self.player.calculate_hand()})")
        print(f"Dealer's hand: {self.dealer.hand[0]}, Hidden")

# プレイヤー
        while self.player.calculate_hand() < 21:
            action = input("Hit or Stand? (hit/stand): ").lower()
            if action == 'hit':
                self.player.add_card(self.deck.draw_card())
                print(f"Player's hand: {self.player.show_hand()} (Total: {self.player.calculate_hand()})")
            else:
                break

# ディーラー
        while self.dealer.calculate_hand() < 17:
            self.dealer.add_card(self.deck.draw_card())

        print(f"Dealer's hand: {self.dealer.show_hand()} (Total: {self.dealer.calculate_hand()})")

# 勝敗
        player_total = self.player.calculate_hand()
        dealer_total = self.dealer.calculate_hand()

        if player_total > 21:
            print("あなたはバーストしました。ディーラの勝利です。")
        elif dealer_total > 21 or player_total > dealer_total:
            print("あなたの勝利です。")
        elif player_total < dealer_total:
            print("ディーラーの勝利です。")
        else:
            print("同点です。")

if __name__ == "__main__":
    game = BlackJackGame()
    game.play()
