import streamlit as st

# Define a list of riddles
riddles = [
    {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        "answer": "An Echo"},
    {
        "question": "I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, and I can drown. What am I?",
        "answer": "Fire"},
    {"question": "The more of this there is, the less you see. What is it?", "answer": "Darkness"},
    {"question": "What has keys but can't open locks?", "answer": "A Piano"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
     "answer": "The letter 'M'"},
]

# Set up the Streamlit page
st.title("Riddles Game")
st.markdown("Welcome to the riddles game! Try to solve the following riddles:")

# Display riddles and get answers from the user
score = 0
for i, riddle in enumerate(riddles):
    st.subheader(f"Riddle {i + 1}:")
    st.write(riddle['question'])

    # Input box for the answer
    user_answer = st.text_input(f"Your answer for Riddle {i + 1}:")

    # Check the answer and give feedback
    if user_answer.lower() == riddle["answer"].lower():
        st.success("Correct!")
        score += 1
    elif user_answer != "":
        st.error("Wrong answer!")

# Display the user's score at the end
if st.button("Check your score"):
    st.write(f"Your score is: {score}/{len(riddles)}")
