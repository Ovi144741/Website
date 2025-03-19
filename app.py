import streamlit as st
import pandas as pd

# Function to display Banglish lessons
def show_banglish():
    st.subheader("Banglish (English Transliteration)")
    banglish = {
        "English": [
            "Hello", "How are you?", "Thank you", "Goodbye", "What is your name?", "My name is...",
            "Where are you from?", "I am from...", "How much is this?", "I don't understand",
            "Can you help me?", "I love you", "See you later", "Good morning", "Good night",
            "Excuse me", "Sorry", "Yes", "No", "Please", "What time is it?", "Where is the bathroom?",
            "How do I get there?", "I need help", "Can you repeat that?", "I am learning Bengali", "Nice to meet you",
            "How old are you?", "I am ... years old", "Do you speak English?", "I speak a little Bengali",
            "Where can I find food?", "This is delicious", "I like this", "I don’t like this", "What is this?",
            "Can you recommend something?", "How much does it cost?", "I am lost", "I am tired", "I am happy",
            "I am sad", "I am hungry", "I am thirsty", "What is the weather like?", "Be careful", "Congratulations!",
            "Happy birthday", "Happy new year", "Good luck", "Have a nice day", "I will be back soon", "Take care",
            "See you tomorrow", "Let’s go", "Do you understand?", "I understand", "I don’t know", "Where is the bus stop?",
            "Can you write it down?", "I need a doctor", "Call the police", "It’s an emergency", "Everything is fine",
            "What’s happening?", "Can I have the bill, please?", "Do you accept credit cards?", "Where can I buy this?",
            "It’s too expensive", "Can you lower the price?", "That’s a good deal", "What do you recommend?",
            "I am looking for a hotel", "Where is the nearest hospital?", "I need a taxi", "How far is it?",
            "Do you have a menu?", "What’s your favorite food?", "I am allergic to...", "Can I try this on?",
            "Where is the market?", "I would like to buy...", "What’s your phone number?", "Can I take a photo?",
            "I am married", "I am single", "Do you have children?", "Let’s be friends", "I am busy",
            "What do you do for work?", "Where do you live?", "I need some rest", "I am having fun", "That’s interesting",
            "I need water", "Where can I find a bus?", "This is my first time here", "Can you show me the way?",
            "Where is the nearest ATM?", "What is your favorite place?", "Can I get a discount?"
        ],
        "Banglish": [
            "Assalamualaikum", "Apni kemon achen?", "Dhonnobad", "Alo bidai", "Apnar naam ki?", "Amar naam...",
            "Apni kotha theke aschen?", "Ami ... theke aschi", "Eta koto taka?", "Ami bujhte parchina",
            "Apni ki amake shahajjo korte parben?", "Ami tomake bhalobashi", "Pore dekha hobe", "Shuprobhat", "Shubho raatri",
            "Dukkho korchi", "Maaf korben", "Haan", "Na", "Doyakore", "Ekhon kotota baje?", "Toilet kothay?",
            "Kivabe jabo?", "Amar shahajjo dorkar", "Apni ki abar bolte parben?", "Ami Bangla shikhchi", "Apnar shathe dekha hoye bhalo laglo",
            "Apnar boyosh koto?", "Amar boyosh ...", "Apni ki English bolte paren?", "Ami ektu Bangla bolte pari",
            "Kothay khabar pabo?", "Eta khub moja", "Eta bhalo laglo", "Eta bhalo laglo na", "Eta ki?",
            "Apni ki kono suggestion dite paren?", "Eta koto dam?", "Ami hariye gechi", "Ami klanto", "Ami khushi",
            "Ami dukkhito", "Ami khide peyeche", "Ami tesh to", "Akal somoy ki rokom?", "Shabdhan thakun", "Abhinondon!",
            "Shubho jonmodin", "Shubho noboborsho", "Shubho kamona", "Shubho din hok", "Ami shighroi fire ashbo", "Nije ke shambhalun",
            "Agami kal dekha hobe", "Cholon jabo", "Apni ki bujhte perechen?", "Ami bujhte perechi", "Ami jani na", "Bus stop kothay?",
            "Apni ki eta likhe dite parben?", "Amar doctor dorkar", "Police ke dakun", "Ekhon joruri obostha", "Shob thik ache",
            "Ki hocche?", "Amar bill ta deben?", "Apni ki credit card niben?", "Eta kothay kinte parbo?",
            "Eta onek dami", "Apni ki daam komate parben?", "Eta bhalo deal", "Apni ki suggest korte parben?",
            "Ami hotel khujchi", "Kothay najdik hospital?", "Amar ekta taxi dorkar", "Eta koto dur?",
            "Apnar menu ache?", "Apnar priyo khabar ki?", "Ami ... te allergy achi", "Ami eta porbo?",
            "Bazaar kothay?", "Ami ... kinbo", "Apnar phone number ki?", "Ami ekta chhobi tulte pari?",
            "Ami biye korechi", "Ami akek", "Apnar ki shontan ache?", "Cholon bondhu hoi", "Ami byasto",
            "Apni ki kaj koren?", "Apni kothay thaken?", "Amar ekto bishram dorkar", "Ami moja pachchi", "Eta moja",
            "Amar pani dorkar", "Kothay bus pabo?", "Eta amar prothom bar ekhane asha", "Apni ki amake rasta dekhiye dite parben?",
            "Kothay najdik ATM?", "Apnar priyo jaiga konta?", "Ami ki ekta discount pabo?"
        ]
    }
    df = pd.DataFrame(banglish)
    st.table(df)

# Streamlit App
st.title("Learn Bengali Language")

menu = ["Banglish"]
choice = st.sidebar.selectbox("Select a section", menu)

if choice == "Banglish":
    show_banglish()

st.write("Enjoy learning Bengali!")
