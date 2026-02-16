#!/usr/bin/env python3
"""
localis - A powerful local AI coding assistant by Sparrow
Powered by Ollama | 100% Local | No Cloud
Repo: https://github.com/appointeasedev-oss/localis
"""

import os
import sys
import json
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Tuple

# Version & Branding
__version__ = "1.0.0"
__author__ = "Sparrow"
__repo__ = "https://github.com/appointeasedev-oss/localis"

# Colors for terminal
C = {
    'HEADER': '\033[95m', 'BLUE': '\033[94m', 'CYAN': '\033[96m',
    'GREEN': '\033[92m', 'YELLOW': '\033[93m', 'RED': '\033[91m',
    'ENDC': '\033[0m', 'BOLD': '\033[1m', 'MAGENTA': '\033[35m'
}

# Config file location
CONFIG_DIR = Path.home() / ".localis"
CONFIG_FILE = CONFIG_DIR / "config.json"
MEMORY_DIR = CONFIG_DIR / "memory"
SHORT_TERM_MEMORY = MEMORY_DIR / "short_term.json"


def print_banner():
    print(f"""
{C['MAGENTA']}╔════════════════════════════════════════════════════════════════════════════════╗{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}                                                                              {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}██{C['MAGENTA']}╗  {C['CYAN']}██{C['MAGENTA']}╗  {C['CYAN']}█████╗{C['MAGENTA']}║{C['CYAN']}  ██╗███╗  {C['MAGENTA']}║{C['CYAN']}  ██╗  █████╗  ██╗   ██╗{C['MAGENTA']}║{C['ENDC']}   {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}██{C['MAGENTA']}║{C['CYAN']} ████╗ {C['MAGENTA']}║{C['CYAN']} ██╔══██╗{C['MAGENTA']}║{C['CYAN']} ██║████╗ {C['MAGENTA']}║{C['CYAN']}  ██║{C['MAGENTA']}╔════╝██╔══██╗{C['MAGENTA']}║{C['ENDC']}   {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}██{C['MAGENTA']}║{C['CYAN']}╚████╔╝{C['MAGENTA']}║{C['CYAN']} ███████║{C['MAGENTA']}║{C['CYAN']} ██║██╔██╗{C['MAGENTA']}║{C['CYAN']}  ██║{C['MAGENTA']}║{C['CYAN']}  ██████╔╝{C['MAGENTA']}║{C['ENDC']}   {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}██{C['MAGENTA']}║{C['CYAN']}  ╚██╔╝ {C['MAGENTA']}║{C['CYAN']} ██╔══██║{C['MAGENTA']}║{C['CYAN']} ██║██║╚██╗{C['MAGENTA']}║{C['CYAN']}  ██║{C['MAGENTA']}║{C['CYAN']}  ██╔══██╗{C['MAGENTA']}║{C['ENDC']}   {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}██{C['MAGENTA']}║{C['CYAN']}   ██║  {C['MAGENTA']}║{C['CYAN']} ██║  ██║{C['MAGENTA']}║{C['CYAN']} ██║██║ ╚████║{C['MAGENTA']}║{C['CYAN']}  ██║{C['MAGENTA']}║{C['CYAN']}  ██║  ██║{C['MAGENTA']}║{C['CYAN']}███████╗╚██████╔╝{C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}╚═╝{C['MAGENTA']}   ╚═╝  {C['MAGENTA']}║{C['CYAN']} ╚═╝  ╚═╝{C['MAGENTA']}║{C['CYAN']} ╚═╝╚═╝  ╚═══╝{C['MAGENTA']}║{C['CYAN']}  ╚═╝{C['MAGENTA']}║{C['CYAN']}  ╚═╝  ╚═╝{C['MAGENTA']}║{C['CYAN']}╚══════╝ ╚═════╝ {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}                                                                              {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['GREEN']}╔═══════════════════════════════════════════════════════════════════╗{C['MAGENTA']}   ║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['GREEN']}║{C['ENDC']}                  localis v{__version__} by Sparrow                         {C['GREEN']}║{C['MAGENTA']}   ║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['GREEN']}╚═══════════════════════════════════════════════════════════════════╝{C['MAGENTA']}   ║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}   {C['CYAN']}Repo: {__repo__}{C['MAGENTA']}                                              ║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}                                                                              {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}╚════════════════════════════════════════════════════════════════════════════════╝{C['ENDC']}
""")


def print_status(model: str, ws: str, ollama_status: str):
    print(f"""
{C['BLUE']}╔════════════════════════════════════════════════════════════════════════════════╗{C['ENDC']}
{C['BLUE']}║{C['ENDC']}                          SYSTEM STATUS                                {C['BLUE']}║{C['ENDC']}
{C['BLUE']}╠════════════════════════════════════════════════════════════════════════════════╣{C['ENDC']}
{C['BLUE']}║{C['ENDC']}  {C['CYAN']}AI Model:{C['ENDC']}    {model:<55}  {C['BLUE']}║{C['ENDC']}
{C['BLUE']}║{C['ENDC']}  {C['CYAN']}Workspace:{C['ENDC']}   {ws:<55}  {C['BLUE']}║{C['ENDC']}
{C['BLUE']}║{C['ENDC']}  {C['CYAN']}Ollama:{C['ENDC']}      {ollama_status:<55}  {C['BLUE']}║{C['ENDC']}
{C['BLUE']}║{C['ENDC']}  {C['CYAN']}Version:{C['ENDC']}     v{__version__:<54}  {C['BLUE']}║{C['ENDC']}
{C['BLUE']}╚════════════════════════════════════════════════════════════════════════════════╝{C['ENDC']}
""")


def print_help():
    print(f"""
{C['MAGENTA']}╔════════════════════════════════════════════════════════════════════════════════╗{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}                         AVAILABLE COMMANDS                          {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}╠════════════════════════════════════════════════════════════════════════════════╣{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/setup{C['ENDC']}       Quick setup wizard                                    {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/models{C['ENDC']}      Manage AI models (list, pull, use)                  {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/workspace{C['ENDC']}   Manage workspace (list, clone, edit, run)           {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/template{C['ENDC']}    Create project from templates                       {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/code{C['ENDC']}       Run code files (Python, Node, etc)                {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/chat{C['ENDC']}       Start AI chat session                              {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/git{C['ENDC']}        Git operations (status, push, pull)               {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/web{C['ENDC']}        Web tools (fetch URL)                              {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/memory{C['ENDC']}      Memory management                                  {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/system{C['ENDC']}      System information                                {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/help{C['ENDC']}       Show this help                                    {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}║{C['ENDC']}  {C['GREEN']}/quit{C['ENDC']}       Exit localis                                       {C['MAGENTA']}║{C['ENDC']}
{C['MAGENTA']}╚════════════════════════════════════════════════════════════════════════════════╝{C['ENDC']}
""")


class Config:
    def __init__(self):
        self.data = {
            "default_model": "llama3.2",
            "workspace": str(Path.home() / "localis_workspace"),
            "ollama_host": "http://localhost:11434",
            "installed_version": __version__
        }
        self.load()
    
    def load(self):
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    self.data.update(json.load(f))
            except:
                pass
    
    def save(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)
    
    def get(self, k, d=None):
        return self.data.get(k, d)
    
    def set(self, k, v):
        self.data[k] = v
        self.save()


class Memory:
    def __init__(self):
        MEMORY_DIR.mkdir(parents=True, exist_ok=True)
        self.data = {"conversation": []}
        self.load()
    
    def load(self):
        if SHORT_TERM_MEMORY.exists():
            try:
                with open(SHORT_TERM_MEMORY, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except:
                pass
    
    def save(self):
        with open(SHORT_TERM_MEMORY, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2)
    
    def add(self, role, content):
        self.data["conversation"].append({
            "role": role, "content": content,
            "timestamp": datetime.now().isoformat()
        })
        if len(self.data["conversation"]) > 100:
            self.data["conversation"] = self.data["conversation"][-100:]
        self.save()
    
    def get_convo(self):
        return self.data["conversation"]
    
    def clear(self):
        self.data["conversation"] = []
        self.save()


class Ollama:
    def __init__(self):
        self.host = "http://localhost:11434"
    
    def installed(self):
        return shutil.which("ollama") is not None
    
    def running(self):
        try:
            r = subprocess.run(
                ["curl", "-s", f"{self.host}/api/tags"],
                capture_output=True, timeout=3
            )
            return r.returncode == 0
        except:
            return False
    
    def start(self):
        """Auto-start Ollama."""
        if self.running():
            return True
        
        print(f"{C['CYAN']}Starting Ollama...{C['ENDC']}")
        
        # Try multiple methods
        methods = [
            ["ollama", "serve"],
            [sys.executable, "-m", "ollama"] if sys.platform == "win32" else None
        ]
        
        for cmd in methods:
            if cmd is None:
                continue
            try:
                subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                import time
                for _ in range(10):
                    time.sleep(1)
                    if self.running():
                        print(f"{C['GREEN']}Ollama started!{C['ENDC']}")
                        return True
            except:
                continue
        
        print(f"{C['YELLOW']}Ollama not found. Please install from https://ollama.ai{C['ENDC']}")
        return False
    
    def get_installed(self):
        """Fetch installed models from Ollama API."""
        try:
            r = subprocess.run(
                ["curl", "-s", f"{self.host}/api/tags"],
                capture_output=True, text=True, timeout=5
            )
            if r.returncode == 0:
                data = json.loads(r.stdout)
                return [m["name"] for m in data.get("models", [])]
        except:
            pass
        return []
    
    def all_models(self):
        return [
            "llama3.2", "llama3.1", "llama3", "llama2",
            "codellama", "codellama:7b", "codellama:13b", "codellama:34b",
            "deepseek-coder", "deepseek-coder:6.7b", "deepseek-coder:33b",
            "qwen2.5-coder", "qwen2.5-coder:1.5b", "qwen2.5-coder:7b",
            "wizardcoder", "wizardcoder:13b", "starcoder",
            "mistral", "mistral:7b", "neural-chat",
            "gemma", "gemma:2b", "gemma:7b", "phi3", "phi3:3.8b",
            "llava", "llava:7b", "llava:13b", "bakllava", "moondream"
        ]
    
    def pull(self, name):
        print(f"{C['CYAN']}Downloading {name}...{C['ENDC']}")
        try:
            r = subprocess.run(["ollama", "pull", name], capture_output=True, text=True)
            return r.returncode == 0
        except:
            return False
    
    def chat(self, model, messages):
        import requests
        url = f"{self.host}/api/chat"
        payload = {"model": model, "messages": messages, "stream": True}
        
        try:
            resp = requests.post(url, json=payload, stream=True, timeout=60)
            resp.raise_for_status()
            full = ""
            for line in resp.iter_lines():
                if line:
                    data = json.loads(line)
                    if "message" in data:
                        content = data["message"].get("content", "")
                        full += content
                        print(content, end="", flush=True)
            print()
            return full
        except Exception as e:
            print(f"{C['RED']}Chat error: {e}{C['ENDC']}")
            return ""


class Workspace:
    def __init__(self):
        self.path = None
    
    def set(self, p):
        self.path = Path(p)
        self.path.mkdir(parents=True, exist_ok=True)
        return self.path
    
    def get(self):
        if not self.path:
            return Path.home() / "localis_workspace"
        return self.path
    
    def create(self, name):
        base = Path.home() / "localis_workspace"
        base.mkdir(parents=True, exist_ok=True)
        p = base / name
        p.mkdir(exist_ok=True)
        self.path = p
        return p
    
    def clone(self, url):
        print(f"{C['CYAN']}Cloning {url}...{C['ENDC']}")
        name = url.split("/")[-1].replace(".git", "")
        target = Path.home() / "localis_workspace" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        
        if target.exists():
            shutil.rmtree(target)
        
        try:
            r = subprocess.run(
                ["git", "clone", url, str(target)],
                capture_output=True, text=True, timeout=60
            )
            if r.returncode == 0:
                print(f"{C['GREEN']}Cloned to {target}{C['ENDC']}")
                self.path = target
                return target
        except:
            pass
        print(f"{C['RED']}Clone failed{C['ENDC']}")
        return None
    
    def files(self):
        ws = self.get()
        if ws.exists():
            return list(ws.rglob("*"))
        return []
    
    def read(self, fpath):
        full = self.get() / fpath
        if full.exists():
            try:
                with open(full, 'r', encoding='utf-8') as fp:
                    return fp.read(), True
            except:
                pass
        return None, False
    
    def write(self, fpath, content):
        full = self.get() / fpath
        full.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(full, 'w', encoding='utf-8') as fp:
                fp.write(content)
            return True
        except:
            return False
    
    def run(self, cmd):
        ws = self.get()
        try:
            r = subprocess.run(cmd, shell=True, cwd=str(ws),
                             capture_output=True, text=True, timeout=120)
            return r.returncode, r.stdout, r.stderr
        except Exception as e:
            return -1, "", str(e)


class Git:
    def __init__(self, ws):
        self.ws = ws
    
    def is_repo(self):
        return (self.ws.get() / ".git").exists()
    
    def status(self):
        c, out, _ = self.ws.run("git status")
        return out if c == 0 else "Not a git repo"
    
    def push(self, msg="Update via localis"):
        self.ws.run("git add -A")
        self.ws.run(f'git commit -m "{msg}"')
        c, out, err = self.ws.run("git push")
        return c == 0, out + err


class Localis:
    def __init__(self):
        self.cfg = Config()
        self.mem = Memory()
        self.ollama = Ollama()
        self.ws = Workspace()
        self.git = Git(self.ws)
        
        if self.cfg.get("workspace"):
            p = Path(self.cfg.get("workspace"))
            if p.exists():
                self.ws.set(str(p))
    
    def run(self):
        print_banner()
        
        # Auto-start Ollama
        self.ollama.start()
        
        # Show status
        m = self.cfg.get("default_model", "Not set")
        ws = str(self.ws.get())
        ostat = f"{C['GREEN']}Running{C['ENDC']}" if self.ollama.running() else f"{C['RED']}Stopped{C['ENDC']}"
        print_status(m, ws, ostat)
        
        print_help()
        
        print(f"{C['CYAN']}Ready! Type a message or command.{C['ENDC']}\n")
        
        while True:
            try:
                inp = input(f"{C['GREEN']}localis{C['ENDC']}> ").strip()
                if not inp:
                    continue
                if inp.lower() in ['quit', 'exit', 'q']:
                    print(f"{C['CYAN']}Goodbye!{C['ENDC']}")
                    break
                if inp.startswith('/'):
                    self.handle_cmd(inp)
                else:
                    self.chat(inp)
            except KeyboardInterrupt:
                print(f"\n{C['CYAN']}Goodbye!{C['ENDC']}")
                break
            except Exception as e:
                print(f"{C['RED']}Error: {e}{C['ENDC']}")
    
    def handle_cmd(self, cmd):
        parts = cmd.split()
        base = parts[0].lower()
        args = parts[1:]
        
        handlers = {
            '/setup': self.cmd_setup,
            '/models': self.cmd_models,
            '/workspace': lambda: self.cmd_workspace(args),
            '/chat': lambda: self.cmd_chat(' '.join(args) if args else None),
            '/help': lambda: print_help(),
            '/status': self.cmd_status,
            '/git': lambda: self.cmd_git(args),
            '/web': lambda: self.cmd_web(args),
            '/memory': self.cmd_memory,
            '/system': self.cmd_system,
            '/quit': lambda: sys.exit(0),
            '/exit': lambda: sys.exit(0),
        }
        
        if base in handlers:
            handlers[base]()
        else:
            print(f"{C['RED']}Unknown command: {base}{C['ENDC']}")
    
    def cmd_status(self):
        m = self.cfg.get("default_model", "Not set")
        ws = str(self.ws.get())
        ostat = f"{C['GREEN']}Running{C['ENDC']}" if self.ollama.running() else f"{C['RED']}Stopped{C['ENDC']}"
        print_status(m, ws, ostat)
    
    def cmd_setup(self):
        print(f"\n{C['CYAN']}=== QUICK SETUP ==={C['ENDC']}\n")
        
        print(f"{C['YELLOW']}Step 1/3: Ollama{C['ENDC']}")
        self.ollama.start()
        
        print(f"\n{C['YELLOW']}Step 2/3: Model{C['ENDC']}")
        installed = self.ollama.get_installed()
        if installed:
            print(f"{C['GREEN']}Installed: {', '.join(installed)}{C['ENDC']}")
        else:
            print(f"{C['YELLOW']}Installing llama3.2...{C['ENDC']}")
            self.ollama.pull("llama3.2")
        
        choice = input(f"\n{C['CYAN']}Select model: {C['ENDC']}").strip() or "llama3.2"
        self.cfg.set("default_model", choice)
        print(f"{C['GREEN']}Model: {choice}{C['ENDC']}")
        
        print(f"\n{C['YELLOW']}Step 3/3: Workspace{C['ENDC']}")
        name = input(f"{C['CYAN']}Workspace name: {C['ENDC']}").strip() or "myproject"
        ws = self.ws.create(name)
        self.cfg.set("workspace", str(ws))
        
        print(f"\n{C['GREEN']}Setup Complete!{C['ENDC']}")
        self.cmd_status()
    
    def cmd_models(self):
        installed = self.ollama.get_installed()
        all_models = self.ollama.all_models()
        current = self.cfg.get("default_model")
        
        print(f"\n{C['MAGENTA']}╔════════════════════════════════════════════════════════════════════════╗{C['ENDC']}")
        print(f"{C['MAGENTA']}║{C['ENDC']}                            AI MODELS                           {C['MAGENTA']}║{C['ENDC']}")
        print(f"{C['MAGENTA']}╠════════════════════════════════════════════════════════════════════════╣{C['ENDC']}")
        
        if installed:
            print(f"{C['CYAN']}║{C['ENDC']}  INSTALLED:{C['MAGENTA']}                                                      ║{C['ENDC']}")
            for m in installed:
                mrk = " <==" if m == current else ""
                print(f"{C['GREEN']}║{C['ENDC']}  [OK] {m:<20}{mrk:<35}{C['MAGENTA']}║{C['ENDC']}")
        else:
            print(f"{C['YELLOW']}║{C['ENDC']}  No models installed yet{C['MAGENTA']:<53}║{C['ENDC']}")
        
        print(f"{C['CYAN']}║{C['ENDC']}{C['MAGENTA']}║{C['ENDC']}")
        print(f"{C['CYAN']}║{C['ENDC']}  AVAILABLE ({len(all_models)} models):{C['MAGENTA']:<49}║{C['ENDC']}")
        print(f"{C['CYAN']}║{C['ENDC']}{C['MAGENTA']}╠{'─'*58}╣{C['ENDC']}")
        
        for i, m in enumerate(all_models[:15], 1):
            if m in installed:
                st = f"{C['GREEN']}[INSTALLED]{C['MAGENTA']}"
            else:
                st = f"{C['YELLOW']}[NOT INSTALLED]{C['MAGENTA']}"
            print(f"{C['CYAN']}║{C['ENDC']}  {i:2}. {m:<20} {st}{C['MAGENTA']:<25}║{C['ENDC']}")
        
        print(f"{C['MAGENTA']}╚════════════════════════════════════════════════════════════════════════╝{C['ENDC']}")
        print(f"\n{C['CYAN']}Commands: /models pull <name> | /models use <name>{C['ENDC']}\n")
    
    def cmd_workspace(self, args):
        print(f"\n{C['CYAN']}=== WORKSPACE ==={C['ENDC']}\n")
        print(f"{C['CYAN']}Current: {self.ws.get()}{C['ENDC']}")
        print(f"\n{C['CYAN']}Commands:{C['ENDC']}")
        print("  /workspace list     - List files")
        print("  /workspace new <n>  - Create workspace")
        print("  /workspace clone <url> - Clone repo")
        print("  /workspace cat <f>  - Read file")
        print("  /workspace run <c>  - Run command")
        
        if args:
            if args[0] == "list":
                for f in self.ws.files()[:20]:
                    print(f"  {'[DIR] ' if f.is_dir() else '[FILE]'} {f.relative_to(self.ws.get())}")
            elif args[0] == "cat" and len(args) > 1:
                c, ok = self.ws.read(args[1])
                if ok:
                    print(c[:1000])
                else:
                    print(f"{C['RED']}File not found{C['ENDC']}")
            elif args[0] == "run" and len(args) > 1:
                c, out, err = self.ws.run(' '.join(args[1:]))
                print(out)
                if err:
                    print(f"{C['RED']}{err}{C['ENDC']}")
    
    def cmd_chat(self, prompt=None):
        if not self.cfg.get("default_model"):
            print(f"{C['RED']}Run /setup first{C['ENDC']}")
            return
        
        self.ollama.start()
        
        if not self.ollama.running():
            print(f"{C['RED']}Ollama not running. Start with: ollama serve{C['ENDC']}")
            return
        
        if not prompt:
            print(f"\n{C['CYAN']}=== CHAT MODE (type 'quit' to exit) ==={C['ENDC']}\n")
            while True:
                try:
                    inp = input(f"{C['GREEN']}You{C['ENDC']}> ").strip()
                    if inp.lower() in ['quit', 'exit', 'q']:
                        break
                    if not inp:
                        continue
                    self.mem.add("user", inp)
                    print(f"{C['CYAN']}AI{C['ENDC']}> ", end="")
                    self.ollama.chat(self.cfg.get("default_model"), [{"role": "user", "content": inp}])
                except KeyboardInterrupt:
                    break
        else:
            self.mem.add("user", prompt)
            print(f"{C['CYAN']}AI{C['ENDC']}> ", end="")
            self.ollama.chat(self.cfg.get("default_model"), [{"role": "user", "content": prompt}])
    
    def cmd_git(self, args):
        print(f"\n{C['CYAN']}=== GIT ==={C['ENDC']}\n")
        if not self.git.is_repo():
            print(f"{C['YELLOW']}Not a git repo{C['ENDC']}")
            return
        print(self.git.status())
        print(f"\n{C['CYAN']}Commands: /git push <msg> | /git status{C['ENDC']}")
        
        if args and args[0] == "push":
            msg = ' '.join(args[1:]) if len(args) > 1 else "Update via localis"
            ok, out = self.git.push(msg)
            print(out)
    
    def cmd_web(self, args):
        print(f"\n{C['CYAN']}=== WEB ==={C['ENDC']}\n")
        print(f"{C['CYAN']}Commands: /web fetch <url>{C['ENDC']}")
        
        if args and args[0] == "fetch" and len(args) > 1:
            try:
                import requests
                r = requests.get(args[1], timeout=10)
                print(r.text[:1000])
            except Exception as e:
                print(f"{C['RED']}Error: {e}{C['ENDC']}")
    
    def cmd_memory(self):
        print(f"\n{C['CYAN']}=== MEMORY ==={C['ENDC']}\n")
        print(f"{C['CYAN']}Messages: {len(self.mem.get_convo())}{C['ENDC']}")
        print(f"{C['CYAN']}Commands: /memory clear{C['ENDC']}")
    
    def cmd_system(self):
        import platform
        print(f"\n{C['CYAN']}=== SYSTEM ==={C['ENDC']}\n")
        print(f"  OS:       {platform.system()} {platform.release()}")
        print(f"  Python:   {platform.python_version()}")
        print(f"  localis:  v{__version__}")
        print(f"  Workspace: {self.ws.get()}")
        print(f"  Files:    {len(self.ws.files())}")


if __name__ == "__main__":
    Localis().run()
