"""
Hugging Face API Integration
Accepts user input, sends request to Hugging Face Inference API, and displays the AI-generated response.
"""

import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


def load_api_token():
    """Load Hugging Face API token from environment variables."""
    load_dotenv()
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not api_token or api_token == "your_huggingface_token_here":
        print("Error: HUGGINGFACE_API_TOKEN not found in environment variables.")
        print("Please set your Hugging Face API token in the .env file.")
        print("Get your token from: https://huggingface.co/settings/tokens")
        sys.exit(1)
    return api_token


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("Hugging Face Inference API")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_huggingface_response(client, prompt):
    """Send request to Hugging Face API and return the response."""
    try:
        response = client.chat_completion(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            model="mistralai/Mistral-7B-Instruct-v0.2",
            max_tokens=1000,
            temperature=0.7
        )
        
        if response and response.choices:
            return response.choices[0].message.content
        else:
            return "No response received from the API."
            
    except Exception as e:
        return f"Error occurred while calling Hugging Face API: {str(e)}"


def main():
    """Main function to run the Hugging Face integration."""
    try:
        api_token = load_api_token()
        client = InferenceClient(token=api_token)
        
        print("\nHugging Face client initialized successfully!")
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Hugging Face Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print("\nSending request to Hugging Face API...")
            print("-" * 50)
            
            response = get_huggingface_response(client, user_input)
            
            print("\nAI Response:")
            print("=" * 50)
            print(response)
            print("=" * 50)
            print()
            
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
