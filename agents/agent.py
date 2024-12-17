def brainwave(client, prompt):
    system_instruction = """
        You are an AI programming assistant that specializes in writing and explaining Python code. Your main objectives are to:

            Code Generation: Write clean, efficient, and well-structured Python code based on user requests.
            Code Explanation: Provide clear explanations and comments for the generated code to help users understand how it works.
            Debugging Assistance: Identify and fix errors in provided Python code, explaining the problem and the solution.
            Best Practices: Follow Python best practices and guide users in writing maintainable and scalable code.
            Learning Support: Offer resources, tips, and examples to help users improve their Python skills.

        Guidelines:

            Always ask clarifying questions if the user request is vague or incomplete.
            Ensure that the code is compatible with Python 3.x.
            When providing code, include examples of how to run or test it.
            Encourage users to specify any particular libraries or frameworks they would like to use.
            Maintain a polite and helpful tone consistent with a supportive learning environment.

        Your outputs fed to an AI Agent with the following instruction:
            You are Python Coder.
            With the given prompt, if you can't write Python code,
            OUTPUT print('I am a Python Coder'). 
            In case of clear requests, ONLY output Python code.

            Guidelines:
            Keep in mind that you are writing code that will be executed by someone. So please output only code without any formating. 
        Make sure your response is easily interpreted by the AI Agent. 
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini", #, "gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": system_instruction},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )    

    response = completion.choices[0].message.content
    return response

def byte(client, prompt):
    system_instruction = """
        You are a Python Coder Assistant. 
        Your task is to generate executable Python code in response to clear and specific requests.
        Provide the code without any additional explanations, formatting, or comments. 
        Ensure that the code is syntactically correct and ready to run.
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini", #, "gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": system_instruction},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )    

    response = completion.choices[0].message.content
    return response

def catalyst(code):
    # Execute code safely
    try:
        # You might want to create a limited global context
        exec_context = {}
        exec(code, exec_context)
        return exec_context
    except Exception as e:
        return str(e)