# Streamlit Quiz App

This project is a Streamlit application that generates quizzes based on a provided text. Users can select the complexity of the quiz (Beginner, Intermediate, or Advanced) and receive three questions generated from the text.

## Project Structure

```
streamlit-quiz-app
├── src
│   ├── app.py            # Main entry point of the Streamlit application
│   ├── quiz_generator.py  # Contains the QuizGenerator class for generating quiz questions
│   └── utils.py          # Utility functions for text processing
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-quiz-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Enter the text (1000-2000 words) in the provided input box.

3. Select the desired quiz complexity (Beginner, Intermediate, Advanced).

4. Click on the "Generate Quiz" button to receive three quiz questions based on the provided text.

## Quiz Generation

The quiz questions are generated using the `QuizGenerator` class, which utilizes advanced language models like Google Gemini or equivalent LLMs to analyze the text and create relevant questions based on the selected complexity level.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.