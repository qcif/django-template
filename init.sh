#!/bin/bash

# Django Template Initialization Script
# This script customizes the template project with your project name

set -e  # Exit on any error

echo "Django Template Project Initialization"
echo "====================================="
echo

# Get project name from user
read -p "Enter your project name (alphanumeric and underscores only): " PROJECT_NAME

# Validate project name
if [[ ! "$PROJECT_NAME" =~ ^[a-zA-Z_][a-zA-Z0-9_]*$ ]]; then
    echo "Error: Project name must start with a letter or underscore and contain only letters, numbers, and underscores."
    exit 1
fi

if [ -z "$PROJECT_NAME" ]; then
    echo "Error: Project name cannot be empty."
    exit 1
fi

echo
echo "Initializing project: $PROJECT_NAME"
echo

# Replace all instances of 'myproject' (case insensitive) in files
echo "1. Replacing 'myproject' with '$PROJECT_NAME' in all files..."

# Find all files (excluding .git, __pycache__, and binary files) and replace content
find . -type f \
    -not -path "./.git/*" \
    -not -path "./__pycache__/*" \
    -not -path "./venv/*" \
    -not -path "*/__pycache__/*" \
    -not -path "*/migrations/*" \
    -not -name "*.pyc" \
    -not -name "*.pyo" \
    -not -name "*.so" \
    -not -name "*.db" \
    -not -name "*.sqlite3" \
    -exec grep -l -i "myproject" {} \; 2>/dev/null | \
while read -r file; do
    echo "  Updating: $file"
    sed -i.bak "s/myproject/$PROJECT_NAME/gi" "$file"
    rm "$file.bak"
done

# Rename directories
echo
echo "2. Renaming directories..."

# We should be in the template root directory that contains myproject/
if [ -d "myproject" ]; then
    echo "  Renaming: myproject -> $PROJECT_NAME"
    mv "myproject" "$PROJECT_NAME"
    
    # Rename inner project directory
    if [ -d "$PROJECT_NAME/myproject" ]; then
        echo "  Renaming: $PROJECT_NAME/myproject -> $PROJECT_NAME/$PROJECT_NAME"
        mv "$PROJECT_NAME/myproject" "$PROJECT_NAME/$PROJECT_NAME"
    fi
    
    # Update manage.py path
    if [ -f "$PROJECT_NAME/manage.py" ]; then
        echo "  Updating manage.py settings path..."
        sed -i.bak "s/myproject\.settings\.base/$PROJECT_NAME.settings.base/g" "$PROJECT_NAME/manage.py"
        rm "$PROJECT_NAME/manage.py.bak"
    fi
else
    echo "Error: myproject directory not found. Please run this script from the template root directory."
    exit 1
fi

echo
echo "✅ Project initialization complete!"
echo
echo "Next steps:"
echo "1. cd $PROJECT_NAME"
echo "2. Create and activate a virtual environment"
echo "3. pip install -r requirements.txt"
echo "4. Copy .env.sample to .env and configure your environment variables"
echo "5. python manage.py migrate"
echo "6. python manage.py createsuperuser"
echo "7. python manage.py runserver"
echo
echo "Happy coding! 🚀"
echo
echo "You can now remove this init.sh script."
echo
