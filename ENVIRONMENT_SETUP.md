# Environment Setup Guide

## 🔧 Local Development Environment

### Prerequisites
- Python 3.12+
- Git
- Django 4.2.23

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd coreflow-epc-casestudies
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Setup**
   ```bash
   # Copy the template file
   cp env.py.template env.py
   
   # Edit env.py with your local settings:
   # - Set your database URL
   # - Set your secret key
   # - Set DEBUG = "True" for local development only
   ```

### Important Security Notes

⚠️ **NEVER commit `env.py` to the repository!**

- The `env.py` file is already in `.gitignore`
- It contains sensitive information (database URLs, secret keys)
- For production deployment, use environment variables instead

### Local Development

For local development, you can set `DEBUG = "True"` in your `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "your-local-database-url")
os.environ.setdefault("SECRET_KEY", "your-local-secret-key")
os.environ.setdefault("DEBUG", "True")  # OK for local development
```

### Production Deployment

For production (Heroku, etc.), ensure:
- `DEBUG = False` is set in `settings.py` (already configured)
- Use platform environment variables for sensitive data
- Never commit sensitive information to the repository

## 🚀 Running the Application

1. **Run migrations**
   ```bash
   python manage.py migrate
   ```

2. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

3. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 🔒 Security Compliance

This project includes GitHub Actions workflows that:
- Check for `DEBUG = True` in committed code
- Ensure production safety
- Block deployment if security issues are found

The security check will fail if:
- `DEBUG = True` is found in any committed `.py` file
- Sensitive environment files are committed
- Production security settings are misconfigured

## 📁 File Structure

```
├── env.py.template     # Template for local environment setup
├── env.py             # Local only - DO NOT COMMIT
├── coreflowepc/
│   └── settings.py    # Main Django settings (DEBUG = False)
└── .github/
    └── workflows/
        └── debug-check.yml  # Security validation workflow
```

## 🐛 Troubleshooting

### GitHub Actions Failing
If GitHub Actions show security check failures:
1. Ensure no `DEBUG = True` exists in committed files
2. Check that `env.py` is not committed
3. Verify `.gitignore` includes `env.py`

### Local Development Issues
If the application doesn't work locally:
1. Check your `env.py` file exists and has correct settings
2. Ensure virtual environment is activated
3. Run `python manage.py check` to validate configuration

## 📞 Support

For issues with environment setup:
1. Check this guide first
2. Verify all steps were followed correctly
3. Check GitHub Actions logs for specific error messages

## 🔄 Last Updated
- Environment setup validation: August 4, 2025
- GitHub Actions workflow: Tested and functional
