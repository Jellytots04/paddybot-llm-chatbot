# PaddyBot - Sports Betting Assistant

A CLI chatbot powered by the Anthropic Claude API, built to demonstrate
LLM integration and prompt engineering in a real-world domain context.
PaddyBot acts as a knowledgeable sports betting assistant — explaining
odds, bet types, and markets in plain English.

## Features
- Multi-turn conversation with full context retention
- Custom system prompt defining persona, purpose, and responsible 
  gambling guardrails
- Clean error handling for API and connection failures
- Session reset without restarting the program

## Setup

**Requirements:** Python 3.x

1. Clone the repo
2. Install the Anthropic library:
   pip install anthropic
3. Set your API key as an environment variable:
   export ANTHROPIC_API_KEY=your_key_here   (Mac/Linux)
   set ANTHROPIC_API_KEY=your_key_here      (Windows)
4. Run:
   python chatbot.py

## Commands
Type naturally to chat. Special commands:
  reset  — clears conversation history, starts fresh context
  quit   — exits the program

## Architecture
Each user message is appended to a running conversation history list
which is passed in full to the API on every call. This is how all
LLM chat applications maintain context — the model has no memory of
its own, so the client is responsible for managing and sending the
full history each turn.

The system prompt is sent separately from the conversation history,
allowing the persona and rules to persist across resets without
appearing in the chat log.
