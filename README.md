# AI Code Review Chat

This is a code review app that utilizes AI to provide insights and suggestions for your code. 


## Requirements

- Python 3.11.8 or lower (Torch is not compatible with newer versions)
- Virtual environment with pip (Important to not cause dependency conflicts)
- Other dependencies listed in `requirements.txt`

## Installation

1. Download the Ollama from the Ollama website and follow the installation instructions. https://ollama.com/

2. Pull codellama

    ```shell
    ollama pull codellama
    ```

3. Create and activate a virtual environment:

    ```shell
    pip install virtualenv
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate  # For Windows
    ```

4. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Configuration

1. Open the `app.py` file.

2. Locate the following lines of code:

    ```python
    SYSTEM_PROMPT = """
    As Bob, your AI code review assistant, you will show code examples to code that needs improvement and explain why its better.
    """
    MODEL = "codellama"
    ```

3. Change the `SYSTEM_PROMPT` to your desired system prompt.

4. You can change the `MODEL` to any Ollama model if needed.

5. You can change `TIMEOUT` to the desired prompt timeout.

## How to run

1. Run the app:

    ```shell
    streamlit run app.py
    ```
![Image Description](example.png)
