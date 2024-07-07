# Local LLMBot
## Description
Local LLMBot is a Python application designed to act as a question-and-answer assistant. The application uses the streamlit library for creating a web interface and the ollama library for interacting with the Large Language Model. The assistant aims to provide accurate answers based on the instructions and context provided by the user.

## File Structure

- `app.py`: The main application file that runs the Streamlit web interface.
- `requirements.txt`: Lists the dependencies required for the project.
- `code_without_UI.py`: Contains the core logic of the application without the UI components, designed to run in a terminal environment.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>

2. Install the required packages:

   ```bash
   pip install -r requirements.txt

3. Running the Streamlit Web Application

   ```bash
   streamlit run app.py
>Open your web browser and go to http://localhost:8501 to interact with the Local LLMBot.