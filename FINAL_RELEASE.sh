#!/bin/bash
# Localis - Final Commit & Release Script

echo "=========================================="
echo "  🐦 LOCALIS - FINAL VERIFICATION"
echo "=========================================="
echo ""

# Check files exist
FILES=("localis.py" "install.sh" "install.bat" "requirements.txt" "README.md" "INSTALL.md" ".github/workflows/release.yml")

for f in "${FILES[@]}"; do
    if [ -f "$f" ]; then
        SIZE=$(wc -c < "$f")
        echo "✓ $f ($SIZE bytes)"
    else
        echo "✗ $f MISSING"
    fi
done

echo ""
echo "=========================================="
echo "  Git Commands to Run:"
echo "=========================================="
echo ""
echo "# Stage all files:"
echo "git add -A"
echo ""
echo "# Create commit:"
echo 'git commit -m "Release v1.0.0: localis by Sparrow

🐦 localis - A powerful local AI coding assistant

Features:
- 100% local AI powered by Ollama
- Auto-install Ollama and models
- Workspace management with GitHub clone
- Interactive chat with memory
- Git integration
- Premium ASCII UI

Repo: https://github.com/appointeasedev-oss/localis"'
echo ""
echo "# Add remote (first time):"
echo "git remote add origin https://github.com/appointeasedev-oss/localis.git"
echo ""
echo "# Push:"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "# Create release:"
echo "git tag v1.0.0"
echo "git push origin v1.0.0"
echo ""
echo "=========================================="
