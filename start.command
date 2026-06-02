#!/bin/zsh
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

launch_in_terminal() {
  local cmd="$1"
  osascript <<EOF >/dev/null
 tell application "Terminal"
   activate
   do script "cd '$PROJECT_DIR'; $cmd"
 end tell
EOF
}

# Start Streamlit app if nothing is already listening on 8501.
if ! lsof -iTCP:8501 -sTCP:LISTEN -t >/dev/null 2>&1; then
  launch_in_terminal "streamlit run app.py"
fi

# Start React dashboard if nothing is already listening on 5173.
if ! lsof -iTCP:5173 -sTCP:LISTEN -t >/dev/null 2>&1; then
  launch_in_terminal "npm run dev"
fi

# Open dashboard URL in default browser.
open "http://localhost:5173"
