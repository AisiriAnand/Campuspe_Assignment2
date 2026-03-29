"""
Ollama API Integration
Accepts user input, sends request to local Ollama instance, and displays the AI-generated response.
Note: Ollama must be installed and running locally.
"""

import sys
import requests


def check_ollama_running():
    """Check if Ollama is running locally."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False
    except Exception:
        return False


def get_user_input():
    """Get user input for the prompt."""
    print("=" * 50)
    print("Ollama Local AI Integration")
    print("=" * 50)
    print("Type 'exit' to quit the program.")
    print("-" * 50)
    
    user_input = input("\nEnter your prompt: ").strip()
    return user_input


def get_ollama_response(prompt, model="llama2"):
    """Send request to local Ollama API and return the response."""
    try:
        url = "http://localhost:11434/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(url, json=payload, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "No response received.")
        else:
            return f"Error: HTTP {response.status_code} - {response.text}"
            
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Please ensure Ollama is running."
    except requests.exceptions.Timeout:
        return "Error: Request timed out. The model may be taking too long to respond."
    except Exception as e:
        return f"Error occurred while calling Ollama API: {str(e)}"


def main():
    """Main function to run the Ollama integration."""
    try:
        print("Checking if Ollama is running...")
        if not check_ollama_running():
            print("\nError: Ollama is not running or not installed.")
            print("Please install Ollama from https://ollama.com/")
            print("Then run: ollama run llama2")
            sys.exit(1)
        
        print("Ollama is running!\n")
        
        model_name = input("Enter model name (default: llama2): ").strip() or "llama2"
        
        while True:
            user_input = get_user_input()
            
            if user_input.lower() == 'exit':
                print("\nThank you for using Ollama Integration. Goodbye!")
                break
            
            if not user_input:
                print("Error: Please enter a valid prompt.")
                continue
            
            print(f"\nSending request to Ollama (model: {model_name})...")
            print("-" * 50)
            
            response = get_ollama_response(user_input, model_name)
            
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
