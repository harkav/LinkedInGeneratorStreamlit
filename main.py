import streamlit as st 
import ollama
import time 
import threading 

from crypto_dict import create_crypto_dict, crypto_ticker, random_top_g_energy

def main():
    st.markdown("<h1 style='text-align: center;'>LinkedIn post generator</h1>", unsafe_allow_html=True)
    crypto_dict = create_crypto_dict() 
    st.markdown(crypto_ticker(crypto_dict), unsafe_allow_html=True)


    welcome_text = """
    <div style='text-align: center; font-size: 18px; line-height: 1.5em; margin-bottom: 20px;'>
    This is a LinkedIn fluff post generator.<br>
    <br>
    It will generate a prompt based on the situation (what has happened), what you learned from the situation (about),
    and generate some fluff using Mistral and Ollama based on the situation and the learning experience, as well as the
    cringe level (starts at 5, goes to 11) and a specified tone.
    </div>
    """

    st.markdown(welcome_text, unsafe_allow_html=True)

        
    
    
    situation = st.text_input(label="Situation")
    about = st.text_input(label="About")
    tone = st.text_input(label = "Tone")
    cringe_level = st.slider(label= "Cringe level", min_value = 5, max_value = 11, step = 1)
    
    if not tone: 
        tone = "formal"
    ollama_prompt = f"""
    Write a LinkedIn post about what you learned about {about} from {situation}. 
    Cringe level is {cringe_level}/11, where 5 is the lowest (every LinkedIn post is at least 5/11 cringe),
    and 11 is the highest. Level 5 should be almost neutral, while 11 should include all buzzwords you can imagine and 
    overuse emojis. 
    Mention the situation and what you've learned explicitly. Make the tone {tone}.
    """

    
    if st.button("Get prompt"): 
        placeholder = st.empty()

        # Display rotating quotes every 5 seconds for up to 15 seconds
        for _ in range(3):  # 3 quotes, 5s each = 15s
            quote = random_top_g_energy()
            placeholder.info(f"⏳ Generating your post... While waiting, reflect on the wisdom of the alpha:\n\n💬 *\"{quote}\"*")
            time.sleep(5)

        result = ollama.generate(model="Mistral", prompt=ollama_prompt)
        placeholder.empty()
        st.write(result["response"])


def dynamic_spinner(placeholder, stop_event):
    while not stop_event.is_set():
        quote = random_top_g_energy()
        placeholder.info(f"⏳ Generating your post... While waiting, reflect on the wisdom of the alpha:\n\n💬 *\"{quote}\"*")
        st.write(placeholder.info)
        time.sleep(15)


if __name__ == "__main__":
    main()




