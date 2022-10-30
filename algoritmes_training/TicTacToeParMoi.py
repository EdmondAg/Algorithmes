class TicTacToe:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        #self.rows = None
        #self.board = []
        self.alf = "ABCDEFGHJ"
        self.alf2 = "ABCDEFGHJ"
        self.count = 0

    # def create_board(self):
    #     for i in range(3):
    #         self.rows = []
    #         for j in range(3):
    #             j += i
    #             self.rows.append(self.alf[i + j])
    #         self.board.append(self.rows)

    def showBoard(self):
        print(self.alf[0:3])
        print(self.alf[3:6])
        print(self.alf[6:9])

    def start(self):
        while not self.isBoardFilled():
            self.count += 1
            self.showBoard()
            while True:
                cords1 = input("Player 1 turn: ")
                if self.alf[int(cords1)] != "X" or "O":
                    break
                print("Place already taken")
            self.player1 += self.alf[int(cords1)]
            self.alf[int(cords1)] = "X"

            self.showBoard()
            while True:
                cords1 = input("Player 2 turn: ")
                if self.alf[int(cords1)] != "X" or "O":
                    break
                print("Place already taken")
            self.player1 += self.alf[int(cords1)]
            self.alf[int(cords1)] = "O"

            if "ABC" in self.player1:
                print("Player 1 won")
            if "ABC" in self.player2:
                print("Player 2 won")
                break
            elif self.count == 9:
                break

  #  def printGameBoard(self):
    #    for i in range(len(self.board)):
      #      print(self.board[i])

    def isBoardFilled(self):
        for _ in self.alf:
            for e2 in self.alf2:
                if e2 == "-":
                    return False
        else:
            return True


# or "ADG" or "BEH" or "CFJ" or "DEF" or "GHJ" or "AEJ" or "CEG"
ell = TicTacToe()

ell.start()
