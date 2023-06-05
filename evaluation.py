import chess


piece_values = {
    chess.PAWN: 150,
    chess.ROOK: 490,
    chess.KNIGHT: 270,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}


board = chess.Board(chess.STARTING_FEN)
white_material = 0
black_material = 0
def evaluate():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
            if piece.color == chess.WHITE:
                eval += piece_values[piece.piece_type]
            else:
                eval -= piece_values[piece.piece_type]
    return eval