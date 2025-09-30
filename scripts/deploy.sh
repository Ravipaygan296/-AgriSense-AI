#!/bin/bash

# AgriSense AI - Deployment Script
echo "🚀 AgriSense AI - Deployment Assistant"
echo "======================================"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

print_status() { echo -e "${GREEN}✅ $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }

# Check if main files exist
check_files() {
    print_info "Checking required files..."
    
    if [ ! -f "frontend/index.html" ]; then
        print_error "frontend/index.html not found!"
        print_warning "Please ensure the complete AgriSense AI HTML is in frontend/index.html"
        return 1
    fi
    
    if [ ! -f "README.md" ]; then
        print_warning "README.md not found (recommended)"
    fi
    
    if [ ! -f "LICENSE" ]; then
        print_warning "LICENSE file not found (recommended)"
    fi
    
    print_status "Required files check passed"
    return 0
}

# Show deployment options
show_options() {
    echo ""
    print_info "Choose your deployment platform:"
    echo ""
    echo "1️⃣  Hugging Face Spaces (Recommended - FREE Forever)"
    echo "   • Zero configuration needed"
    echo "   • Upload frontend/index.html only"
    echo "   • Global CDN and fast loading"
    echo ""
    echo "2️⃣  Netlify (Drag & Drop - FREE)"
    echo "   • Instant deployment"
    echo "   • Custom domain support"
    echo "   • Form handling included"
    echo ""
    echo "3️⃣  Vercel (GitHub Integration - FREE)" 
    echo "   • Auto-deploy on git push"
    echo "   • Serverless functions"
    echo "   • Great performance"
    echo ""
    echo "4️⃣  GitHub Pages (Static Hosting - FREE)"
    echo "   • Simple static hosting"
    echo "   • Custom domain possible"
    echo "   • Built into GitHub"
    echo ""
    echo "5️⃣  Docker Deployment (Self-hosted)"
    echo "   • Full control over environment"
    echo "   • Can include backend features"
    echo "   • Scalable infrastructure"
    echo ""
    echo "6️⃣  Local Development Server"
    echo "   • Test locally before deployment"
    echo "   • Development and debugging"
    echo ""
}

# Deploy to Hugging Face Spaces
deploy_huggingface() {
    print_info "Deploying to Hugging Face Spaces..."
    echo ""
    echo "📋 Manual Steps Required:"
    echo "1. Go to: https://huggingface.co/spaces"
    echo "2. Click 'Create new Space'"
    echo "3. Choose 'Static HTML' as SDK"
    echo "4. Upload: frontend/index.html"
    echo "5. Your app will be live at: https://huggingface.co/spaces/USERNAME/agrisense-ai"
    echo ""
    
    # Copy file to deployment directory for easy access
    mkdir -p deployment/huggingface
    cp frontend/index.html deployment/huggingface/
    
    print_status "File prepared in deployment/huggingface/index.html"
    print_info "Upload this file to Hugging Face Spaces"
    
    # Open browser if possible
    if command -v open &> /dev/null; then
        open "https://huggingface.co/spaces"
    elif command -v xdg-open &> /dev/null; then
        xdg-open "https://huggingface.co/spaces"
    fi
}

# Deploy to Netlify
deploy_netlify() {
    print_info "Deploying to Netlify..."
    
    # Prepare Netlify deployment
    mkdir -p deployment/netlify
    cp frontend/index.html deployment/netlify/
    cp deployment/platforms/netlify/netlify.toml deployment/netlify/
    
    print_status "Files prepared in deployment/netlify/"
    echo ""
    echo "📋 Deployment Steps:"
    echo "1. Go to: https://app.netlify.com/drop"
    echo "2. Drag the deployment/netlify/ folder to the drop zone"
    echo "3. Your app will be live instantly!"
    echo ""
    
    if command -v open &> /dev/null; then
        open "https://app.netlify.com/drop"
    elif command -v xdg-open &> /dev/null; then
        xdg-open "https://app.netlify.com/drop"
    fi
}

# Deploy to Vercel
deploy_vercel() {
    print_info "Deploying to Vercel..."
    
    # Check if project is in git
    if [ ! -d ".git" ]; then
        print_warning "Git repository not found. Initializing..."
        git init
        git add .
        git commit -m "Initial commit: AgriSense AI"
        print_status "Git repository initialized"
    fi
    
    # Prepare Vercel config
    cp deployment/platforms/vercel/vercel.json ./
    
    print_status "Vercel configuration ready"
    echo ""
    echo "📋 Deployment Steps:"
    echo "1. Push your code to GitHub:"
    echo "   git remote add origin https://github.com/USERNAME/agrisense-ai.git"
    echo "   git push -u origin main"
    echo "2. Go to: https://vercel.com/new"
    echo "3. Import your GitHub repository"
    echo "4. Deploy with default settings"
    echo ""
    
    if command -v open &> /dev/null; then
        open "https://vercel.com/new"
    elif command -v xdg-open &> /dev/null; then
        xdg-open "https://vercel.com/new"
    fi
}

# Deploy to GitHub Pages
deploy_github_pages() {
    print_info "Setting up GitHub Pages deployment..."
    
    if [ ! -d ".git" ]; then
        print_info "Initializing Git repository..."
        git init
        git add .
        git commit -m "Initial commit: AgriSense AI"
    fi
    
    print_status "GitHub Pages setup ready"
    echo ""
    echo "📋 Deployment Steps:"
    echo "1. Create GitHub repository: https://github.com/new"
    echo "2. Push your code:"
    echo "   git remote add origin https://github.com/USERNAME/agrisense-ai.git"
    echo "   git push -u origin main"
    echo "3. Go to repository Settings > Pages"
    echo "4. Select 'Deploy from main branch'"
    echo "5. Your app will be live at: https://USERNAME.github.io/agrisense-ai"
    echo ""
    
    if command -v open &> /dev/null; then
        open "https://github.com/new"
    elif command -v xdg-open &> /dev/null; then
        xdg-open "https://github.com/new"
    fi
}

# Docker deployment
deploy_docker() {
    print_info "Preparing Docker deployment..."
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker not found. Please install Docker first."
        return 1
    fi
    
    print_info "Building Docker image..."
    docker build -t agrisense-ai -f deployment/Dockerfile .
    
    if [ $? -eq 0 ]; then
        print_status "Docker image built successfully"
        echo ""
        echo "🚀 Run your application:"
        echo "   docker run -p 8000:8000 agrisense-ai"
        echo ""
        echo "🌐 Access your app at: http://localhost:8000"
        echo ""
        echo "📋 Production deployment:"
        echo "1. Push image to Docker Hub:"
        echo "   docker tag agrisense-ai USERNAME/agrisense-ai"
        echo "   docker push USERNAME/agrisense-ai"
        echo "2. Deploy to any cloud provider supporting Docker"
    else
        print_error "Docker build failed"
        return 1
    fi
}

# Local development server
start_dev_server() {
    print_info "Starting local development server..."
    
    if command -v python3 &> /dev/null; then
        cd frontend
        print_status "Server starting at http://localhost:8000"
        print_info "Press Ctrl+C to stop the server"
        echo ""
        
        # Open browser automatically
        if command -v open &> /dev/null; then
            open "http://localhost:8000" &
        elif command -v xdg-open &> /dev/null; then
            xdg-open "http://localhost:8000" &
        fi
        
        python3 -m http.server 8000
    else
        print_error "Python 3 not found. Please install Python 3."
        return 1
    fi
}

# Main deployment logic
main() {
    # Check files first
    if ! check_files; then
        exit 1
    fi
    
    # Show options
    show_options
    
    # Get user choice
    echo ""
    read -p "Enter your choice (1-6): " choice
    echo ""
    
    case $choice in
        1)
            deploy_huggingface
            ;;
        2)
            deploy_netlify
            ;;
        3)
            deploy_vercel
            ;;
        4)
            deploy_github_pages
            ;;
        5)
            deploy_docker
            ;;
        6)
            start_dev_server
            ;;
        *)
            print_error "Invalid choice. Please run the script again."
            exit 1
            ;;
    esac
    
    echo ""
    print_status "Deployment process initiated!"
    echo ""
    print_info "Need help? Check docs/DEPLOYMENT.md for detailed instructions"
    print_status "Your AgriSense AI will be helping farmers soon! 🌾"
}

# Run main function
main


