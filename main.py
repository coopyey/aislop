import os
import argparse
from dotenv import load_dotenv
from google import genai

# Creating the ai client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("API Key Empty")
client = genai.Client(api_key=api_key)

# Creating the argument setup
parser = argparse.ArgumentParser(description="AI Bot")
parser.add_argument("user_prompt", type=str, help="Prompt to give to the bot.")
args = parser.parse_args()
# Now we can access args.user_prompt

result = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=args.user_prompt
)

if not result.usage_metadata:
    raise RuntimeError("Metadata empty: API call likely failed")
else:
    print(f"Prompt tokens: {result.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {result.usage_metadata.candidates_token_count}")
    print(result.text)
