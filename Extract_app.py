import streamlit as st
import time

# Page config

st.set_page_config(page_title="Love Calculater 💘", page_icon="💘", layout="centered")

# Custom background
st.markdown("""
    <style>
        .stApp {
            background-image: linear-gradient(135deg, #ffc0cb, #fff0f5);
            background-size: cover;
            font-family: 'Comic Sans MS', cursive;
            color: #800000; /* Romantic deep red for all text */
        }

        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .css-1q8dd3e {
            color: #800000 !important;
        }

        .stTextInput input {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


st.title("👩‍❤️‍💋‍👨 Simple Love Calculater")



st.markdown("""
> ⚠️ **Disclaimer**  
> This app is designed purely for entertainment purposes. The love score it generates is based on a playful formula and doesn't reflect any real emotional compatibility.  
> Please don't take it too seriously or judge anyone by the results—it's all in good fun! 💖  
""")


name1 = st.text_input("Enter Your Name: ", placeholder= "e.g. Rahul")
name2 = st.text_input("Enter Your Loved one Name: ", placeholder= "e.g. Anjali")

if st.button("💖 Calculate Love Score"):
    if name1 and name2:
        combined = (name1 + name2).lower()
        true_score = sum(combined.count(char) for char in "true")
        love_score = sum(combined.count(char) for char in "love")
        
        final_score = true_score *10 +love_score
        
        # Colorful progress bar
        progress_text = "Matching your romantic vibes... 💌"
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)

        
        st.markdown("---")
        st.subheader("💖 Your Love Score is: ")
        st.markdown(f"<h1 style= 'text-align: center; color:red; '>{final_score}</h1>", unsafe_allow_html= True)
        
        #Result Massage
        if final_score < 10 or final_score> 90:
            st.success("You go Together like coke and Mentos! 🕺💃")
        elif 40 <= final_score<= 50:
            st.warning("You're alright Together. 💏")
        else:
            st.info("Keep the romance alive! 💗")
            
        st.markdown("---")
    else:
        st.error("Enter Both Name To Calculate Your Love Score. 💘 Try again!")