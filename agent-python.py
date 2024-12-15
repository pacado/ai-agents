import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

input = sys.argv[1] 

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

# print(os.environ)
# print(OPENAI_API_KEY)


def agent_victoria(prompt):
    content_system = """
    You are Python Coder.
    If you get a request for anything you can't convert to a python function,
    OUTPUT print('I am a Python Coder').
    In case of clear requests, ONLY output Python code without any code formatting.
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini", #, "gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": content_system},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )    

    victoria_says = completion.choices[0].message.content
    return victoria_says

def safe_execute(code):
    # Execute code safely
    try:
        # You might want to create a limited global context
        exec_context = {}
        exec(code, exec_context)
        return exec_context
    except Exception as e:
        return str(e)


victoria_says = agent_victoria(input)
print(f'{victoria_says:}')

safe_execute(victoria_says)


