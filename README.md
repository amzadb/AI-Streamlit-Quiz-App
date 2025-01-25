# Streamlit Quiz Generator

This project is a Streamlit application that generates multiple-choice quiz questions based on provided text. Users can either paste text directly or upload a PDF or TXT file to generate quiz questions. The application uses Amazon Bedrock's foundation models to generate the questions.

## Features

- Generate multiple-choice quiz questions from provided text.
- Support for text input and file upload (PDF or TXT).
- Display questions with radio button options.
- Evaluate answers and display the score.

## Requirements

- Python 3.7 or higher
- Streamlit
- Boto3
- PyPDF2
- OpenAI (if using OpenAI's GPT-3 model)

## Installation

1. Clone the repository:

```sh
git clone https://github.com/amzadb/ai-streamlit-quiz-app.git
cd ai-streamlit-quiz-app
```

## Project Structure

```
ai-streamlit-quiz-app
├── src
│   ├── app.py            # Main entry point of the Streamlit application
│   ├── quiz_generator.py  # Contains the QuizGenerator class for generating quiz questions
│   └── utils.py          # Utility functions for text processing
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your AWS credentials to access Amazon Bedrock models:
   ```
   aws configure
   ```
4. If using OpenAI's GPT-3 model, set up your OpenAI API key:
   ```
   export OPENAI_API_KEY='your_openai_api_key'  # On Windows, use `set OPENAI_API_KEY=your_openai_api_key`
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```
2. Open your web browser and go to http://localhost:8501.

3. Enter the text (1000-2000 words) in the text area or upload a PDF or TXT file.

4. Select the desired quiz complexity (Beginner, Intermediate, Advanced).

5. Click on the "Generate Quiz" button to generate quiz questions.

6. Answer the questions and click the "Submit" button to evaluate your answers and see your score.

## Example
Here is an example of how to use the application:
1. Enter text or upload a file
2. Generate quiz questions
3. Answer the questions
4. Submit and see your score

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to submit issues or pull requests for improvements or additional features.