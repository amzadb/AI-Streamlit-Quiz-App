import streamlit as st
from quiz_generator import QuizGenerator
import PyPDF2
import io

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type. Please upload a PDF or TXT file.")
        return None

def main():
    st.title("AI Quiz Generator")
    st.subheader("Generate multiple-choice quiz questions using the Foundation model: Llama 3 8B Instruct")
    
    text_input = st.text_area("Enter your text (1000-2000 words):", height=300)
    uploaded_file = st.file_uploader("Or upload a PDF or TXT file", type=["pdf", "txt"])
    # complexity = st.selectbox("Select Quiz Complexity:", ["Beginner", "Intermediate", "Advanced"])
    complexity = "Beginner"
    
    if st.button("Generate Quiz"):
        if uploaded_file:
            text_input = extract_text_from_file(uploaded_file)
        
        if text_input:
            quiz_gen = QuizGenerator(text_input, complexity)
            questions = quiz_gen.generate_quiz()
            st.session_state.questions = questions
            st.session_state.answers = [None] * len(questions)
            st.session_state.show_results = False
        else:
            st.error("Please enter a valid text or upload a valid file.")
    
    if 'questions' in st.session_state and len(st.session_state.questions) > 0: 
        st.subheader("Quiz Questions:")
        for i, question in enumerate(st.session_state.questions):
            st.markdown(f"**{question['question_number']}**")
            st.session_state.answers[i] = st.radio(
                f"Select your answer for question {i + 1}",
                options=[question['option_A'], question['option_B'], question['option_C']],
                key=f"question_{i}"
            )
        
        if st.button("Submit"):
            st.session_state.show_results = True
        
        if st.session_state.show_results:
            correct_answers = 0
            for i, question in enumerate(st.session_state.questions):
                st.markdown(f"**{question['question_number']}**")
                st.write(f"{question['option_A']}")
                st.write(f"{question['option_B']}")
                st.write(f"{question['option_C']}")
                st.markdown(f"**Correct Answer: {question['correct_answer']}**")
                if st.session_state.answers[i] == question['correct_answer']:
                    correct_answers += 1
                    st.write("Your answer: ✅")
                else:
                    st.write(f"Your answer: ❌ ({st.session_state.answers[i]})")
            st.write(f"Your score: {correct_answers} out of {len(st.session_state.questions)}")
    else:
        st.markdown(f"**Sorry! No questions generated, please retry!!.**")

if __name__ == "__main__":
    main()