# 🔒 Django DEBUG Security Protection

This repository implements **multiple layers of protection** to prevent committing Django applications with `DEBUG=True` enabled, which is a critical security vulnerability in production.

## 🛡️ Protection Layers

### 1. **Pre-commit Hook** (Primary Protection)
- **Location**: `.git/hooks/pre-commit` (Unix/Linux/Mac) & `.git/hooks/pre-commit.bat` (Windows)
- **Function**: Automatically runs before every commit
- **Action**: Scans all `settings.py` files and **blocks commits** if `DEBUG=True` is found

### 2. **GitHub Actions Workflow** (CI/CD Protection)
- **Location**: `.github/workflows/debug-check.yml`
- **Function**: Runs on every push/pull request to main/develop branches
- **Action**: **Fails the build** if `DEBUG=True` is detected, preventing merges

### 3. **Python Checker Script** (Manual Verification)
- **Location**: `scripts/check_debug.py`
- **Function**: Standalone script for manual checking
- **Usage**: 
  ```bash
  python scripts/check_debug.py           # Check all settings files
  python scripts/check_debug.py --strict  # Exit with error if DEBUG=True
  ```

## 🚀 How It Works

### Pre-commit Protection Flow:
```
Developer commits → Pre-commit hook runs → Scans settings.py → 
   ↓
   ├─ DEBUG=False found → ✅ Commit allowed
   └─ DEBUG=True found  → ❌ Commit blocked with helpful message
```

### GitHub Actions Protection Flow:
```
Code pushed → GitHub Actions trigger → Security check runs →
   ↓
   ├─ DEBUG=False → ✅ Build passes → Merge allowed
   └─ DEBUG=True  → ❌ Build fails  → Merge blocked
```

## 🔧 For Developers

### ✅ Recommended Development Setup

**Option 1: Environment Variables (Recommended)**
```python
# In settings.py:
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# For local development, set environment variable:
# Windows: set DEBUG=True
# Unix/Mac: export DEBUG=True
```

**Option 2: Local Settings File**
```python
# Create local_settings.py (already in .gitignore):
DEBUG = True
# Any other local overrides...

# In settings.py, add at the end:
try:
    from .local_settings import *
except ImportError:
    pass
```

**Option 3: Multiple Settings Files**
```bash
# Create settings/development.py, settings/production.py
# Run with: python manage.py runserver --settings=myproject.settings.development
```

### 🚨 What Happens When DEBUG=True is Detected

**Pre-commit Hook Output:**
```
❌ ERROR: DEBUG=True found in coreflowepc/settings.py
🚫 COMMIT REJECTED!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   DEBUG mode is enabled in your Django settings.
   This is a security risk and should not be committed to version control.

🔧 To fix this:
   1. Set DEBUG = False in your settings.py file(s)
   2. Use environment variables for DEBUG in production
```

**GitHub Actions Output:**
```
🚫 SECURITY VIOLATION DETECTED!
❌ DEBUG=True detected in Django settings
❌ This is a critical security vulnerability
❌ Deployment blocked until resolved
```

## 🛠️ Manual Operations

### Check Current DEBUG Status:
```bash
python scripts/check_debug.py
```

### Force Check with Error Exit:
```bash
python scripts/check_debug.py --strict
```

### Check Specific File:
```bash
python scripts/check_debug.py --path coreflowepc/settings.py
```

### Emergency Bypass (NOT RECOMMENDED):
```bash
# Skip pre-commit hook (GitHub Actions will still block):
git commit --no-verify -m "emergency commit"
```

## 📁 Files Created/Modified

### New Security Files:
- `.git/hooks/pre-commit` - Unix/Linux/Mac pre-commit hook
- `.git/hooks/pre-commit.bat` - Windows pre-commit hook
- `scripts/check_debug.py` - Python DEBUG checker script
- `.github/workflows/debug-check.yml` - GitHub Actions workflow
- `security-config.ini` - Security configuration documentation

### Modified Files:
- `.gitignore` - Added local development files to ignore list

## 🎯 Security Benefits

1. **Prevents Production Vulnerabilities**: Stops `DEBUG=True` from reaching production
2. **Multiple Failure Points**: Even if one protection fails, others catch it
3. **Developer Education**: Clear error messages teach secure practices
4. **Automation**: No manual checking required
5. **Flexibility**: Multiple ways to enable DEBUG locally without committing it

## 🔍 How to Test the Protection

### Test Pre-commit Hook:
1. Temporarily change `DEBUG = False` to `DEBUG = True` in settings.py
2. Try to commit: `git add . && git commit -m "test"`
3. Should be blocked with security message
4. Change back to `DEBUG = False` and commit should work

### Test GitHub Actions:
1. Push a branch with `DEBUG = True` 
2. Check Actions tab in GitHub
3. Should see failed "Security Check" workflow

## 📞 Support

If you encounter issues with the security system:

1. **Check Current Status**: `python scripts/check_debug.py`
2. **Verify Settings**: Ensure `DEBUG = False` in all settings files
3. **Check Permissions**: Ensure pre-commit hook is executable
4. **Review Configuration**: Check `security-config.ini` for guidance

---

**⚠️ IMPORTANT**: These security measures are designed to protect your application. Do not bypass them unless you fully understand the security implications of deploying with `DEBUG=True` enabled.
