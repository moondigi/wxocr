import os
import uuid
import base64
import wcocr

wcocr.init("/app/wx/opt/wechat/wxocr", "/app/wx/opt/wechat")


def ocr(image_data):
    # Create temp directory if not exists
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Generate unique filename and save image
    filename = os.path.join(temp_dir, f"{str(uuid.uuid4())}.png")
    try:
        image_bytes = base64.b64decode(image_data)
        if len(image_bytes) == 0:
            return {"error": "Image data is empty"}
        with open(filename, "wb") as f:
            f.write(image_bytes)

        # Process image with OCR
        result = wcocr.ocr(filename)
        return result

    finally:
        # Clean up temp file
        if os.path.exists(filename):
            os.remove(filename)
