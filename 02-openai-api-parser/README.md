## 02-openai-api-parser
This Python program demonstrates how to use the OpenAI API to parse unstructured data to a JSON output.

## Features

- Uses the OpenAI API to parse unstructured data to JSON

### Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.7+ installed on your system
- Git installed on your system

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/KamalRavichandran/genai-llm-playground.git
```
2. **Change Directory**
```bash
cd genai-llm-playground\02-openai-api-parser
```
3. **Set Environment Variables**
- Copy the `.env.example` file and rename it to `.env`.
- Open the `.env` file and replace the placeholder with your actual OpenAI API key.
4. **Install Dependencies**
```bash
pip install -r requirements.txt
```
### Running the Project

After completing the installation steps, you can run the project with the following command:
```bash
python openai-parser.py
```
This will execute the `openai-parser.py` file, which is the entry point of the project.

### Additional Notes

- Make sure to keep the `.env` file secure and never commit it to version control. It has been added to the `.gitignore` file to prevent accidental commits.