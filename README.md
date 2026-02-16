# Localis - Local AI Command Line System

<div align="center">

![Localis Logo](https://via.placeholder.com/400x100/1a1a2e/00d9ff?text=LOCALIS)

**🐦 localis - A powerful local AI coding assistant by Sparrow**

[![GitHub release](https://img.shields.io/github/release/appointeasedev-oss/localis.svg)](https://github.com/appointeasedev-oss/localis/releases)
[![License](https://img.shields.io/github/license/appointeasedev-oss/localis.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)

</div>

---

## ✨ Features

- 🐦 **localis** - AI-powered coding assistant built by Sparrow
- 🤖 **100% Local** - Your code never leaves your machine
- 📦 **Auto-Install Ollama** - No manual setup required
- 🧠 **Smart Memory** - Long-term and short-term context
- 📁 **Workspace Manager** - Clone repos, manage files
- 💬 **Interactive Chat** - Conversational AI coding
- 🐙 **Git Integration** - Push, pull, commit
- 🎨 **Premium UI** - Beautiful ASCII art interface
- 🔒 **Privacy First** - No cloud APIs, no tracking

---

## 🚀 Quick Install

### Linux/macOS
```bash
curl -fsSL https://raw.githubusercontent.com/appointeasedev-oss/localis/main/install.sh | bash
```

### Windows
```powershell
# Download from Releases or run:
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

## 📖 Usage

### First Run
```bash
localis
```

### Commands

| Command | Description |
|---------|-------------|
| `/setup` | Quick setup wizard |
| `/models` | Manage AI models |
| `/workspace` | Manage workspace |
| `/chat` | Start AI chat |
| `/git` | Git operations |
| `/help` | Show help |

---

## 🎯 Model Support

All Ollama models supported:
- **llama3.2** (default)
- **codellama** (coding)
- **mistral** (balanced)
- **deepseek-coder**
- And many more!

Auto-downloads on first use!

---

## 📁 Project Structure

```
localis/
├── localis.py          # Main application
├── install.sh          # Linux/macOS installer
├── install.bat         # Windows installer
├── requirements.txt    # Python deps
├── README.md           # This file
├── INSTALL.md         # Detailed installation guide
├── EXAMPLES.md         # Usage examples
├── RELEASE.md         # Release workflow
└── LICENSE            # MIT License
```

---

## 🔧 Configuration

Stored in `~/.localis/config.json`:
```json
{
  "default_model": "llama3.2",
  "fallback_models": ["codellama", "mistral"],
  "workspace": "~/localis_workspace",
  "auto_pull": true
}
```

---

## 🐙 GitHub Release

Push a tag to trigger auto-release:
```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions automatically creates the release!

---

## 📝 License

MIT License - See [LICENSE](LICENSE)

---

<div align="center">

**🐦 Built with ❤️ by Sparrow**

[Repo](https://github.com/appointeasedev-oss/localis) • 
[Issues](https://github.com/appointeasedev-oss/localis/issues)

</div>
