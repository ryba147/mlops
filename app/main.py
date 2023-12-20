import uvicorn
from fastapi import FastAPI

from app.common.config import settings
from app.model.model import load_model

app = FastAPI()


@app.post("/api/inference")
def inference():
    model = load_model(settings.REPO_ID, settings.MODEL_FILENAME)
    # result = perform_inference()
    return {"result": "result"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
