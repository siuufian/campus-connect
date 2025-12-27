# 🚀 GitHub Push Guide for Campus Connect

This guide will help you safely push your Campus Connect project to GitHub.

---

## 📋 Pre-Push Checklist

Before pushing to GitHub, verify:

- ✅ `.gitignore` is configured (prevents sensitive files)
- ✅ `.env` file exists but is NOT tracked by git
- ✅ `requirements.txt` is up to date
- ✅ `README.md` is complete
- ✅ All migrations are created and applied locally
- ✅ Project runs without errors locally
- ✅ Sensitive data removed from code

---

## 🔒 Security Check

### CRITICAL: Ensure These Files Are NOT Committed

```bash
# Check what will be committed
git status

# These should NOT appear in git status:
# ❌ .env
# ❌ control.env
# ❌ db.sqlite3
# ❌ venv/
# ❌ __pycache__/
# ❌ *.pyc
# ❌ media/ (user uploads)
```

If any appear, they're already in `.gitignore`. Just don't force-add them!

---

## 🌿 Branch Strategy

We recommend a **three-tier branch strategy**:

```
main (production)
  ↑
dev (development/staging)
  ↑
feature/* (individual features)
```

### Branch Purposes

1. **main** - Production-ready code
   - Only merge from `dev` after testing
   - Protected branch (require PR reviews)
   - Tagged releases

2. **dev** - Development/integration branch
   - Active development happens here
   - Merge feature branches here first
   - Test before merging to `main`

3. **feature/** - Individual features
   - Branch from `dev`
   - Naming: `feature/feature-name`
   - Examples:
     - `feature/notifications-system`
     - `feature/comment-system`
     - `feature/user-profiles`

4. **bugfix/** - Bug fixes
   - Branch from `dev`
   - Naming: `bugfix/issue-description`
   - Example: `bugfix/login-redirect`

5. **hotfix/** - Urgent production fixes
   - Branch from `main`
   - Naming: `hotfix/critical-issue`
   - Merge back to both `main` and `dev`

---

## 🚀 First-Time Push (Initial Setup)

### Step 1: Verify Git is Initialized

```bash
# Navigate to project directory
cd C:\Users\abusu\Downloads\Diagram\campus-connect-main

# Check if git is initialized
git status
```

If you see "not a git repository":
```bash
git init
```

### Step 2: Review What Will Be Committed

```bash
# See which files will be tracked
git status

# See the actual changes
git diff
```

**⚠️ IMPORTANT:** If you see `.env`, `db.sqlite3`, or `venv/`, DO NOT PROCEED!
Check your `.gitignore` file.

### Step 3: Add Files to Staging

```bash
# Add all files (gitignore will exclude sensitive files)
git add .

# Or add specific files
git add README.md .gitignore requirements.txt
git add blog/ events/ notifications/ users/ proj2/
git add manage.py
```

### Step 4: Commit Changes

```bash
git commit -m "Initial commit: Campus Connect project with notifications system"
```

### Step 5: Connect to GitHub Repository

Replace `YOUR_USERNAME` with your GitHub username:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/campus-connect.git

# Verify remote was added
git remote -v
```

### Step 6: Create and Push Main Branch

```bash
# Rename current branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 7: Create Dev Branch

```bash
# Create and switch to dev branch
git checkout -b dev

# Push dev branch
git push -u origin dev
```

---

## 🔄 Regular Development Workflow

### Working on a New Feature

```bash
# 1. Make sure you're on dev and it's up to date
git checkout dev
git pull origin dev

# 2. Create a feature branch
git checkout -b feature/comment-system

# 3. Make your changes
# ... edit files ...

# 4. Check what changed
git status
git diff

# 5. Stage your changes
git add .

# 6. Commit with descriptive message
git commit -m "feat(blog): add comment system with threading"

# 7. Push to GitHub
git push -u origin feature/comment-system
```

### Creating a Pull Request

1. Go to your GitHub repository
2. Click "Compare & pull request"
3. Base: `dev` ← Compare: `feature/comment-system`
4. Fill in the PR description
5. Click "Create pull request"

### Merging Feature to Dev

```bash
# After PR is approved, switch to dev
git checkout dev

# Pull latest changes
git pull origin dev

# Merge feature branch
git merge feature/comment-system

# Push to GitHub
git push origin dev

# Delete feature branch (optional)
git branch -d feature/comment-system
git push origin --delete feature/comment-system
```

### Merging Dev to Main (Release)

```bash
# Switch to main
git checkout main

# Pull latest
git pull origin main

# Merge dev
git merge dev

# Tag the release
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push with tags
git push origin main --tags
```

---

## 🛠️ Common Git Commands

### Checking Status
```bash
git status                 # See changed files
git log                    # See commit history
git log --oneline          # Compact commit history
git diff                   # See unstaged changes
git diff --staged          # See staged changes
```

### Branch Management
```bash
git branch                 # List local branches
git branch -a              # List all branches (including remote)
git checkout branch-name   # Switch to branch
git checkout -b new-branch # Create and switch to new branch
git branch -d branch-name  # Delete local branch
```

### Updating Code
```bash
git pull origin main       # Pull latest from main
git pull origin dev        # Pull latest from dev
git fetch --all            # Fetch all remote changes
```

### Undoing Changes
```bash
git checkout -- file.py    # Discard changes to file
git reset HEAD file.py     # Unstage file
git reset --hard HEAD      # Discard all local changes (DANGEROUS!)
git revert commit-hash     # Revert a specific commit
```

### Stashing (Temporary Save)
```bash
git stash                  # Save changes temporarily
git stash list             # List stashed changes
git stash pop              # Apply and remove latest stash
git stash apply            # Apply latest stash (keep in stash)
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Accidentally Committed .env File

```bash
# Remove from git tracking (keeps local file)
git rm --cached .env

# Commit the removal
git commit -m "Remove .env from tracking"

# Push
git push origin main
```

### Issue 2: Merge Conflict

```bash
# Pull latest changes
git pull origin dev

# Fix conflicts in files (look for <<<<<<< markers)
# Edit the files to resolve conflicts

# After fixing
git add .
git commit -m "Resolve merge conflicts"
git push origin dev
```

### Issue 3: Wrong Commit Message

```bash
# Change last commit message (before push)
git commit --amend -m "Corrected commit message"

# Force push (if already pushed - use carefully!)
git push --force origin branch-name
```

### Issue 4: Committed to Wrong Branch

```bash
# Move commit to correct branch
git checkout correct-branch
git cherry-pick commit-hash

# Remove from wrong branch
git checkout wrong-branch
git reset --hard HEAD~1
```

### Issue 5: Large Files Rejected

```bash
# Remove large file from git history
git rm --cached path/to/large/file

# Add to .gitignore
echo "path/to/large/file" >> .gitignore

# Commit
git commit -m "Remove large file"
git push origin main
```

---

## 📦 Updating requirements.txt

When you add new packages:

```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Commit
git add requirements.txt
git commit -m "Update dependencies"
git push origin dev
```

---

## 🏷️ Release Tagging

For version releases:

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial public release"

# Push tags
git push origin --tags

# List tags
git tag -l
```

### Semantic Versioning

Use version format: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (v2.0.0)
- **MINOR**: New features, backwards compatible (v1.1.0)
- **PATCH**: Bug fixes (v1.0.1)

---

## 🔐 GitHub Repository Settings

### Recommended Settings

1. **Branch Protection Rules**
   - Settings → Branches → Add rule
   - Branch name pattern: `main`
   - Enable:
     - ✅ Require pull request reviews before merging
     - ✅ Require status checks to pass
     - ✅ Include administrators

2. **Secrets** (for CI/CD)
   - Settings → Secrets → Actions
   - Add:
     - `SECRET_KEY`
     - `EMAIL_USER`
     - `EMAIL_USER_PASS`

3. **Collaborators**
   - Settings → Collaborators
   - Add team members

---

## 📊 Git Workflow Visualization

```
feature/comment-system ──┐
                         │
feature/user-profiles ───┼──→ dev ──→ main (v1.0.0)
                         │      ↑
feature/notifications ───┘      │
                                │
                         hotfix/critical-bug
```

---

## ✅ Safe Push Checklist

Before every push:

- [ ] `git status` shows no sensitive files
- [ ] `.env` is in `.gitignore` and not tracked
- [ ] `db.sqlite3` is not tracked
- [ ] `venv/` is not tracked
- [ ] Code has been tested locally
- [ ] Commit message is descriptive
- [ ] Pushing to correct branch
- [ ] No merge conflicts
- [ ] `requirements.txt` is up to date

---

## 🎯 Quick Reference Commands

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/campus-connect.git
git push -u origin main
```

### Daily Workflow
```bash
git checkout dev
git pull origin dev
git checkout -b feature/my-feature
# ... make changes ...
git add .
git commit -m "feat: add my feature"
git push -u origin feature/my-feature
# ... create PR on GitHub ...
```

### Check Before Push
```bash
git status           # What will be committed?
git diff            # What changed?
git log --oneline   # Recent commits
```

---

## 📞 Need Help?

If you encounter issues:

1. Check the error message carefully
2. Search on Stack Overflow
3. Refer to [GitHub Docs](https://docs.github.com)
4. Ask in project discussions

---

## 🎉 You're Ready!

Follow these steps carefully, and your code will be safely pushed to GitHub with proper version control and collaboration workflow!

**Remember:** 
- Never force push to `main` or `dev`
- Always create feature branches
- Write meaningful commit messages
- Review before pushing

**Happy Coding!** 🚀
