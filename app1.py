import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# App ka design
st.title("📝 Script Summarizer")
st.write("Lamba script paste karo, chhota summary pao!")

# Bara input box (script ke liye)
script = st.text_area("Apna script yahan paste karo:", height=300)

# Summary ki length choose karo
length = st.selectbox("Summary kitni lambi?", ["Chhoti", "Medium", "Detailed"])

# Button
if st.button("Summary Banao"):
    if script:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=600,
            messages=[
                {
                    "role": "system",
                    "content": f"Tum ek expert summarizer ho. Diye gaye script ka {length} summary Roman Urdu mein banao. Saaf aur asaan zabaan use karo. Sirf summary do, faltu baat nahi."
                },
                {
                    "role": "user",
                    "content": f"Is script ka summary banao:\n\n{script}"
                }
            ]
        )
        summary = response.choices[0].message.content
        st.write("### Summary:")
        st.write(summary)
    else:
        st.write("⚠️ Pehle script paste karo!")