import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
You are an assistant that simplifies technical error messages for developers.
Your job is to:
1. Explain the error in simple terms
2. Suggest where the issue might be
3. Offer practical next steps (e.g., "Check this file", "Google this exact message")

Here is the error:
```{error}```
"""

def simlify_error(error_message : str) -> str:
    prompt = PROMPT_TEMPLATE.format(error=error_message)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for debugging."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ Failed to get LLM response: {str(e)}"