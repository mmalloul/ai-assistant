## AI Assistant
This project aims to provide an AI-powered assistant that, for example, can help you review your code. The assistant utilizes a language model from Ollama, running your prompts through it. By default, the project is set to use the codellama model, but you're encouraged to explore and download any model from their extensive library on the [Ollama website](https://ollama.com/library) :)

## Changelog

The changelog for this project is available [here](CHANGELOG.md).

## Requirements

Before using the AI Assistant, ensure you meet the following requirements:

- Python 3.11.8 or earlier versions (due to Torch compatibility issues with newer Python versions).
- A virtual environment with pip to avoid dependency conflicts.
- Additional dependencies as listed in the `requirements.txt` file.
- The Ollama background service must be active for model functionality.

## Installation

Follow these steps to set up the AI Assistant:

1. Clone the project repository:

    ```shell
    git clone https://github.com/mmalloul/ai-assistant.git
    cd ai-assistant
    ```

2. Download your choice of Ollama model from the [Ollama website](https://ollama.com/) and follow their setup instructions.

3. Specifically, to pull the codellama model, use:

    ```shell
    ollama pull codellama
    ```

4. Create and activate a virtual environment:

    ```shell
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate  # For Windows
    ```

5. Install the required Python packages:

    ```shell
    pip install -r requirements.txt
    ```

### Optional Data Directory Setup

To analyze documents, you need to create a `data` folder in the project's root directory or specify a custom path in `config.py`. If done correctly, it will notify you that it's indexing the files on startup.
This directory will be used to store and index documents for analysis:

1. Create a `data` folder in the root of your cloned repository:

    ```shell
    mkdir data
    ```
    (Optional) To use a custom directory, update the `DATA_DIRECTORY` variable in `config.py` with your chosen path.

2. Add documents you want the LLM to analyse to the `data` (or your custom) directory. 
## Configuration

Adjust your setup in the `config.py` file:

- `DEFAULT_MODEL`: Sets the default AI model (e.g., 'codellama') for operations.
- `DEFAULT_TIMEOUT`: Specifies the default timeout in seconds for AI processing.
- `DEFAULT_SYSTEM_PROMPT`: Establishes the initial instructions for the AI, guiding its responses and actions.
- `DEFAULT_DATA_DRECTORY`: The path to the directory where documents are stored for analysis. By default, this is set to a `data` folder in the project root. Customize this path if needed.

## Running the Application

Start the AI Assistant with the following command:

```shell
streamlit run app.py
```

## Example
![Image Description](example.png)
