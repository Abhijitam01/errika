import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create OpenAI client using the new SDK style
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
You are an assistant that simplifies technical error messages for developers.
Your job is to:
1. Explain the error in simple terms
2. Suggest where the issue might be
3. Offer practical next steps (e.g., "Check this file", "Google this exact message")

Here is the error:
```{error}```
"""

def simplify_error(error_text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that simplifies Python and terminal errors and gives suggestions to fix them.",
                },
                {
                    "role": "user",
                    "content": PROMPT_TEMPLATE.format(error=error_text),
                },
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Failed to get LLM response: {e}"
