"""
Cohere API Integration
Accepts user input, sends request to Cohere API, and displays the AI-generated response.
"""

import os
import sys
from dotenv import load_dotenv
import cohere


def load_api_key():
    """Load Cohere API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key or api_key == "your_cohere_api_key_here":
        print("Error: COHERE_API_KEY not found in environment variables.")
        print("Please set your Cohere API key in the .env file.")
        print("Get your API key from: https://dashboard.cohere.com/api-keys")
        sys.exit(1)
    return api_key


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("Cohere AI Integration")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_cohere_response(client, prompt):
    """Send request to Cohere API and return the response."""
    try:
        response = client.chat(
            model="command",
            message=prompt,
            temperature=0.7,
            max_tokens=1000
        )
        
        if response and response.text:
            return response.text
        else:
            return "No response received from the API."
            
    except Exception as e:
        return f"Error occurred while calling Cohere API: {str(e)}"


def main():
    """Main function to run the Cohere integration."""
    try:
        api_key = load_api_key()
        client = cohere.Client(api_key)
        
        print("\nCohere client initialized successfully!")
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Cohere Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print("\nSending request to Cohere API...")
            print("-" * 50)
            
            response = get_cohere_response(client, user_input)
            
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
