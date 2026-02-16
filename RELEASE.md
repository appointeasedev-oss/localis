# Localis Release Guide

## 🚀 How to Release on GitHub

### Method 1: Push a Tag (Recommended)

```bash
# Make sure you're on main branch
git checkout main
git pull

# Create a version tag
git tag v1.0.0

# Push the tag
git push origin v1.0.0
```

This will automatically trigger the GitHub Actions workflow and create a release!

### Method 2: Manual Release via GitHub UI

1. Go to: https://github.com/appointeasedev-oss/localis/releases
2. Click "Draft a new release"
3. Choose a tag version (e.g., v1.0.0)
4. Fill in release notes
5. Click "Publish release"

### What Gets Released

The GitHub Actions workflow automatically uploads:
- ✅ `localis.py` (main source)
- ✅ `install.sh` (Linux/macOS installer)
- ✅ `install.bat` (Windows installer)
- ✅ `requirements.txt` (dependencies)
- ✅ `README.md` (documentation)

## 📦 User Installation

### Linux/macOS
```bash
curl -fsSL https://raw.githubusercontent.com/appointeasedev-oss/localis/main/install.sh | bash
```

### Windows
```batch
# Download install.bat from releases
install.bat
```

### From Source
```bash
git clone https://github.com/appointeasedev-oss/localis.git
cd localis
pip install -r requirements.txt
python localis.py
```

## 🔄 Versioning

We use **Semantic Versioning** (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

Examples:
- `v1.0.0` - First stable release
- `v1.1.0` - Added new features
- `v1.1.1` - Bug fix
- `v2.0.0` - Breaking changes

## 🏷️ Creating Tags

```bash
# Patch release (bug fixes)
git tag v1.0.1
git push origin v1.0.1

# Minor release (new features)
git tag v1.1.0
git push origin v1.1.0

# Major release (breaking changes)
git tag v2.0.0
git push origin v2.0.0
```

## ✅ Checklist Before Release

- [ ] All tests pass
- [ ] Code is clean and documented
- [ ] README is updated
- [ ] Version number updated in code
- [ ] No debug code left
- [ ] Dependencies are correct

## 📝 Quick Release Commands

```bash
# Full release workflow
git add -A
git commit -m "Release v1.0.0"
git tag v1.0.0
git push origin main --tags

# Verify release
# Go to https://github.com/appointeasedev-oss/localis/releases
```

That's it! GitHub Actions handles everything else! 🎉
