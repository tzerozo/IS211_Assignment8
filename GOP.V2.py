#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IS211 Week8 (10/12/2020 - 10/18/2020)  "Game of Pig with Design Patterns"
#Lang | 10/19/2020
#Adding classes(subclasses as well) to make the game playable with Computer.

import argparse
import random
import sys
import time

#####Rolling Dice class.
class Dice:
    """Generates random number from 1 to 6."""
    def __init__(self):
        self.number = int()
        seed = 0

    def roll_dice(self):
        """To roll a dice."""
        self.number = random.randint(1,6)
        return self.number

#####Base Class for Player.
class Player:
    """ Attributes and Behaviors of players."""
    def __init__(self):
        self.turn = False
        self.hold = False
        self.roll = True
        self.total_points = 0

    def choose(self):
        """Keep rolling or holding it."""
        question = input("Do you want to keep rolling or hold it?")
        if question == 'r':
            self.roll = True
            self.hold = False
        elif question == 'h':
            self.roll = False
            self.hold = True
        else:
            print("Please enter either 'r' or 'h'!")
            self.choose

#####New this week.
#####Subclass of Player class for computer player.
class ComputerPlayer(Player):
    """A strategy for computer to hold or roll."""
    def ComputerDecision(self):
      #(hold)if <25 and 100-x (x = score)
        if 25 < 100 - self.total_points:
            hold_num = 25
        else:
            hold_num = 100 - self.total_points

        if self.total_points < hold_num:
            return 'r'
        elif self.total_points >= hold_num:
            return 'h'

#####New this week.
#####Factory Design Patterns.
class PlayerFactory():
    """To instantiate the correct Player class."""
    def __init__(self):
        return None
    def selectplayer(self, typeofplayer):
        """To check the type of player."""
        if typeofplayer == 'h':
            return Player("Human Gamer")
        elif typeofplayer == 'c':
            return ComputerPlayer()
        else:
            print("Uh oh!!! something went wrong....")


class Game:
    """To play the game."""
    def __init__(self,player1,player2,dice):
        self.player1 = player1
        self.player2 = player2
        self.player1.name  = 'Gamer1'
        self.player2.name  = 'Gamer2'
        self.player1.score = 0
        self.player2.score = 0
        self.total_points = 0
        self.dice = dice

        ask = input("Do you wanna play first, enter y or n: ")
        if ask == 'y':
            self.currentplayer = player1
            print("Gamer1 will begin")
        elif ask == 'n':
            self.currentplayer = player2
            print("Gamer2 will begin")
        self.switch()

    def next_player(self):
        self.total_points = 0
        if self.player1.score >= 100:
            print("Gamer1 has won!!!")
            sys.exit()
        elif self.player2.score >= 100:
            print("Gamer2 has won!!!")
            sys.exit()
        else:
            if self.currentplayer == self.player1:
                self.currentplayer = self.player2
            elif self.currentplayer == self.player2:
                self.currentplayer = self.player1
        print(self.currentplayer.name, "Will take turn")
        self.switch()

    def switch(self):
        """Taking turn of rolling"""
        print("Gamer1's total_points: ", self.player1.score)
        print("Gamer2's total_points: ", self.player2.score)
        self.dice.roll_dice()
        if self.dice.number == 1:
            print("Sorry you rolled 1, we will forfeit your turn")
            self.total_points = 0
            self.next_player()
        else:
            self.total_points += self.dice.number
            print(self.dice.number," is rolled, you will earn the points")
            print("Your current score for this turn is ", self.total_points)
            self.currentplayer.choose()
            if self.currentplayer.hold == True and self.currentplayer.roll == False:
                self.currentplayer.score += self.total_points
                self.next_player()
            elif self.currentplayer.hold == False and self.currentplayer.roll == True:
                self.switch()

#####New this week.
#####Class for timed version of the game.At 1min, more points win.
class TimedGameProxy(Game):
    """To have a timed(1 min)game so that winner can be announced."""
    def __init__(self):
        self.start = time.time()
        Game.__init__(self,player1,player2)

    def timechecker(self):
        """To check time."""
        if time.time() - self.start >= 60:
            if self.player1.total_points > self.player2.total_points:
                print("Game Over, {} wins with {} points".format(self.player1.name,self.player1.total_points))
            else:
                print("Game Over, {} wins with {} points".format(self.player2.name,self.player2.total_points))
        else:
            sys.exit()

    def next_player(self):
        self.total_points = 0
        if self.player1.score >= 100:
            print("Gamer1 has won!!!")
            sys.exit()
        elif self.player2.score >= 100:
            print("Gamer2 has won!!!")
            sys.exit()
        else:
            if self.currentplayer == self.player1:
                self.currentplayer = self.player2
            elif self.currentplayer == self.player2:
                self.currentplayer = self.player1
        print(self.currentplayer.name, "Will take turn")
        self.switch()

    def switch(self):
        """Taking turn of rolling"""
        print("Gamer1's total_points: ", self.player1.score)
        print("Gamer2's total_points: ", self.player2.score)
        self.dice.roll_dice()
        if self.dice.number == 1:
            print("Sorry you rolled 1, we will forfeit your turn")
            self.total_points = 0
            self.next_player()
        else:
            self.total_points += self.dice.number
            print(self.dice.number," is rolled, you will earn the points")
            print("Your current score for this turn is ", self.total_points)
            self.currentplayer.choose()
            if self.currentplayer.hold == True and self.currentplayer.roll == False:
                self.currentplayer.score += self.total_points
                self.next_player()
            elif self.currentplayer.hold == False and self.currentplayer.roll == True:
                self.switch()

#####To start a new game
def GameofPig():
    begin = input("Are you ready? Enter: y or n: ")
    if begin == 'y':
        player1 = Player()
        player2 = Player()
        dice = Dice()
        start = Game(player1,player2,dice)
    elif begin == 'n':
        print ("Cool,have a nice time!")
        sys.exit()
    else:
        print("You must enter 'y' or 'n'")
        GameofPig()
    
def main():
    """To start the program/game"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', help='Chooose type of player: human or computer')
    parser.add_argument('--player2', help='Choose type of player: human or computer')
    parser.add_argument('--timed', help='Game will last 1 minute')
    args = parser.parse_args()

    if args.timed:
        timed = TimedGameProxy()
    else:
        regular = GameofPig()
    

if __name__ == '__main__':
    main()
