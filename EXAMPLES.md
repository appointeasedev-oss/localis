# Localis Examples

## Example 1: First-time Setup

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
║                    ╔═══════════════════════════════════════╗                 ║
║                    ║     LOCAL AI SYSTEM - v1.0.0           ║                 ║
║                    ╚═══════════════════════════════════════╝                 ║
║                                                                              ║
║                         🚀 SYSTEM READY                                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

localis> /setup

⚡ QUICK SETUP WIZARD

Step 1/3: Ollama Setup
[✓] Ollama found

Step 2/3: Model Selection
Available models:
  1. llama3.2
  2. llama3.1
  3. codellama
  ...

Select model (1-10) or enter name: 1

✓ Set default model: llama3.2
📥 Pulling model: llama3.2... done

Step 3/3: Workspace Setup
Create new workspace? (y/n): y
Workspace name: my_project

✓ Workspace: /home/user/localis_workspace/my_project

🎉 Setup Complete!
```

## Example 2: Chat with AI

```bash
localis> help me create a REST API in Python

AI> I'll help you create a REST API. Let me set up a Flask application:

Creating file: app.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': []})

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    return jsonify({'user': data}), 201

if __name__ == '__main__':
    app.run(debug=True)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Done! I've created a basic Flask REST API. Want me to add authentication or database integration?
```

## Example 3: Clone GitHub Repository

```bash
localis> /workspace clone https://github.com/user/awesome-project.git

📥 Cloning repository: https://github.com/user/awesome-project.git
✓ Cloned to: /home/user/localis_workspace/awesome-project

localis> /workspace list
📁 awesome-project/
   📄 README.md
   📄 main.py
   📄 requirements.txt
   📄 tests/
```

## Example 4: Git Operations

```bash
localis> /git status
On branch main
Your branch is up to date with 'origin/main'.

localis> /git push "Added new feature via localis"
✓ Changes committed and pushed

localis> /git pull
✓ Pulled latest changes
```

## Example 5: File Operations

```bash
localis> /workspace cat config.json
{
  "database": "sqlite:///app.db"
}

localis> /workspace edit config.json
Enter old text to replace: sqlite:///app.db
Enter new text: postgresql://user:pass@localhost/db

✓ File updated successfully
```

## Example 6: Run Commands

```bash
localis> /workspace run npm install
📦 Installing dependencies...
✓ Done in 2.3s

localis> /workspace run python -m pytest
🧪 Running tests...
✓ All tests passed!
```

## Environment Variables

```bash
# Optional configuration
export OLLAMA_HOST=http://localhost:11434
export LOCALIS_THEME=dark
```

## Tips

1. **Use Tab completion** - Type partial commands and press Tab
2. **Memory persists** - Localis remembers your conversations
3. **Quick commands**:
   - `/status` - Quick system overview
   - `/clear` - Clear conversation
   - `/models pull codellama` - Download coding model
