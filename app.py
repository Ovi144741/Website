import streamlit as st
import numpy as np


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None


def is_board_full(board):
    return all(cell != "" for row in board for cell in row)


def reset_game():
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X"


def main():
    st.title("Two Player Tic-Tac-Toe")

    if 'board' not in st.session_state or 'turn' not in st.session_state:
        reset_game()

    winner = check_winner(st.session_state.board)
    if winner:
        st.success(f"Player {winner} wins!")
        if st.button("Restart Game"):
            reset_game()
        return

    if is_board_full(st.session_state.board):
        st.warning("It's a draw!")
        if st.button("Restart Game"):
            reset_game()
        return

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if cols[j].button(st.session_state.board[i][j] if st.session_state.board[i][j] else " "):
                if not st.session_state.board[i][j]:
                    st.session_state.board[i][j] = st.session_state.turn
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                    st.experimental_rerun()


if __name__ == "__main__":
    main()
