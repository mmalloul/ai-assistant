import streamlit as st
from services.ChatService import ChatService
from util.TextManager import TextManager
from enums.MessageRole import MessageRole

def display_chat_message(role: MessageRole, content: str, history_key: str = None):
    """Displays chat messages on the page and stores them in session state if specified."""
    with st.chat_message(role.value.capitalize()):
        st.markdown(content)
    if history_key and st.session_state.get(history_key) is not None:
        st.session_state[history_key].append({'role': role.value, 'content': content})

def display_chat_history(history, history_key: str):
    """Displays the entire chat history from session state or an external source."""
    if history:
        for message in history:
            if message['role'] != MessageRole.SYSTEM.value:
                display_chat_message(MessageRole(message['role']), message['content'])
    else:
        st.session_state[history_key] = []

def app():
    """Main application for handling chat interactions."""
    # Initialize text manager and chat service
    text_manager = TextManager('en')
    chat_service = ChatService()

    # Setup page title and description
    st.title(text_manager.get_text('titles', 'main'))
    st.write(text_manager.get_text('context_help', 'chat'))

    # Dropdown for selecting the model type
    model_type = st.selectbox("Select Model", ["openai", "ollama", "bedrock"])

    # Initialize chat history if not in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    display_chat_history(st.session_state.chat_history, "chat_history")

    # Input field for new messages
    prompt = st.chat_input(text_manager.get_text('actions', 'what_can_i_do'), key="chat_prompt")
    if prompt:
        with st.spinner('Processing your message..'):
            # Display user message and send to backend
            display_chat_message(MessageRole.USER, prompt, "chat_history")
            response = chat_service.send_chat_message(prompt, model_type)
            # Display response from AI if available
            if response:
                display_chat_message(MessageRole.ASSISTANT, response['content'], "chat_history")
                st.session_state.chat_history.append({"role": "assistant", "content": response['content']})

    # Option to clear chat history
    if st.button(text_manager.get_text('actions', 'clear_chat_history'), key="clear_chat"):
        st.session_state.chat_history = []
        st.rerun()

app()