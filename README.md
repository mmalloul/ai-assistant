## AI Assistant
This project delivers an AI-powered assistant designed to aid in various tasks, such as code review, document analysis, and interactive queries. The assistant utilizes a language model from Ollama, allowing you to interact with it based on your input. The project defaults to using the "codellama" model from Ollama's extensive model library, but you are encouraged to explore and utilize other models available at the [Ollama website](https://ollama.com/library).

## Changelog

Stay informed about the latest updates by checking our changelog [here](CHANGELOG.md).

## Requirements

Ensure you meet the following requirements before setting up the AI Assistant:

- Python 3.11.8 or earlier (compatibility issues exist with newer versions due to Torch dependencies).
- A virtual environment, ideally managed via `venv` or a similar tool, to manage Python packages without conflicts.
- Installation of additional Python packages as specified in the `requirements.txt` file.
- Active Ollama background service, necessary for the model functionalities.

## Installation

Follow these steps to get started with the AI Assistant:

1. **Clone the Repository**:
    ```shell
    git clone https://github.com/mmalloul/ai-assistant.git
    cd ai-assistant
    ```

2. **Model Setup**:
   - Download your desired Ollama model from the [Ollama website](https://ollama.com/).
   - For the codellama model:
     ```shell
     ollama pull codellama
     ```

3. **Environment Setup**:
    ```shell
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate.bat  # For Windows
    ```

4. **Install Dependencies**:
    ```shell
    pip install -r requirements.txt
    ```

### Data Directory Setup for Query

To enable document analysis functionalities, set up a `data` directory or specify a custom path:

1. **Create a Data Folder**:
    ```shell
    cd backend
    mkdir data
    ```

    - Optionally, update the `DATA_DIRECTORY` in `config.py` to a custom path if you prefer a different location.

2. **Add Documents**:
    Place the documents you want the LLM to analyze in the `data` directory or your custom location.

## Configuration

Modify settings in the `config.py` file as needed:

- `MODEL`: Define the AI model to use, default is 'codellama'.
- `TIMEOUT`: Set the timeout in seconds for AI operations.
- `SYSTEM_PROMPT`: Custom prompt to guide the AI's behavior.
- `DATA_DIRECTORY`: Path to the directory for document storage and analysis.

## Running the Application

Launch the AI Assistant using the following command:

```shell
streamlit run app.py
```

## Example
![Image Description](example.png)
