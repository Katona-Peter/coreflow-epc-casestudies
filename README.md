# CoreFlow EPC Case Studies

A Django web application for showcasing Energy Performance Certificate (EPC) case studies. This project allows users to browse case studies with detailed information about clients, locations, industries, and visual documentation through image uploads.

![CoreFlow EPC Case Studies](static/images/default.png)

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Models](#models)
- [Admin Interface](#admin-interface)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

### Current Features
- **Case Study Display**: Browse case studies with card-based layout
- **Image Upload System**: Upload and display images for each case study
- **Background Images**: Dynamic background images on case study cards
- **Categorization**: Organize case studies by client, location, and industry
- **Responsive Design**: Mobile-friendly Bootstrap-based UI
- **Admin Interface**: Django admin for content management
- **User Authentication**: Built-in Django authentication system
- **Comments System**: User comments on case studies (with approval workflow)
- **Search & Filter**: Filter case studies by various criteria

### Visual Features
- **Card Layout**: Split-view cards with visible images and background images
- **Custom Styling**: Blue border margins and custom border-radius effects
- **Visual Indentation**: Clean spacing for client/location/industry information
- **Responsive Grid**: Bootstrap-powered responsive grid system

## Technologies Used

### Backend
- **Django 4.2.23**: Web framework
- **Python 3.12**: Programming language
- **SQLite3**: Database (development)
- **PostgreSQL**: Database (production ready)
- **Pillow 10.4.0**: Image processing

### Frontend
- **Bootstrap 5**: CSS framework
- **HTML5**: Markup language
- **CSS3**: Styling
- **Font Awesome**: Icons
- **JavaScript**: Interactive elements

### Additional Libraries
- **django-allauth**: Authentication
- **django-crispy-forms**: Form rendering
- **django-summernote**: Rich text editor
- **whitenoise**: Static file serving
- **gunicorn**: WSGI server

## Project Structure

```
coreflow-epc-casestudies/
├── casestudy/
│   ├── migrations/
│   ├── templates/
│   │   └── casestudy/
│   │       ├── index.html
│   │       └── casestudy_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── coreflowepc/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/
│   └── base.html
├── requirements.txt
├── manage.py
└── README.md
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Katona-Peter/coreflow-epc-casestudies.git
   cd coreflow-epc-casestudies
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create an `env.py` file in the root directory:
   ```python
   import os
   
   os.environ["SECRET_KEY"] = "your-secret-key-here"
   os.environ["DEBUG"] = "True"
   os.environ["DATABASE_URL"] = "your-database-url"  # Optional for production
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000` to view the application.

## Configuration

### Environment Variables

Create an `env.py` file with the following variables:

```python
import os

# Security
os.environ["SECRET_KEY"] = "your-django-secret-key"
os.environ["DEBUG"] = "True"  # Set to "False" for production

# Database (optional - uses SQLite by default)
os.environ["DATABASE_URL"] = "postgresql://user:password@host:port/database"

# Media files (optional)
os.environ["CLOUDINARY_URL"] = "cloudinary://api_key:api_secret@cloud_name"
```

### Settings Configuration

Key settings in `settings.py`:
- **MEDIA_URL**: `/media/` for uploaded images
- **MEDIA_ROOT**: Local media file storage
- **STATIC_URL**: `/static/` for static files
- **DEBUG**: Set to `False` for production

## Usage

### Adding Case Studies

1. **Access the admin interface**: Navigate to `/admin/`
2. **Login**: Use your superuser credentials
3. **Add Case Studies**: 
   - Create clients, locations, and industries first
   - Add case studies with images and detailed descriptions
   - Images are automatically processed and saved with unique filenames

### Image Upload System

The application features an advanced image upload system:
- **Dynamic Paths**: Images are saved with case study slug as filename
- **Background Images**: Each case study card displays the uploaded image as background
- **Fallback Images**: Default images when no image is uploaded
- **Image Processing**: Automatic image optimization with Pillow

### Card Layout Features

- **Split View**: Left side shows the actual image, right side shows content
- **Background Images**: The same image appears as card background
- **Custom Border**: Unique border-radius styling (8px 0 8px 0)
- **Responsive Design**: Adapts to different screen sizes

## Models

### Casestudy Model
- `title`: Unique case study title
- `slug`: URL-friendly identifier
- `client`: Foreign key to Client model
- `location`: Foreign key to Location model
- `industry`: Foreign key to Industry model
- `description`: Detailed case study description
- `excerpt`: Short summary for card display
- `casestudyimage`: Uploaded image with dynamic path

### Supporting Models
- **Client**: Company or individual clients
- **Location**: Geographic locations for projects
- **Industry**: Business sectors/industries
- **Comment**: User comments with approval system

## Admin Interface

The Django admin interface provides:
- **Case Study Management**: Add, edit, delete case studies
- **Image Upload**: Direct image upload with preview
- **Category Management**: Manage clients, locations, industries
- **Comment Moderation**: Approve/reject user comments
- **User Management**: Handle user accounts and permissions

## Deployment

### Heroku Deployment

1. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

2. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

4. **Run migrations**
   ```bash
   heroku run python manage.py migrate
   ```

### Production Considerations

- Set `DEBUG=False` in production
- Use PostgreSQL for production database
- Configure static file serving with WhiteNoise
- Set up proper media file handling (Cloudinary recommended)
- Use environment variables for sensitive settings

## API Endpoints

- `/`: Home page with case study listing
- `/casestudy/<slug>/`: Individual case study detail
- `/admin/`: Django administration interface

## Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -am 'Add new feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/new-feature
   ```
6. **Create a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Ensure responsive design compatibility

## Future Enhancements

- [ ] Advanced search and filtering
- [ ] Case study categories and tags
- [ ] PDF export functionality
- [ ] Email notifications for comments
- [ ] REST API development
- [ ] Multi-language support
- [ ] Performance analytics dashboard
- [ ] Social media integration

## Troubleshooting

### Common Issues

1. **Image Upload Problems**
   - Ensure Pillow is installed: `pip install Pillow`
   - Check MEDIA_URL and MEDIA_ROOT settings
   - Verify file permissions

2. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATIC_ROOT settings
   - Ensure DEBUG settings for development

3. **Database Migration Issues**
   - Delete migration files and regenerate: `python manage.py makemigrations`
   - Reset database if needed: `python manage.py flush`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

**Developer**: Peter Katona  
**Repository**: [GitHub Repository](https://github.com/Katona-Peter/coreflow-epc-casestudies)  
**Issues**: [Report Issues](https://github.com/Katona-Peter/coreflow-epc-casestudies/issues)

---

*This project was developed as part of a Code Institute course, demonstrating Django web development skills with a focus on image handling, responsive design, and content management.*
