from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Business Analyzer", "status": "running", "platform": "vercel"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# Test if we can import the main app
@app.get("/test")
async def test_import():
    try:
        import sys
        import os
        
        # Add the current directory to path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        sys.path.insert(0, parent_dir)
        
        # Try to import
        from app.main import app as main_app
        return {"status": "success", "message": "Main app imported successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e), "type": type(e).__name__}

# This is what Vercel will call
def handler(event, context):
    return app