import uvicorn
from fastapi import FastAPI

from app.common.config import settings
from app.model.model import load_model, perform_inference
from app.schemas.schemas import ActionRequestSchema, ActionResponseSchema

app = FastAPI()
model = load_model(settings.REPO_ID, settings.MODEL_FILENAME)


@app.post("/api/inference", response_model=ActionResponseSchema)
def inference(data: ActionRequestSchema):
    action = perform_inference(model=model, data=data)
    return {"action": action}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=settings.DEBUG)
