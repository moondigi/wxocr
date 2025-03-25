import runpod
from runpod.serverless.utils import rp_upload
from ocr import ocr


def handler(job):
    input = job["input"]
    image = input.get("image")

    return ocr(image)


# Start the handler only if this script is run directly
if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
