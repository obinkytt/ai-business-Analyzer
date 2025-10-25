from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Business Analyzer is running on Vercel!", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "platform": "vercel"}

# Vercel expects this
def handler(request):
    return app(request)