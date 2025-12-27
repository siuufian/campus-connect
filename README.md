# 🎓 Campus Connect

**Campus Connect** is a comprehensive web platform designed for university students and faculty to share blog posts, organize events, and stay connected through real-time notifications. Built with Django, this project provides a modern, responsive, and feature-rich social networking experience tailored for academic communities.

[![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

### 🌟 Core Features
- **User Authentication & Authorization**
  - User registration and login
  - Password reset via email
  - Profile management with avatars
  - Role-based access control (Admin, User)

- **Blog System**
  - Create, read, update, delete (CRUD) blog posts
  - Rich text editor with CKEditor 5
  - Post categorization and tagging
  - Like functionality for posts
  - User-specific post listings
  - Responsive blog cards with animations

- **Event Management**
  - Create and manage campus events
  - Event registration system
  - Track registered participants
  - Attendance tracking
  - Event calendar integration
  - User event dashboard (organized & registered events)

- **Notifications System** 🔔
  - Real-time notification bell in navbar
  - Automatic notifications for:
    - New blog posts
    - Event registrations
    - Comments (infrastructure ready)
    - Likes (infrastructure ready)
  - AJAX-powered mark as read
  - Notification history with pagination
  - Badge count with pulse animation
  - Context-aware notification types

### 🎨 User Experience
- **Modern UI/UX**
  - Bootstrap 5 responsive design
  - Particle.js animated backgrounds
  - AOS (Animate On Scroll) effects
  - Font Awesome icons
  - Gradient color schemes
  - Mobile-friendly interface

- **Interactive Features**
  - FullCalendar integration
  - AJAX operations for smooth UX
  - Scroll-to-top button
  - Image preview on upload
  - Dynamic content loading

### 🔐 Security
- CSRF protection
- Password hashing with Django's built-in system
- SQL injection prevention via ORM
- XSS protection
- Secure session management
- Environment-based configuration

---

## 📸 Screenshots

> Add screenshots of your application here

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 5.0.6
- **Language:** Python 3.13
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **ORM:** Django ORM

### Frontend
- **HTML5, CSS3, JavaScript**
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Icon library
- **Particle.js** - Interactive backgrounds
- **AOS** - Scroll animations
- **FullCalendar** - Event calendar
- **CKEditor 5** - Rich text editor

### Key Libraries
- `django-crispy-forms` - Form styling
- `django-ckeditor-5` - Rich text editing
- `python-decouple` - Environment variable management
- `Pillow` - Image processing
- `djangorestframework` - API support

---

## 📁 Project Structure

```
campus-connect/
├── blog/                      # Blog application
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   ├── static/
│   ├── models.py             # Post model
│   ├── views.py              # Blog views
│   ├── urls.py               # Blog URLs
│   └── forms.py              # Blog forms
│
├── events/                    # Events application
│   ├── migrations/
│   ├── templates/
│   │   └── events/
│   ├── models.py             # Event, EventParticipant models
│   ├── views.py              # Event views
│   └── urls.py               # Event URLs
│
├── notifications/             # Notifications system
│   ├── migrations/
│   ├── templates/
│   ├── templatetags/         # Custom template tags
│   ├── management/           # Management commands
│   ├── models.py             # Notification model
│   ├── views.py              # Notification views
│   ├── signals.py            # Auto-notification triggers
│   └── context_processors.py # Global unread count
│
├── users/                     # User management
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   ├── models.py             # Profile model
│   ├── views.py              # User views
│   ├── forms.py              # User forms
│   └── signals.py            # Profile creation
│
├── proj2/                     # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI config
│
├── media/                     # User uploads
│   ├── profile_pics/         # Profile pictures
│   └── default.jpg           # Default avatar
│
├── static/                    # Static files
│   └── blog/
│       └── main.css          # Custom styles
│
├── manage.py                  # Django management
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
├── .env.example              # Environment variables template
└── README.md                 # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/campus-connect.git
cd campus-connect
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the root directory:
```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` with your settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_USER=your-email@gmail.com
EMAIL_USER_PASS=your-app-password
```

### Step 5: Database Setup
```bash
# Create migrations for all apps
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Django Settings
SECRET_KEY=your-django-secret-key
DEBUG=True

# Email Configuration (for password reset)
EMAIL_USER=your-email@gmail.com
EMAIL_USER_PASS=your-gmail-app-password

# Database (optional, for production)
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Gmail Setup for Email Notifications

1. Enable 2-Factor Authentication in your Google Account
2. Generate an App Password:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the generated password
3. Add to `.env`:
   ```env
   EMAIL_USER=your-email@gmail.com
   EMAIL_USER_PASS=generated-app-password
   ```

---

## 📖 Usage

### For Users

#### Registration & Login
1. Navigate to the homepage
2. Click "Register" to create an account
3. Fill in username, email, and password
4. Login with your credentials

#### Creating Blog Posts
1. Login to your account
2. Click "Add" → "Blog" in the navbar
3. Write your post using the rich text editor
4. Submit to publish

#### Managing Events
1. Click "Add" → "Event" in the navbar
2. Fill in event details (name, description, date)
3. Submit to create the event
4. Users can register for events from the event detail page

#### Notifications
1. Look for the bell icon (🔔) in the navbar
2. Badge shows unread notification count
3. Click to view all notifications
4. Mark as read or delete notifications

### For Administrators

#### Admin Panel
Access at: `http://127.0.0.1:8000/admin/`

Features:
- Manage users, posts, events, notifications
- View site statistics
- Moderate content
- Manage user permissions

---

## 🔌 API Endpoints

### Notifications API (AJAX)
```
GET  /notifications/                    # List all notifications
POST /notifications/mark-read/<id>/    # Mark as read
POST /notifications/mark-all-read/     # Mark all as read
GET  /notifications/unread-count/      # Get unread count
GET  /notifications/recent/            # Get recent notifications
```

### Blog API
```
GET  /                                  # List all posts
GET  /post/<id>/                       # Post detail
POST /post/new/                        # Create post (auth required)
PUT  /post/<id>/update/                # Update post (auth required)
DEL  /post/<id>/delete/                # Delete post (auth required)
GET  /user/<username>/                 # User's posts
```

### Events API
```
GET  /events/                          # List all events
GET  /events/<id>/                     # Event detail
POST /events/new/                      # Create event (auth required)
POST /events/<id>/register/            # Register for event
GET  /events/user/<username>/          # User's events
```

---

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test notifications
python manage.py test blog
python manage.py test events
```

### Create Test Notifications
```bash
python manage.py create_test_notifications --username=admin --count=10
```

### Cleanup Old Notifications
```bash
python manage.py cleanup_notifications --days=30
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

### 1. Fork the Repository
Click the "Fork" button at the top right of this page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/campus-connect.git
cd campus-connect
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Changes
- Write clean, documented code
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed

### 5. Commit Changes
```bash
git add .
git commit -m "Add: your feature description"
```

### 6. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request
Go to the original repository and click "New Pull Request"

### Coding Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write unit tests for new features
- Keep commits atomic and well-described

---

## 📋 Development Roadmap

### Completed ✅
- [x] User authentication system
- [x] Blog post CRUD operations
- [x] Event management system
- [x] Notifications system with real-time updates
- [x] Rich text editor integration
- [x] Calendar integration
- [x] Profile management
- [x] Responsive UI with animations

### In Progress 🚧
- [ ] Comment system for blog posts
- [ ] Like notifications
- [ ] Search functionality
- [ ] Post categories and tags
- [ ] Advanced filtering options

### Planned 📅
- [ ] Real-time chat system
- [ ] File sharing
- [ ] Groups and communities
- [ ] Email notifications
- [ ] Mobile app (React Native)
- [ ] RESTful API with DRF
- [ ] GraphQL support
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Performance optimization

---

## 🐛 Known Issues

- None currently reported

To report a bug, please create an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/YOUR_USERNAME)

See also the list of [contributors](https://github.com/YOUR_USERNAME/campus-connect/contributors) who participated in this project.

---

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the UI framework
- All contributors who helped improve this project
- IIUC (International Islamic University Chittagong) for inspiration

---

## 📞 Contact

**Project Link:** [https://github.com/YOUR_USERNAME/campus-connect](https://github.com/YOUR_USERNAME/campus-connect)

**Email:** your.email@example.com

**LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

## 📚 Additional Documentation

For more detailed documentation, see:
- [Notifications System](notifications/README.md)
- [Testing Guide](notifications/TESTING.md)
- [Architecture Overview](notifications/ARCHITECTURE.md)
- [Migration Guide](notifications/MIGRATION_GUIDE.md)

---

**Made with ❤️ for the Campus Community**

---

## 📸 Demo

> Add a link to your live demo here (if deployed)

**Live Demo:** [Coming Soon]

---

## 🔒 Security

If you discover a security vulnerability, please email security@example.com instead of creating a public issue.

---

*Last Updated: December 27, 2024*
