def agent_victoria(client, prompt):
    system_instruction = """
    You are Python Coder.
    With the given prompt, if you can't write Python code,
    OUTPUT print('I am a Python Coder'). 
    In case of clear requests, ONLY output Python code.

    Guidelines:
    Keep in mind that you are writing code that will be executed by someone. So please output only code without any formating. 

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

    victoria_says = completion.choices[0].message.content
    return victoria_says

def agent_victoria(client, prompt):
    system_instruction = """
    You are Python Coder.
    With the given prompt, if you can't write Python code,
    OUTPUT print('I am a Python Coder'). 
    In case of clear requests, ONLY output Python code.

    Guidelines:
    Keep in mind that you are writing code that will be executed by someone. So please output only code without any formating. 

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

    victoria_says = completion.choices[0].message.content
    return victoria_says