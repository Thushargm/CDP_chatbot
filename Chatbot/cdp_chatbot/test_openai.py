import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file (ensure to specify full path if needed)
load_dotenv(dotenv_path=r'C:\Users\mahes\OneDrive\Desktop\cdp_chatbot\.env', override=True)

# Securely load your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Function to verify API key loading
def verify_api_key():
    if not api_key:
        print("API Key not found. Please check your .env file or environment variables.")
        return False
    print(f"API Key Loaded: {api_key[:5]}...{api_key[-5:]} (Key Length: {len(api_key)})")
    return True

# Function to list available models
def test_openai(model_name="gpt-3.5-turbo"):
    try:
        response = openai.Completion.create(
            model=model_name,  # Specify model name
            prompt="Hello, how are you?", 
            max_tokens=50
        )
        print("\nOpenAI response:", response['choices'][0]['text'].strip())
    except Exception as e:
        print("\nError occurred during API call:", e)

# Function to test OpenAI API with basic request
def test_openai(model_name="gpt-3.5-turbo"):
    try:
        # Test API with a simple request
        response = openai.ChatCompletion.create(
            model=model_name,  # Specify model name
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": "Hello, how are you?"}],
            max_tokens=100
        )
        print("\nOpenAI response:", response['choices'][0]['message']['content'].strip())
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please check your usage or try again later.")
    except openai.error.APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    print("### OpenAI API Key Verification ###")
    if verify_api_key():
        openai.api_key = api_key
        print("\n### Testing OpenAI API ###")
        test_openai()