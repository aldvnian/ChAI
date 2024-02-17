from Game import *

def doTurn():
    if Game.isInCheck():
        print("In check!")
        Game.isCheck = True
        Game.isCheckmate = Game.checkmate()

    if Game.isCheckmate:
        return

    if Game.currentPlayer == Game.player1:
        Board.displayBoard()
        Game.getInput()

        if Game.isCheck:
            while Game.isCheck:
                while not Game.validMove():
                    Board.displayBoard()
                    Game.getInput()
                tempPiece = Board.checkPiece(Game.moveX, Game.moveY)
                Game.move()
                if Game.isInCheck():
                    Game.undoMove(tempPiece)
                    print("Cannot do move which doesn't resolve check!")
                    Board.displayBoard()
                    Game.getInput()
                else:
                    Game.isCheck = False
        else:
            while not Game.validMove():
                Board.displayBoard()
                Game.getInput()
            Game.move()
        Game.swap()

    if Game.currentPlayer == Game.player2:
        engineBestMove = Game.chessEngine.findBestMove()
        Game.pieceX, Game.pieceY = engineBestMove[0]
        Game.moveX, Game.moveY = engineBestMove[1]
        Game.move()
        Game.swap()