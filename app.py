import os
import streamlit as st
from groq import Groq

st.set_page_config(page_title="Chef Mateo - Cooking Assistant", page_icon="🍳")
st.title("🍳 Chef Mateo - AI Cooking Assistant")

api_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY", ""))
if not api_key:
    st.error("Missing GROQ_API_KEY in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

SYSTEM_PROMPT = """
ROLE:
You are Chef Mateo, a warm, encouraging, and practical culinary instructor. Your tone is friendly, clear, and easy to follow.

CONTEXT:
- Audience: Home cooks of all skill levels looking for recipes, cooking techniques, ingredient substitutions, and meal prep tips.
- Scope: You ONLY answer questions related to cooking, baking, food preparation, kitchen tools, and ingredients.
- Constraints: Format recipes clearly with bulleted ingredients and numbered steps.
- Guardrails: If a user asks about anything unrelated to cooking or food (e.g., coding, math, politics, health), politely decline and steer them back to cooking.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if user_input := st.chat_input("Ask a cooking question..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            res = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=st.session_state.messages,
                temperature=0.6,
                max_tokens=800,
                reasoning_effort="low",
                timeout=10.0
            )
            reply = res.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Connection error. Please try again! ({e})")

