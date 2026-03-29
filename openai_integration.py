"""
OpenAI API Integration
Accepts user input, sends request to OpenAI API, and displays the AI-generated response.
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI


def load_api_key():
    """Load OpenAI API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_openai_api_key_here":
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set your OpenAI API key in the .env file.")
        sys.exit(1)
    return api_key


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("OpenAI Chat Completion")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_openai_response(client, prompt):
    """Send request to OpenAI API and return the response."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error occurred while calling OpenAI API: {str(e)}"


def main():
    """Main function to run the OpenAI integration."""
    try:
        api_key = load_api_key()
        client = OpenAI(api_key=api_key)
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using OpenAI Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print("\nSending request to OpenAI API...")
            print("-" * 50)
            
            response = get_openai_response(client, user_input)
            
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
