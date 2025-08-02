from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import base64
from rembg_model import remove_background

app = FastAPI()

@app.post("/remove-background")
async def remove_bg(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        removed_bg_bytes = remove_background(image_data)

        encoded_string = base64.b64encode(removed_bg_bytes).decode("utf-8")

        return JSONResponse(content={
            "status": "success",
            "image_base64": encoded_string
        })

    except Exception as e:
        return JSONResponse(content={
            "status": "error",
            "message": str(e)
        }, status_code=500)
