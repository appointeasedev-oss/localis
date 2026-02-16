# Localis - Installation & Usage Guide

<div align="center">

**🐦 localis v1.0.0 by Sparrow**

*A powerful local AI coding assistant*

</div>

---

## 🚀 Quick Install

### Linux/macOS
```bash
curl -fsSL https://raw.githubusercontent.com/appointeasedev-oss/localis/main/install.sh | bash
localis
```

### Windows
```powershell
# Download install.bat from Releases and run as Administrator
# OR:
winget install Ollama.Ollama
pip install requests
python localis.py
```

### From Source
```bash
git clone https://github.com/appointeasedev-oss/localis.git
cd localis
pip install -r requirements.txt
python localis.py
```

---

## 🛠️ First-Time Setup

When you run localis for the first time:

```bash
$ localis

╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗██████╗  █████╗ ██╗      ██╗   ██╗  ║
║   ████╗ ████║██╔══██╗██║████╗  ██║██╔════╝██╔══██╗██╔══██╗██║      ██║   ██║  ║
║   ██╔████╔██║███████║██║██╔██╗ ██║█████╗  ██████╔╝███████║██║      ██║   ██║  ║
║   ██║╚██╔╝██║██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║██║      ██║   ██║  ║
║   ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████╗██║  ██║██║  ██║███████╗╚██████╔╝  ║
║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝   ║
║                                                                              ║
║                    ╔═══════════════════════════════════════════════════════╗     ║
║                    ║                                                          ║     ║
║                    ║   ██████╗ ██████╗ ██████╗ ███████╗                      ║     ║
║                    ║   ██╔══██╗██╔══██╗██╔══██╗██╔════╝                      ║     ║
║                    ║   ██████╔╝██████╔╝██████╔╝███████╗                      ║     ║
║                    ║   ██╔═══╝ ██╔══██╗██╔══██╗╚════██║                      ║     ║
║                    ║   ██║     ██║  ██║██║  ██║███████║                      ║     ║
║                    ║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                      ║     ║
║                    ║                   BY SPARROW                             ║     ║
║                    ╚═══════════════════════════════════════════════════════════╝     ║
║                                                                              ║
║                    🐦 localis v1.0.0 by Sparrow                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

localis> /setup
```

The setup wizard will:
1. ✅ Check/install Ollama
2. ✅ Download default model (llama3.2)
3. ✅ Create workspace folder
4. ✅ Save all settings

---

## 💬 Basic Usage

### Chat with AI
```bash
localis> create a Python calculator
```

### Manage Models
```bash
localis> /models           # List all models
localis> /models pull codellama  # Download coding model
localis> /models use llama3.2   # Switch model
```

### Workspace
```bash
localis> /workspace new myproject        # Create workspace
localis> /workspace clone <github-url>   # Clone repo
localis> /workspace list                 # List files
localis> /workspace cat app.py           # Read file
localis> /workspace edit app.py          # Edit file
localis> /workspace run npm install      # Run command
```

### Git Operations
```bash
localis> /git status       # Check status
localis> /git pull         # Pull changes
localis> /git push "my message"  # Commit & push
```

---

## 📋 Commands Reference

| Command | Description |
|---------|-------------|
| `/setup` | Quick configuration wizard |
| `/models` | List/select/download AI models |
| `/workspace` | Manage workspace & files |
| `/chat` | Start AI chat session |
| `/git` | Git operations |
| `/memory` | View/clear memory |
| `/status` | Current system status |
| `/help` | Show help |

---

## 🐧 Linux Installation

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Clone and run localis
git clone https://github.com/appointeasedev-oss/localis.git
cd localis

# Install and create global command
chmod +x install.sh
./install.sh

# Run localis
localis
```

**After install, simply run:**
```bash
localis
```

---

## 🍎 macOS Installation

```bash
# Install Ollama
# Download from: https://ollama.ai/download
# OR: brew install ollama

# Clone and run
git clone https://github.com/appointeasedev-oss/localis.git
cd localis
chmod +x install.sh
./install.sh

localis
```

---

## 🪟 Windows Installation

**Option 1: Download from Releases**
1. Download `install.bat` from [Releases](https://github.com/appointeasedev-oss/localis/releases)
2. Run as Administrator

**Option 2: PowerShell**
```powershell
# Install Ollama
winget install Ollama.Ollama

# Clone and run
git clone https://github.com/appointeasedev-oss/localis.git
cd localis
pip install requests
python localis.py
```

---

## 🚨 Troubleshooting

### "Ollama not found"
```bash
# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows/macOS
# Download from https://ollama.ai/download
```

### "Model not found"
```bash
localis> /models pull llama3.2
```

### Connection refused
```bash
# Start Ollama
ollama serve

# On Windows, run the Ollama app
```

---

## 📦 What Gets Installed

```
~/.localis/
├── config.json          # Your settings
└── memory/
    ├── long_term.json   # Project memories
    └── short_term.json # Conversation history

~/localis_workspace/     # Your code projects

/usr/local/bin/localis   # Global command (Linux/macOS)
```

---

## 🔄 Updating Localis

```bash
# Get latest version
git pull origin main

# Or download new release from GitHub
# https://github.com/appointeasedev-oss/localis/releases
```

---

## 🤝 Support

- **Issues**: https://github.com/appointeasedev-oss/localis/issues
- **Discussions**: https://github.com/appointeasedev-oss/localis/discussions

---

<div align="center">

**🐦 Built with ❤️ by Sparrow**

[Repo](https://github.com/appointeasedev-oss/localis)

</div>
