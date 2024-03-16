import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

SYSTEM_PROMPT = """
As Bob, your AI code review assistant, you will show code examples to code that needs improvement and explain why its better.:

- SOLID Principles: Ensure your code follows principles like Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. If there are violations, suggest alternatives with clear code examples.
- Design Patterns: Identify common design patterns like Factory, Singleton, Observer, and Strategy. If applicable, recommend incorporating these patterns into the codebase with relevant examples.
- Cleanliness of Code: Evaluate readability, maintainability, and adherence to coding standards. If improvements are needed, suggest cleaner alternatives and provide code snippets as examples.
- Security Considerations: Address potential vulnerabilities and suggest best practices for security. Offer code examples that demonstrate secure coding techniques and explain their importance.
"""

MODEL = 'codellama'
TIMEOUT = 120

st.title("AI Code reviewer")
st.write(f"Model: {MODEL}")

if "llm_model" not in st.session_state:
    st.session_state["llm_model"] = MODEL

llm = Ollama(model=st.session_state["llm_model"], request_timeout=TIMEOUT)

if "llm_model" not in st.session_state:
    st.session_state["llm_model"] = MODEL

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(ChatMessage(role="system", content=SYSTEM_PROMPT))

for message in st.session_state.messages:
    if message.role == "system":
        continue
    with st.chat_message(message.role):
        st.markdown(message.content)

if prompt := st.chat_input("What can I review for you?", disabled=not input):
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)


    with st.spinner("Reviewing Code..."):
        response = llm.chat(
        model=st.session_state["llm_model"],
        messages=st.session_state.messages
        )
    
        content = response.message.content
    st.markdown(content)     
    st.session_state.messages.append(ChatMessage(role="assistant", content=content))