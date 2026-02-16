#!/bin/bash

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                              ║
# ║   ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗██████╗  █████╗ ██╗      ██╗   ██╗  ║
# ║   ████╗ ████║██╔══██╗██║████╗  ██║██╔════╝██╔══██╗██╔══██╗██║      ██║   ██║  ║
# ║   ██╔████╔██║███████║██║██╔██╗ ██║█████╗  ██████╔╝███████║██║      ██║   ██║  ║
# ║   ██║╚██╔╝██║██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║      ██║   ██║  ║
# ║   ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████╗██║  ██║██║  ██║███████╗╚██████╔╝  ║
# ║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ║
# ║                                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                  🐦 LOCALIS - Git Setup & Push 🐦                          ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

cd "$(dirname "$0")"

# Check if git initialized
if [ ! -d ".git" ]; then
    echo -e "${CYAN}[1/5]${NC} Initializing Git..."
    git init
    echo -e "${GREEN}[✓]${NC} Git initialized"
else
    echo -e "${GREEN}[✓]${NC} Git already initialized"
fi

# Check if remote exists
if ! git remote get-url origin &>/dev/null; then
    echo ""
    echo -e "${CYAN}[2/5]${NC} Adding remote origin..."
    echo -e "${YELLOW}Create empty repo at https://github.com/new first!${NC}"
    echo ""
    read -p "   Repo URL: " REPO_URL
    if [ -n "$REPO_URL" ]; then
        git remote add origin "$REPO_URL"
        echo -e "${GREEN}[✓]${NC} Remote added"
    else
        echo -e "${YELLOW}[SKIP]${NC} No URL provided"
    fi
else
    echo -e "${GREEN}[✓]${NC} Remote already configured"
fi

# Stage all files
echo ""
echo -e "${CYAN}[3/5]${NC} Staging all files..."
git add -A
echo -e "${GREEN}[✓]${NC} Files staged"

# Create initial commit
echo ""
echo -e "${CYAN}[4/5]${NC} Creating initial commit..."
git commit -m "Initial commit: localis v1.0.0 by Sparrow

🐦 localis - A powerful local AI coding assistant
- 100% local, powered by Ollama
- Auto-install Ollama and models
- Workspace management with GitHub clone
- Interactive chat with memory
- Git integration
- Premium ASCII UI

Repo: https://github.com/appointeasedev-oss/localis"
echo -e "${GREEN}[✓]${NC} Commit created"

# Push to GitHub
echo ""
echo -e "${CYAN}[5/5]${NC} Pushing to GitHub..."
echo ""
git branch -M main
git push -u origin main

echo ""
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                         ✅ UPLOAD COMPLETE! 🐦                             ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${CYAN}NEXT STEP - Create release:${NC}"
echo ""
echo "   1. Go to: https://github.com/appointeasedev-oss/localis/releases"
echo "   2. Click: Draft a new release"
echo "   3. Tag: v1.0.0"
echo "   4. Title: Release v1.0.0"
echo "   5. Publish release"
echo ""
echo -e "${YELLOW}OR via command:${NC}"
echo "   git tag v1.0.0"
echo "   git push origin v1.0.0"
echo ""
