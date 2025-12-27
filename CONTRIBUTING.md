# Contributing to Campus Connect

First off, thank you for considering contributing to Campus Connect! It's people like you that make Campus Connect such a great tool for academic communities.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

---

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

---

## How Can I Contribute?

### 1. Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

**Template:**
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 11]
 - Browser [e.g. chrome, safari]
 - Python Version [e.g. 3.13]
 - Django Version [e.g. 5.0.6]

**Additional context**
Add any other context about the problem here.
```

### 2. Suggesting Features

Feature suggestions are welcome! Please provide:

- Clear description of the feature
- Why it would be useful
- How it should work (if you have ideas)
- Any examples from other platforms

### 3. Code Contributions

- Fix bugs
- Implement new features
- Improve documentation
- Write tests
- Refactor code

---

## Development Setup

### Prerequisites
- Python 3.10+
- Git
- Virtual environment tool

### Setup Steps

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/campus-connect.git
   cd campus-connect
   ```

3. **Add upstream remote**
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/campus-connect.git
   ```

4. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

7. **Run migrations**
   ```bash
   python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Run development server**
   ```bash
   python manage.py runserver
   ```

---

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

**Key Points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Type hints are encouraged

**Example:**
```python
def create_notification(
    recipient: User, 
    sender: User, 
    notification_type: str, 
    title: str, 
    message: str, 
    link: str = None
) -> Notification:
    """
    Create a new notification for a user.
    
    Args:
        recipient: User who will receive the notification
        sender: User who triggered the notification
        notification_type: Type of notification (post, event, etc.)
        title: Notification title
        message: Notification message content
        link: Optional URL to redirect to
        
    Returns:
        Notification: The created notification object
    """
    return Notification.objects.create(
        recipient=recipient,
        sender=sender,
        notification_type=notification_type,
        title=title,
        message=message,
        link=link
    )
```

### Django Best Practices

1. **Models**
   - Use explicit `related_name` for foreign keys
   - Add `__str__` methods
   - Include `Meta` class for ordering and indexes
   - Use `verbose_name` and `help_text`

2. **Views**
   - Keep views thin, business logic in models/services
   - Use class-based views where appropriate
   - Always use `@login_required` for protected views
   - Handle exceptions properly

3. **Templates**
   - Use template inheritance
   - Avoid logic in templates
   - Use template tags for reusable components
   - Keep templates DRY (Don't Repeat Yourself)

4. **URLs**
   - Use meaningful URL names
   - Keep URL patterns RESTful
   - Use namespaces for app URLs

### JavaScript & CSS

- Use ES6+ syntax
- Add comments for complex logic
- Keep functions small and focused
- Use meaningful variable names
- Format with Prettier (if available)

### Testing

- Write tests for new features
- Maintain test coverage above 80%
- Use descriptive test names
- Test edge cases

**Example:**
```python
from django.test import TestCase
from django.contrib.auth.models import User
from notifications.models import Notification

class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_create_notification(self):
        """Test creating a notification"""
        notification = Notification.objects.create(
            recipient=self.user,
            notification_type='post',
            title='Test Notification',
            message='This is a test'
        )
        self.assertEqual(notification.recipient, self.user)
        self.assertFalse(notification.is_read)
```

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(notifications): add email notification support

Implemented email notifications for important events.
Users can now receive emails when they get mentions.

Closes #123
```

```bash
fix(blog): resolve pagination issue on mobile

Fixed pagination not working correctly on mobile devices
due to CSS overflow issues.

Fixes #456
```

### Commit Best Practices

- Write clear, concise commit messages
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests
- Make atomic commits (one logical change per commit)

---

## Pull Request Process

### Before Submitting

1. **Update your fork**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write code
   - Add tests
   - Update documentation

4. **Test your changes**
   ```bash
   python manage.py test
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add awesome feature"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

### Creating the Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill in the PR template:

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests that you ran to verify your changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Related Issues
Closes #(issue number)
```

### After Submission

- Be responsive to feedback
- Make requested changes promptly
- Keep your PR up to date with main branch
- Be patient - reviews take time

---

## Branch Strategy

We use a simplified Git Flow:

### Main Branches
- **main**: Production-ready code
- **dev**: Development branch (integration)

### Supporting Branches
- **feature/***: New features
- **bugfix/***: Bug fixes
- **hotfix/***: Urgent fixes for production
- **release/***: Release preparation

### Example Workflow

```bash
# Start new feature
git checkout dev
git pull origin dev
git checkout -b feature/user-profile-enhancement

# Work on feature
git add .
git commit -m "feat(users): add bio field to profile"

# Keep feature branch updated
git checkout dev
git pull origin dev
git checkout feature/user-profile-enhancement
git merge dev

# Push and create PR
git push origin feature/user-profile-enhancement
# Create PR on GitHub: feature/user-profile-enhancement -> dev
```

---

## Review Process

### For Reviewers

- Be constructive and respectful
- Explain the reasoning behind suggestions
- Approve when requirements are met
- Use GitHub's review features

### For Contributors

- Don't take criticism personally
- Ask for clarification if needed
- Make requested changes
- Thank reviewers for their time

---

## Questions?

Feel free to:
- Open an issue for questions
- Join our discussions
- Reach out to maintainers

---

## Recognition

Contributors will be added to:
- README.md contributors section
- GitHub contributors page
- Release notes (for significant contributions)

---

## Thank You!

Your contributions to open source make projects like this possible. Thank you for taking the time to contribute!

---

**Happy Coding!** 🎉
