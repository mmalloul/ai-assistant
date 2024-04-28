import streamlit as st
from services.QueryService import QueryService
from util.TextManager import TextManager
from util.util import display_chat_message
from enums.MessageRole import MessageRole

def app():
    """Handles the display and functionality of the query page in the AI Assistant application."""

    # Initialize the text manager for localization and the query service for backend interactions
    text_manager = TextManager('en')
    query_service = QueryService()

    # Set up the page title and description using localized text
    st.title(text_manager.get_text('titles', 'main'))
    st.write(text_manager.get_text('context_help', 'query'))

    # Create a text area for users to enter their query
    query = st.text_area(text_manager.get_text('actions', 'enter_query_here'), height=150, key="query_prompt")
    submit_button_label = text_manager.get_text('actions', 'submit_query')

    # Button to submit the query to the backend
    if st.button(submit_button_label):
        with st.spinner('Processing your query...'): 
            response = query_service.send_query(query)
            if response:
                display_chat_message(MessageRole.ASSISTANT, response['message'], None)
            else:
                st.error(text_manager.get_text('actions', 'failed_process_query'))

app()
