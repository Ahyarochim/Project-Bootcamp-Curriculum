#!/bin/bash
# Quick Start Script untuk Bootcamp Generator
# Jalankan dengan: bash quick_start.sh

echo "🚀 Bootcamp Curriculum Generator - Quick Start"
echo "=============================================="
echo ""

# Check Python
echo "📍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi
python_version=$(python3 --version)
echo "✅ $python_version"
echo ""

# Check Node.js
echo "📍 Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo "⚠️ Node.js not found. Install Node.js 18+ for API server"
else
    node_version=$(node --version)
    echo "✅ Node.js $node_version"
fi
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install openai python-docx --quiet
echo "✅ Python packages installed"
echo ""

# Install Node dependencies (if package.json exists)
if [ -f "package.json" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install --silent
    echo "✅ Node packages installed"
    echo ""
fi

# Check for API key
echo "🔑 Checking OpenAI API key..."
if [ -f ".env.local" ]; then
    echo "✅ .env.local found"
elif [ -f "api_openai.txt" ]; then
    echo "✅ api_openai.txt found"
else
    echo "⚠️ API key not found!"
    echo ""
    echo "Please create one of these files:"
    echo "  1. .env.local with: OPENAI_API_KEY=sk-your-key"
    echo "  2. api_openai.txt with: sk-your-key"
    echo ""
    read -p "Enter your OpenAI API key (or press Enter to skip): " api_key
    if [ ! -z "$api_key" ]; then
        echo "OPENAI_API_KEY=$api_key" > .env.local
        echo "✅ API key saved to .env.local"
    fi
fi
echo ""

# Run example generation
echo "🎯 Running example bootcamp generation..."
echo ""
python3 ai_to_json.py \
  --name "Python Programming Bootcamp for Beginners" \
  --durasi 6 \
  --level "Beginner" \
  --context "Focus on practical projects, web scraping, data analysis" \
  --output "example_bootcamp.json"

echo ""

# Convert to DOCX
if [ -f "example_bootcamp.json" ]; then
    echo "📄 Converting to DOCX..."
    python3 json_to_docx.py \
      --input "example_bootcamp.json" \
      --output "example_bootcamp.docx"
    echo ""
    echo "✅ SETUP COMPLETE!"
    echo ""
    echo "Generated files:"
    echo "  📁 example_bootcamp.json"
    echo "  📁 example_bootcamp.docx"
    echo ""
else
    echo "⚠️ Generation failed - check API key"
fi

echo "🎉 Quick start complete!"
echo ""
echo "Next steps:"
echo "  1. Check example_bootcamp.json for JSON structure"
echo "  2. Open example_bootcamp.docx to see DOCX output"
echo "  3. Start API server: node express_api.js"
echo "  4. Or use React form in your Next.js app"
echo ""
echo "Documentation: See README.md"
