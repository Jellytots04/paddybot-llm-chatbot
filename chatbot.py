import anthropic
import os

# --- Configuration ---
PERSONA = "PaddyBot"
SYSTEM_PROMPT = """You are PaddyBot, a knowledgeable and friendly sports betting assistant.
You help users understand betting odds, explain different bet types, and summarise 
upcoming fixtures and markets in plain English. You are concise, clear, and never 
encourage irresponsible gambling. Always remind users to bet responsibly if they 
seem to be making impulsive decisions. You have deep knowledge of football, horse 
racing, tennis, and other major sports."""

# --- Initialise client ---
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def chat(conversation_history):
    """Send conversation history to Claude and return the response."""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )
    return response.content[0].text

def main():
    print(f"\n{'='*50}")
    print(f"  Welcome to {PERSONA} - Your Sports Betting Assistant")
    print(f"{'='*50}")
    print("  Type 'quit' to exit, 'reset' to start a new conversation\n")

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print(f"\n{PERSONA}: Good luck and remember — bet responsibly! Goodbye!\n")
            break
        if user_input.lower() == "reset":
            conversation_history = []
            print(f"\n{PERSONA}: Conversation reset. How can I help you?\n")
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = chat(conversation_history)

            # Add assistant response to history so context is maintained
            conversation_history.append({
                "role": "assistant",
                "content": response
            })

            print(f"\n{PERSONA}: {response}\n")

        except anthropic.APIConnectionError:
            print(f"\n[!] Could not connect to the API. Check your internet connection.\n")
        except anthropic.AuthenticationError:
            print(f"\n[!] Invalid API key. Check your ANTHROPIC_API_KEY environment variable.\n")
            break
        except Exception as e:
            print(f"\n[!] Something went wrong: {e}\n")

if __name__ == "__main__":
    main()
