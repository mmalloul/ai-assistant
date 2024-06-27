import streamlit as st
from services.CodeReviewService import CodeReviewService
from util.TextManager import TextManager
from enums.MessageRole import MessageRole

def display_code_review_message(role: MessageRole, content: str):
    """Displays code review messages on the page."""
    with st.chat_message(role.value.capitalize()):
        st.markdown(content)

def app():
    """Handles the display and functionality of the code review page in the AI Assistant application."""

    # Initialize the text manager for localization and the code review service for backend interactions
    text_manager = TextManager('en')
    code_review_service = CodeReviewService()

    # Set up the page title and description using localized text
    st.title(text_manager.get_text('titles', 'main'))
    st.write(text_manager.get_text('context_help', 'query'))

    # Create a text area for users to enter their code
    query = st.text_area(text_manager.get_text('actions', 'enter_query_here'), height=150, key="query_prompt")
    submit_button_label = text_manager.get_text('actions', 'submit_query')

    # Dropdown for selecting the model type
    model_type = st.selectbox("Select Model", ["openai", "ollama", "bedrock"])

    # Button to submit the code for review
    if st.button(submit_button_label):
        with st.spinner('Processing your query...'):
            response = code_review_service.send_code_review(query, model_type)
            if response:
                all_issues_content = ""
                print(response)
                for issue in response['issues']:
               
                    message_content = f"**Category:** {issue['category']}\n\n" \
                                      f"**Location:** {issue['location']}\n\n" \
                                      f"**Description:** {issue['description']}\n\n" \
                                      f"**Suggestion:** {issue['suggestion']}\n\n\n"
                    all_issues_content += message_content

                display_code_review_message(MessageRole.ASSISTANT, all_issues_content)
            else:
                st.error(text_manager.get_text('actions', 'failed_process_query'))

app()