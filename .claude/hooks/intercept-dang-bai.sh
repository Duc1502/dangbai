#!/bin/bash
# Intercept /dang-bai slash command and run the skill

# Read from stdin (hook passes JSON)
read -r INPUT
PROMPT=$(echo "$INPUT" | grep -o '"prompt"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)

# Check if prompt starts with /dang-bai
if [[ "$PROMPT" == "/dang-bai"* ]]; then
  # Get the project root
  SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

  # Run the skill
  cd "$PROJECT_ROOT"
  python skills/dang-bai/main.py

  # Return continue: false to prevent submission
  echo '{"continue": false, "systemMessage": "Running /dang-bai skill..."}'
  exit 0
fi

# Allow other prompts to be submitted normally
exit 0
