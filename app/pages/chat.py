import streamlit as st
from services.ChatService import ChatService
from util.TextManager import TextManager
from util.util import display_chat_message, display_chat_history
from enums.MessageRole import MessageRole

def app():
    """Main application for handling chat interactions."""
    # Initialize text manager and chat service
    text_manager = TextManager('en')
    chat_service = ChatService()

    # Setup page title and description
    st.title(text_manager.get_text('titles', 'main'))
    st.write(text_manager.get_text('context_help', 'chat'))

    # Fetch and display chat history if not already in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = chat_service.fetch_chat_history()
    display_chat_history(st.session_state.chat_history, "chat_history")

    # Input field for new messages
    prompt = st.chat_input(text_manager.get_text('actions', 'what_can_i_do'), key="chat_prompt")
    if prompt:
        with st.spinner('Processing your message..'): 
            # Display user message and send to backend
            display_chat_message(MessageRole.USER, prompt, "chat_history")
            response = chat_service.send_chat_message(prompt)
            # Display response from AI if available
            if response:
                display_chat_message(MessageRole.ASSISTANT, response['message'], "chat_history")

    # Option to clear chat history
    if st.button(text_manager.get_text('actions', 'clear_chat_history'), key="clear_chat"):
        chat_service.clear_chat_history()
        st.session_state.chat_history = []
        st.rerun()
app()
