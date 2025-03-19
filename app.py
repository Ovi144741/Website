import streamlit as st
import random

# Initialize session state variables
if "player1_score" not in st.session_state:
    st.session_state.player1_score = 0
if "player2_score" not in st.session_state:
    st.session_state.player2_score = 0
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
if "num2" not in st.session_state:
    st.session_state.num2 = random.randint(1, 10)
if "winner" not in st.session_state:
    st.session_state.winner = None
if "options" not in st.session_state:
    correct = st.session_state.num1 + st.session_state.num2
    wrong1 = correct + random.choice([-2, -1, 1, 2])
    wrong2 = correct + random.choice([-3, -1, 1, 3])
    st.session_state.options = random.sample([correct, wrong1, wrong2], 3)

# Generate a new question
def new_question():
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)
    correct = st.session_state.num1 + st.session_state.num2
    wrong1 = correct + random.choice([-2, -1, 1, 2])
    wrong2 = correct + random.choice([-3, -1, 1, 3])
    st.session_state.options = random.sample([correct, wrong1, wrong2], 3)

# Check if the answer is correct
def check_answer(player, answer):
    correct_answer = st.session_state.num1 + st.session_state.num2
    if answer == correct_answer:
        if player == 1:
            st.session_state.player1_score += 1
        else:
            st.session_state.player2_score += 1

    # Check if a player has won
    if st.session_state.player1_score >= 10:
        st.session_state.winner = "Player 1"
    elif st.session_state.player2_score >= 10:
        st.session_state.winner = "Player 2"
    else:
        new_question()

# Layout
st.title("🔢 Head-to-Head Math Quiz")
st.subheader("First to 10 points wins!")

if st.session_state.winner:
    st.success(f"🏆 {st.session_state.winner} Wins!")
    if st.button("Play Again"):
        st.session_state.player1_score = 0
        st.session_state.player2_score = 0
        st.session_state.winner = None
        new_question()
    st.stop()

# Player 2 (Flipped Layout for Opponent)
st.markdown("<h2 style='text-align: center; transform: rotate(180deg);'>Player 2</h2>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center; transform: rotate(180deg);'>{st.session_state.num1} + {st.session_state.num2} = ?</h3>", unsafe_allow_html=True)

# Player 2 Answer Buttons (Flipped)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button(f"🔄 {st.session_state.options[0]}", key="p2_opt1"):
        check_answer(2, st.session_state.options[0])
with col2:
    if st.button(f"🔄 {st.session_state.options[1]}", key="p2_opt2"):
        check_answer(2, st.session_state.options[1])
with col3:
    if st.button(f"🔄 {st.session_state.options[2]}", key="p2_opt3"):
        check_answer(2, st.session_state.options[2])

st.markdown(f"<h3 style='text-align: center; transform: rotate(180deg);'>Score: {st.session_state.player2_score}</h3>", unsafe_allow_html=True)

st.markdown("---")

# Player 1 (Normal Layout)
st.header("Player 1")
st.write(f"**Question:** {st.session_state.num1} + {st.session_state.num2} = ?")

# Player 1 Answer Buttons
col4, col5, col6 = st.columns(3)
with col4:
    if st.button(f"{st.session_state.options[0]}", key="p1_opt1"):
        check_answer(1, st.session_state.options[0])
with col5:
    if st.button(f"{st.session_state.options[1]}", key="p1_opt2"):
        check_answer(1, st.session_state.options[1])
with col6:
    if st.button(f"{st.session_state.options[2]}", key="p1_opt3"):
        check_answer(1, st.session_state.options[2])

st.write(f"Score: **{st.session_state.player1_score}**")
