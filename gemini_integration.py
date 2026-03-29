"""
Google Gemini API Integration
Accepts user input, sends request to Google Gemini API, and displays the AI-generated response.
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai


def load_api_key():
    """Load Google Gemini API key from environment variables."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("Please set your Google Gemini API key in the .env file.")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
        sys.exit(1)
    return api_key


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("Google Gemini AI Integration")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_gemini_response(model, prompt):
    """Send request to Google Gemini API and return the response."""
    try:
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
        else:
            return "No response received from the API."
            
    except Exception as e:
        return f"Error occurred while calling Gemini API: {str(e)}"


def main():
    """Main function to run the Gemini integration."""
    try:
        api_key = load_api_key()
        
        # Configure the API
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash-8b')
        
        print("\nGoogle Gemini model initialized successfully!")
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Google Gemini Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print("\nSending request to Google Gemini API...")
            print("-" * 50)
            
            response = get_gemini_response(model, user_input)
            
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
