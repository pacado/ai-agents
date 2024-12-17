```python
import os
from dotenv import load_dotenv
from openai import OpenAI
from agents import victoria, executioner
```


```python
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
```


```python
prompt = """
Create a folder named 'Market Risk' in my workspace
"""
```


```python
response = victoria.agent_victoria(client, prompt)
print(response)
```

    import os
    
    os.makedirs('Market Risk', exist_ok=True)



```python
executioner.safe_execute(response) ;
```


```python
prompt = """
Delete the folder named 'Market Risk' in my workspace
"""
```


```python
response = victoria.agent_victoria(client, prompt)
print(response)

```

    import shutil
    
    shutil.rmtree('Market Risk')



```python
executioner.safe_execute(response) ;
```
