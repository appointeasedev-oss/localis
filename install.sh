#!/bin/bash

echo ""
echo "============================================================================"
echo "  LOCALIS v1.0.0 Installer by Sparrow"
echo "  https://github.com/appointeasedev-oss/localis"
echo "============================================================================"
echo ""

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check Python
echo -e "${CYAN}[1/5]${NC} Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python not found. Please install Python 3.8+${NC}"
    exit 1
fi
echo -e "${GREEN}[OK]${NC} Python found: $(python3 --version)"

# Install dependencies
echo ""
echo -e "${CYAN}[2/5]${NC} Installing dependencies..."
pip3 install -r requirements.txt --quiet
echo -e "${GREEN}[OK]${NC} Dependencies installed"

# Check/Start Ollama
echo ""
echo -e "${CYAN}[3/5]${NC} Checking Ollama..."
if ! command -v ollama &> /dev/null; then
    echo -e "${YELLOW}[WARNING]${NC} Ollama not found"
    echo "    Download: https://ollama.ai/download"
    echo "    Or: curl -fsSL https://ollama.ai/install.sh | sh"
else
    echo -e "${GREEN}[OK]${NC} Ollama found"
    
    # Start Ollama if not running
    echo -e "${CYAN}[4/5]${NC} Starting Ollama..."
    if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
        ollama serve &
        sleep 5
        
        if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
            echo -e "${GREEN}[OK]${NC} Ollama is running"
        else
            echo -e "${YELLOW}[WARNING]${NC} Ollama installed but not running"
            echo "    Run: ollama serve"
        fi
    else
        echo -e "${GREEN}[OK]${NC} Ollama is already running"
    fi
fi

# Create localis command
echo ""
echo -e "${CYAN}[5/5]${NC} Setting up localis command..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
LOCALIS_CMD="/usr/local/bin/localis"

cat > "$LOCALIS_CMD" << 'EOF'
#!/usr/bin/env bash
python3 "$(dirname "$0")/localis.py" "$@"
EOF

chmod +x "$LOCALIS_CMD"
chmod +x "$SCRIPT_DIR/localis.py"

echo -e "${GREEN}[OK]${NC} Command 'localis' created"

# Create directories
mkdir -p "$HOME/.localis/memory"
mkdir -p "$HOME/localis_workspace"
echo -e "${GREEN}[OK]${NC} Directories created"

echo ""
echo "============================================================================"
echo "  INSTALLATION COMPLETE!"
echo "============================================================================"
echo ""
echo -e "${CYAN}[INFO]${NC} To start localis:"
echo "    ${GREEN}localis${NC}"
echo ""
echo -e "${YELLOW}[FIRST TIME]${NC} Run ${GREEN}/setup${NC} to configure"
echo ""
echo "============================================================================"
echo "  LOCALIS v1.0.0 by Sparrow"
echo "  Repo: https://github.com/appointeasedev-oss/localis"
echo "============================================================================"
echo ""
