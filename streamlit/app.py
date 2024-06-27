import streamlit as st

def main():
    """Main application entrypoint."""

    st.set_page_config(page_title="AI Assistant", layout="wide")

    # Setting up the sidebar with navigation and app information
    st.sidebar.title("Navigation")
    st.sidebar.info("""
    Welcome to the AI Assistant app! Use the navigation menu to access different functionalities:
    
    - **Chat**: Engage in real-time conversations with an AI. Ask questions, seek advice, or explore topics in an interactive format.
    - **Code Review**: Submit your code for AI analysis. The AI will review the code and provide feedback on potential improvements, issues, and best practices.
    
    Select a page from the top left menu to begin.
    """)

    # Main page introduction
    st.title("Welcome to the AI Assistant!")
    st.write("""
    This application demonstrates a range of AI-driven functionalities within a user-friendly web interface. 
    Navigate through the sidebar to explore different interaction modes with AI technologies:
    - The **Chat** interface offers a dynamic conversation experience where you can communicate directly with an AI.
    - The **Code Review** interface allows you to submit your code for AI analysis, enabling specific and structured feedback on code quality and improvements.
    """)
    st.write("---")
    st.write("Select a page from the sidebar to get started or continue browsing the available options.")

if __name__ == "__main__":
    main()