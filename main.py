import streamlit as st 
import pandas as pd
import ollama
import resquests
import time 

from crypto_dict import create_crypto_dict

def main():
    st.title("LinkedIn post generator")
        
    crypto_dict = create_crypto_dict() 
    
    situation = st.text_input(label="Situation")
    about = st.text_input(label="About")
    tone = st.text_input(label = "Tone")
    cringe_level = st.slider(label= "Cringe level", min_value = 5, max_value = 11, step = 1)
    
    
    ollama_prompt = f"""
        Write a LinkedIn post about what you learned about {about} from {situation}. 
        Cringe level is {cringe_level}/11, where 5 is the lowest (every linkedin pots is at least 5/11 cringe)
        and 11 is the highest. 5 should be almost neutral, while 11 should include all buzzwords you can imagine and 
        overuse emojiis. 
        Mention the situation and what you've learned explicitly. Make the tone {tone}
    """
    
    if st.button("Get prompt"): 
        result = ollama.generate(model="Mistral", prompt=ollama_prompt)
        st.write(result["response"])
if __name__ == "__main__":
    main()


