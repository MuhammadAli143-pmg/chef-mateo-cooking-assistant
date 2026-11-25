# 🍳 Chef Mateo — AI Cooking Assistant

A domain-specific conversational AI chatbot specializing in **cooking, baking, and culinary guidance**. Powered by the **Groq API** (`llama-3.3-70b-versatile`) and deployed as an interactive web application using **Streamlit**.

## 🔗 Live Demo
**Public App Link:** [https://chef-mateo-cooking-assistant-vyphbhdf5ycsgrhmbafyrc.streamlit.app/]

---

## 🎯 Domain Focus & Guardrails
* **Chosen Domain:** Cooking & Culinary Arts (recipes, ingredient substitutions, cooking techniques, meal prep, and kitchen safety).
* **Off-Topic Handling:** Through strict system-level guardrails, the chatbot stays strictly within the culinary domain. Any unrelated queries (e.g., coding, math, politics, or medical advice) are politely declined and redirected back to cooking.

---

## 🧠 System Prompt Design
The chatbot's behavior is driven by a structured system prompt divided into **Role** and **Context**:

* **Role:** Defines the persona as *Chef Mateo*, a warm, encouraging, and practical culinary instructor with a friendly and easy-to-follow tone.
* **Context:**
  * **Audience:** Home cooks of all skill levels.
  * **Scope:** Restricted exclusively to food preparation, recipes, ingredients, and kitchen tools.
  * **Constraints:** Formats recipes clearly using bulleted ingredient lists and numbered step-by-step instructions.
  * **Guardrails:** Instructs the model to refuse non-culinary prompts politely.

---

## ⚙️ Model Configuration & Justification
* **Model:** `llama-3.3-70b-versatile` (via Groq API) for fast, low-latency, high-accuracy responses.
* **`temperature = 0.6`:** Chosen to strike a balance between creativity and reliability. A very low temperature (`0.0`) produces repetitive, rigid recipe suggestions, while a high temperature (`1.2+`) risks generating unrealistic ingredient combinations or inaccurate measurements. `0.6` allows helpful culinary variations while keeping instructions dependable.
* **`max_tokens = 600`:** Roughly equivalent to 450 words, providing enough room for a complete recipe (ingredients + numbered steps) without cutting off mid-sentence, while keeping responses concise and avoiding runaway token usage.

---

## 🛠️ Key Features
* **Multi-Turn Memory:** Uses `st.session_state` to retain full conversation history across turns so users can ask follow-up questions (e.g., *"How long should I marinate it?"*).
* **Graceful Error Handling:** Wraps API calls in `try-except` blocks with request timeouts to display user-friendly error messages instead of crashing if network or API issues occur.
* **Secure Secret Management:** Uses Streamlit Secrets (`st.secrets`) so API keys are never exposed in public source code.

---

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com
   cd chef-mateo-cooking-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Groq API key:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```
4. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
