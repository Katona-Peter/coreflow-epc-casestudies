# CoreFlow EPC Case Studies

A Django web application for showcasing CoreFlow EPC case studies. This project allows users to browse case studies with detailed information about clients, locations, industries of CoreFlow EPC projects, and visual documentation through image uploads.

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

#### Industrial Color Palette

The application employs a carefully selected industrial color palette that reflects CoreFlow EPC's professional character and expertise in the process industry.

![Industrial Color Palette](staticfiles/images/industrial.colors.png)

**Color Philosophy**
Our color scheme draws inspiration from industrial environments, manufacturing facilities, and energy infrastructure. These colors communicate reliability, technical expertise, and industrial strength - core values that define CoreFlow EPC's approach to energy performance consulting.

**Primary Colors**
- **Steel Blue (#4A90A4)**: Represents technical precision and reliability
- **Industrial Gray (#6C7B7F)**: Conveys professional expertise and stability  
- **Charcoal (#2C3E50)**: Provides strong contrast and industrial strength
- **Slate (#34495E)**: Adds depth while maintaining professional appearance

**Accent Colors**
- **Safety Orange (#E67E22)**: Highlights important information and calls-to-action
- **Steel Silver (#BDC3C7)**: Used for subtle borders and secondary elements
- **Deep Navy (#1B2631)**: Provides maximum contrast for critical text elements

**Design Rationale**
This industrial-inspired palette creates a visual connection to the manufacturing and energy sectors that CoreFlow EPC serves. The combination of cool blues and grays with warm orange accents creates a professional yet approachable aesthetic that builds trust with clients while emphasizing technical competence.

The colors work harmoniously to:
- **Establish Authority**: Deep blues and grays convey expertise and professionalism
- **Ensure Clarity**: High contrast ratios guarantee excellent readability
- **Guide Attention**: Strategic use of orange guides users to important actions
- **Reflect Industry**: Colors echo the industrial environments where CoreFlow EPC assessments take place

## UX Design Improvements

### Advanced Visual Design Implementation

During the development process, we implemented sophisticated visual design solutions that significantly enhanced the user experience. The case study detail page showcases an innovative approach to visual storytelling through creative use of background imagery.

#### Key Design Elements

**Full Background Image Coverage**
- The case study image serves as both a focal point and atmospheric background
- Dynamic background sizing ensures complete card coverage across all device sizes
- Seamless integration between content and visual elements

**Semi-transparent Overlay for Readability**
- Strategic use of `rgba(255, 255, 255, 0.9)` overlay ensures perfect text readability
- Maintains visual impact while preserving content accessibility
- Creates depth and layering in the design hierarchy

**Fixed Background Attachment for Parallax Effect**
- Subtle parallax scrolling creates a modern, engaging user experience
- Adds depth and sophistication to the page interaction
- Enhances the immersive quality of each case study

**Rounded Corners and Proper Spacing**
- Consistent 8px border-radius creates a polished, professional appearance
- Thoughtful padding (20px) ensures comfortable content consumption
- Visual harmony between overlay and content elements

#### Design Philosophy

The best results come from experimenting with creative design solutions. The way the case study image now serves as both the focal point AND the atmospheric background really elevates the entire page aesthetic. It makes each case study feel unique and immersive while maintaining perfect readability.

This approach transforms a simple detail page into something that feels modern and engaging, creating a sophisticated and immersive visual experience that sets the application apart from conventional layouts.

#### Technical Implementation

```css
/* Background image with full coverage */
background-image: url('image.jpg');
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;

/* Semi-transparent overlay */
background-color: rgba(255, 255, 255, 0.9);
padding: 20px;
border-radius: 8px;
```

This innovative design approach demonstrates how creative technical solutions can significantly enhance user experience and visual appeal.

## Agile Project Management

### Development Methodology

This project was developed using Agile methodology principles, emphasizing iterative development, continuous improvement, and flexible response to changing requirements. The development process focused on delivering working software incrementally while maintaining high code quality and user experience standards.

**📋 Project Management**: View the complete sprint planning and task management on our [Sprint Board](https://github.com/users/Katona-Peter/projects/10)

#### Project Planning and User Stories

**Epic: Case Study Management System**
- As a site administrator, I want to manage case studies so that I can showcase our EPC projects effectively
- As a visitor, I want to browse case studies so that I can learn about EPC implementations
- As a registered user, I want to comment on case studies so that I can engage with the content

**Epic: User Authentication and Interaction**
- As a new user, I want to register an account so that I can participate in discussions
- As a returning user, I want to log in securely so that I can access my account features
- As a user, I want my comments to be moderated so that the platform maintains quality content

**Epic: Visual Design and User Experience**
- As a user, I want an intuitive interface so that I can easily navigate the application
- As a mobile user, I want a responsive design so that I can access content on any device
- As a visitor, I want engaging visuals so that the content is appealing and professional

#### Sprint Planning and Execution

**Sprint 1: Foundation and Core Functionality**
- Project initialization and Django setup
- Basic model creation (Casestudy, Client, Location, Industry)
- Initial admin interface configuration
- Basic template structure
- Case study listing and detail views
- Image upload system implementation
- URL routing and navigation
- Basic styling and responsive design

**Sprint 2: User Features and Authentication**
- User authentication system integration
- Comment system implementation with approval workflow
- User registration and login functionality
- Security enhancements
- Advanced UI/UX improvements
- Background image implementation
- Icon integration and styling

**Sprint 3: Visual Enhancement and Deployment**
- Visual hierarchy optimization
- Parallax effects and modern design elements
- Comprehensive testing implementation
- Bug fixes and performance optimization
- Heroku deployment configuration
- Documentation completion

#### Agile Practices Implemented

**Daily Development Reviews**
- Regular code review and refactoring sessions
- Continuous integration of new features
- Immediate bug fixing and issue resolution

**Iterative Design Process**
- Continuous UI/UX improvements based on visual feedback
- Responsive design testing across multiple devices
- User experience optimization through iterative refinement

**Flexible Requirements Management**
- Adaptive approach to feature implementation
- Prioritization based on user value and technical feasibility
- Regular reassessment of project goals and timelines

**Documentation and Knowledge Sharing**
- Comprehensive README documentation
- Inline code documentation and comments
- Technical decision documentation for future reference

#### Tools and Workflow

**Version Control**
- Git with feature branch workflow
- Regular commits with descriptive messages
- Pull request reviews for code quality assurance

**Development Environment**
- Local development with Django development server
- Environment variable management for configuration flexibility
- Database migrations for schema management

**Testing Strategy**
- Unit tests for models and forms
- Integration tests for views and user workflows
- Manual testing for UI/UX validation

**Deployment Pipeline**
- Continuous deployment to Heroku
- Environment-specific configuration management
- Production monitoring and maintenance

#### Lessons Learned

**Technical Growth**
- Advanced Django feature implementation
- Complex CSS and JavaScript integration
- Database design and optimization techniques

**Design Evolution**
- Importance of iterative design improvement
- User feedback integration in development process
- Balance between functionality and aesthetic appeal

**Project Management**
- Effective time management through sprint planning
- Priority-based feature development
- Documentation importance for project sustainability

This Agile approach enabled the delivery of a comprehensive, user-friendly web application while maintaining code quality and incorporating continuous improvements throughout the development process.

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

### Entity Relationship Diagram

![Database ERD](static/images/erd-diagram.png)

The database schema consists of four main entities with clear relationships designed to support comprehensive case study management and user interaction:

**Core Relationships:**
- **Case Studies** are linked to **Clients**, **Locations**, and **Industries** through foreign key relationships
- **Comments** are associated with specific **Case Studies** and **Users** for structured feedback management
- **Users** can create multiple **Comments** across different **Case Studies**
- Each **Case Study** belongs to exactly one **Client**, **Location**, and **Industry** for clear categorization

**Design Principles:**
- Normalized structure to eliminate data redundancy
- Clear foreign key constraints to maintain referential integrity
- Scalable architecture supporting future feature expansion
- User-centric design enabling authenticated interactions

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

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) folder:

- **[Environment Setup Guide](docs/ENVIRONMENT_SETUP.md)** - Complete setup instructions
- **[Deployment Guide](docs/HEROKU_DEPLOYMENT.md)** - Heroku deployment walkthrough  
- **[Security Guidelines](docs/SECURITY_README.md)** - Security best practices
- **[Media Management](docs/MEDIA_CLEANUP_SUMMARY.md)** - File upload and management
- **[Comment System Guide](docs/CREATE_COMMENTS_INSTRUCTIONS.md)** - Comment implementation details

For a complete documentation index, see [`docs/README.md`](docs/README.md).

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

## Deployment

### 🚀 **Live Application**
- **Production URL**: [https://coreflow-epc-casestudies-faf59a0d5c41.herokuapp.com/](https://coreflow-epc-casestudies-faf59a0d5c41.herokuapp.com/)
- **Platform**: Heroku
- **Environment**: Django with WhiteNoise for static files

### 📋 **Deployment Options**

#### **Heroku Deployment (Recommended)**
This Django application is designed for deployment on Heroku:

```bash
# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

#### **GitHub Pages Note**
⚠️ **Important**: This repository contains a Django web application that **cannot be deployed on GitHub Pages** as it requires a Python server environment. GitHub Pages only supports static HTML/CSS/JavaScript sites.

- The `index.html` file in the root is provided for GitHub Pages compatibility only
- It redirects visitors to the live Heroku deployment
- For the actual application, visit the Heroku URL above

### 🔧 **Deployment Configuration**
- **DEBUG**: Set to `False` for production
- **Static Files**: Managed by WhiteNoise
- **Database**: PostgreSQL on Heroku
- **Security**: Environment variables for sensitive data

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
