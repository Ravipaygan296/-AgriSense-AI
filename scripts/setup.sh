#!/bin/bash

# AgriSense AI - Project Setup Script
echo "🌾 AgriSense AI - Project Setup"
echo "================================"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "package.json" ] || [ ! -d "frontend" ]; then
    print_warning "This script should be run from the AgriSense-AI root directory"
    echo "Current directory: $(pwd)"
    echo "Expected structure:"
    echo "  AgriSense-AI/"
    echo "  ├── frontend/"
    echo "  ├── backend/"
    echo "  └── package.json"
    exit 1
fi

print_info "Setting up AgriSense AI development environment..."

# Check for required tools
print_info "Checking system requirements..."

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_status "Python $PYTHON_VERSION found"
else
    print_warning "Python 3 not found. Please install Python 3.8 or later"
fi

# Check Node.js (optional)
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_status "Node.js $NODE_VERSION found"
else
    print_info "Node.js not found (optional for development)"
fi

# Check Git
if command -v git &> /dev/null; then
    print_status "Git found"
else
    print_warning "Git not found. Install Git for version control"
fi

# Setup Python virtual environment
print_info "Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_status "Virtual environment created"
else
    print_info "Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
print_info "Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
print_status "Python dependencies installed"

# Install Node.js dependencies (if package.json exists)
if [ -f "package.json" ] && command -v npm &> /dev/null; then
    print_info "Installing Node.js dependencies..."
    npm install
    print_status "Node.js dependencies installed"
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    print_info "Creating .env file from template..."
    cat > .env << 'ENV_EOF'
# AgriSense AI - Environment Variables
DEBUG=True
OPENWEATHER_API_KEY=your_openweather_api_key_here
DATABASE_URL=sqlite:///./agrisense.db
SECRET_KEY=your-secret-key-change-this-in-production
ENV_EOF
    print_status ".env file created"
    print_warning "Please update .env file with your actual API keys"
else
    print_info ".env file already exists"
fi

# Make scripts executable
print_info "Making scripts executable..."
chmod +x scripts/*.sh
print_status "Scripts are now executable"

# Database initialization
print_info "Initializing database..."
cd backend
python -c "
import sqlite3
conn = sqlite3.connect('agrisense.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";')
tables = cursor.fetchall()
if not tables:
    print('Creating database tables...')
    exec(open('app.py').read())
else:
    print('Database tables already exist')
conn.close()
"
cd ..
print_status "Database initialized"

print_status "Setup complete!"
echo ""
echo "🚀 Next steps:"
echo "1. Update .env file with your API keys"
echo "2. Replace frontend/index.html with the complete AgriSense AI application"
echo "3. Run: ./scripts/dev-server.sh to start development server"
echo "4. Run: ./scripts/deploy.sh to deploy to production"
echo ""
echo "📚 Documentation:"
echo "   - User Guide: docs/USER_GUIDE.md"
echo "   - API Docs: docs/API.md"
echo "   - Deployment: docs/DEPLOYMENT.md"
echo ""
print_status "Happy farming with AgriSense AI! 🌾"
