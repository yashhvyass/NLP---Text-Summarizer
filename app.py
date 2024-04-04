from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from src.textSummarizer.pipeline.prediction import PredictionPipeline

# Create an instance of the FastAPI class
app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) to allow communication with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity, you can adjust this to a specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'static' directory to serve static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define your HTML templates
templates = Jinja2Templates(directory="templates")

# Define the request model for paraphrasing
class ParaphraseRequest(BaseModel):
    text: str
    max_length: int  # Add max_length parameter

# Your paraphrase endpoint
@app.post("/paraphrase")
async def paraphrase(request: ParaphraseRequest):
    input_text = request.text
    max_length = request.max_length  # Extract max_length from request
    try:
        obj = PredictionPipeline()
        paraphrased_text = obj.predict(input_text, max_length=max_length)  # Pass max_length to prediction
        return JSONResponse(content={"paraphrased_text": paraphrased_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# Endpoint to serve the HTML page
@app.get("/", tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the app if this script is executed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
