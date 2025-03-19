import streamlit as st
import random


def main():
    st.title("Simple Game Website")
    st.header("Guess the Number Game")

    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)

    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0

    if 'leaderboard' not in st.session_state:
        st.session_state.leaderboard = []

    difficulty = st.radio("Select Difficulty:", ("Easy", "Medium", "Hard"))

    if difficulty == "Easy":
        max_value = 100
    elif difficulty == "Medium":
        max_value = 500
    else:
        max_value = 1000

    guess = st.number_input(f"Enter your guess (1-{max_value}):", min_value=1, max_value=max_value, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.write("Too low! Try again.")
        elif guess > st.session_state.number:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.leaderboard.append(st.session_state.attempts)
            st.session_state.leaderboard.sort()

            st.session_state.number = random.randint(1, max_value)  # Reset the game
            st.session_state.attempts = 0  # Reset attempts

    st.subheader("Leaderboard (Top 5 Scores)")
    for i, score in enumerate(st.session_state.leaderboard[:5]):
        st.write(f"{i + 1}. {score} attempts")


if __name__ == "__main__":
    main()
