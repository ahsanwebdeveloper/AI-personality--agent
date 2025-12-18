# LLM API call (OpenAI/Groq/etc.)
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set!")

client = Groq(api_key=api_key)

def generate_response(system_prompt: str, user_input: str) -> str:
    """
    Sends a chat prompt to Groq API and returns the response text.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        
        return f"Error communicating with Groq API: {str(e)}"
