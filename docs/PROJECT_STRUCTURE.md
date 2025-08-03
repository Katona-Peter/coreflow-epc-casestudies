# 📁 CoreFlow EPC Case Studies - Project Structure

## 🏗️ Directory Structure

```
coreflow-epc-casestudies/
├── 📁 casestudy/                 # Main Django app
│   ├── 📄 models.py              # Database models (Client, Location, Industry, Casestudy, Comment)
│   ├── 📄 views.py               # View functions for case studies and comments
│   ├── 📄 urls.py                # URL routing for the app
│   ├── 📄 admin.py               # Django admin configuration
│   ├── 📄 forms.py               # Django forms (CommentForm)
│   ├── 📁 templates/             # HTML templates
│   │   └── 📁 casestudy/
│   │       ├── 📄 index.html     # Case studies listing page
│   │       ├── 📄 casestudy_detail.html  # Individual case study page
│   │       └── 📄 casestudy_list.html    # Alternative listing view
│   └── 📁 migrations/            # Database migration files
│
├── 📁 coreflowepc/              # Django project configuration
│   ├── 📄 settings.py           # Project settings
│   ├── 📄 urls.py               # Main URL routing
│   ├── 📄 wsgi.py               # WSGI configuration
│   └── 📄 asgi.py               # ASGI configuration
│
├── 📁 templates/                # Global templates
│   ├── 📄 base.html             # Base template
│   ├── 📄 index.html            # Home page
│   └── 📁 includes/             # Reusable template components
│       └── 📄 messages_help.html # Messages modal component
│
├── 📁 static/                   # Static files
│   ├── 📁 css/
│   │   └── 📄 style.css         # Main stylesheet
│   ├── 📁 images/               # Images
│   └── 📁 js/                   # JavaScript files
│
├── 📁 scripts/                  # Security and utility scripts
│   └── 📄 check_debug.py        # DEBUG security checker
│
├── 📁 .github/                  # GitHub Actions and workflows
│   └── 📁 workflows/
│       └── 📄 debug-check.yml   # CI/CD security workflow
│
├── 📁 .git/                     # Git repository
│   └── 📁 hooks/                # Git hooks for security
│       ├── 📄 pre-commit        # Unix/Linux pre-commit hook
│       └── 📄 pre-commit.bat    # Windows pre-commit hook
│
├── 📄 manage.py                 # Django management script
├── 📄 requirements.txt          # Python dependencies
├── 📄 Procfile                  # Heroku deployment configuration
├── 📄 README.md                 # Project documentation
├── 📄 SECURITY_README.md        # Security documentation
├── 📄 .gitignore               # Git ignore rules
├── 📄 .python-version          # Python version specification
└── 📄 env.py                   # Environment variables (gitignored)
```

## 🎯 Key Features

### 📊 Case Studies Management
- **Models**: Client, Location, Industry, Casestudy, Comment
- **Views**: List view, detail view, comment management
- **Templates**: Responsive design with Bootstrap 5

### 💬 Comment System
- **User Authentication**: Required for commenting
- **Moderation**: Admin approval system
- **CRUD Operations**: Create, read, update, delete comments
- **Real-time Editing**: JavaScript-powered inline editing

### 🔒 Security Features
- **Multi-layer DEBUG Protection**: Pre-commit hooks, GitHub Actions, Python scripts
- **Authentication**: Django's built-in user system
- **CSRF Protection**: All forms protected
- **XSS Prevention**: Template escaping and safe filters

### 🎨 Frontend
- **Bootstrap 5**: Responsive CSS framework
- **Font Awesome**: Icon library
- **Custom CSS**: Professional styling and animations
- **JavaScript**: Interactive comment editing and deletion

### 🚀 Deployment Ready
- **Heroku**: Procfile and configuration
- **Static Files**: Whitenoise configuration
- **Database**: PostgreSQL support via dj-database-url
- **Environment Variables**: Secure configuration management

## 🛠️ Technologies Used

- **Backend**: Django 4.2.23, Python 3.12
- **Frontend**: Bootstrap 5.0.1, Font Awesome, Vanilla JavaScript
- **Database**: PostgreSQL (production), SQLite3 (development)
- **Deployment**: Heroku, Whitenoise
- **Security**: Multi-layer protection system
- **Version Control**: Git with security hooks

## 📈 Development Workflow

1. **Local Development**: Use `DEBUG=True` in local_settings.py
2. **Version Control**: Automatic security checks prevent DEBUG=True commits
3. **CI/CD**: GitHub Actions verify security before deployment
4. **Production**: Secure deployment with DEBUG=False enforced

## 🔧 Maintenance

- **Regular Updates**: Keep dependencies updated
- **Security Monitoring**: Automated DEBUG protection
- **Code Quality**: Consistent formatting and documentation
- **Testing**: Regular functionality verification
