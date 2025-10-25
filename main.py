#!/usr/bin/env python3
"""
Vercel entry point for AI Business Analyzer
"""
import sys
import os

# Add the ai-business-analyzer directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, 'ai-business-analyzer')
sys.path.insert(0, app_dir)

# Import the FastAPI app
from app.main import app

# This is what Vercel will use
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)