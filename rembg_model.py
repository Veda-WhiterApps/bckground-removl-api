from rembg import remove
from PIL import Image
import io

def remove_background(input_bytes: bytes) -> bytes:
    input_image = Image.open(io.BytesIO(input_bytes)).convert("RGBA")
    output_image = remove(input_image)
    
    byte_stream = io.BytesIO()
    output_image.save(byte_stream, format="PNG")
    return byte_stream.getvalue()
