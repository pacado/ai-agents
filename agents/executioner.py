def safe_execute(code):
    # Execute code safely
    try:
        # You might want to create a limited global context
        exec_context = {}
        exec(code, exec_context)
        return exec_context
    except Exception as e:
        return str(e)