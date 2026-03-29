"""
Groq API Integration
Accepts user input, sends request to Groq API, and displays the AI-generated response.
"""

import os
import sys
from dotenv import load_dotenv
from groq import Groq


def load_api_key():
    """Load Groq API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        print("Error: GROQ_API_KEY not found in environment variables.")
        print("Please set your Groq API key in the .env file.")
        sys.exit(1)
    return api_key


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("Groq Chat Completion")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_groq_response(client, prompt):
    """Send request to Groq API and return the response."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error occurred while calling Groq API: {str(e)}"


def main():
    """Main function to run the Groq integration."""
    try:
        api_key = load_api_key()
        client = Groq(api_key=api_key)
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Groq Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print("\nSending request to Groq API...")
            print("-" * 50)
            
            response = get_groq_response(client, user_input)
            
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
