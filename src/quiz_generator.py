import boto3
import json

class QuizGenerator:
    def __init__(self, text, complexity="Beginner"):
        self.text = text
        self.complexity = complexity
        # self.bedrock_endpoint = "your-bedrock-endpoint"  # Replace with your Bedrock endpoint

    def generate_quiz(self):
        questions = self.generate_questions(self.text, self.complexity)
        return questions

    def generate_questions(self, text, complexity, num_questions=3):
        max_tokens = 8192
        prompt = f"Generate {num_questions} {complexity.lower()} level multiple-choice quiz questions, each question only with {num_questions} unique choices: A, B and C and the correct answer, from the following text:\n\n{text}\n\nQuestions and Answers:"
        print("prompt: " + prompt)
        
        # Truncate the input text to fit within the token limit
        if len(prompt) > max_tokens:
            prompt = prompt[:max_tokens]
        
        # Create a Bedrock runtime client
        bedrock_runtime = boto3.client('bedrock-runtime')

        # Prepare the payload
        payload = {
            # "inputText": prompt
            "prompt": prompt
        }

        response = bedrock_runtime.invoke_model(
            modelId = "meta.llama3-8b-instruct-v1:0",
            # modelId = "amazon.titan-text-premier-v1",
            # modelId = "amazon.titan-text-express-v1",
            body = json.dumps(payload),
            accept = "application/json",
            contentType = "application/json"
        )

        # Parse the response
        result = json.loads(response['body'].read().decode('utf-8'))
        # output_text = result['results'][0]['outputText']
        output_text = result['generation']
        print("output_text: " + output_text)
            
        # Process the output text to extract questions and answers
        questions = []
        lines = [line.strip() for line in output_text.strip().split('\n') if line.strip()]
        i = 0
        while i < len(lines):
            if lines[i].startswith("1.") or lines[i].startswith("2.") or lines[i].startswith("3."):
                question_number = lines[i].strip()
                option_A = lines[i + 1].strip()
                option_B = lines[i + 2].strip()
                option_C = lines[i + 3].strip()
                # option_D = lines[i + 4].strip()
                correct_answer = lines[i + 4].strip().replace("Answer: ", "")
                
                # Ensure options are unique and limit to 3 options
                options = list(set([option_A, option_B, option_C]))
                if correct_answer in options:
                    options.remove(correct_answer)
                # options = options[:2]  # Take the first 2 unique options
                options.append(correct_answer)  # Add the correct answer back
                
                if len(options) == 3:
                    questions.append({
                        "question_number": question_number,
                        "option_A": options[0],
                        "option_B": options[1],
                        "option_C": options[2],
                        # "option_D": options[3],
                        "correct_answer": correct_answer
                    })
                i += 5
            else:
                print(f"Skipping incomplete question block starting at line {i}: {lines[i]}")
                i += 1
                        
        print("questions: " + str(questions))
        return questions