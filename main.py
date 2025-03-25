from flask import Flask, request, jsonify
from ocr import ocr

app = Flask(__name__)


@app.route("/ocr", methods=["POST"])
def ocr_api():
    try:
        # Get base64 image from request
        image_data = request.json.get("image")
        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        return jsonify({"result": ocr(image_data)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

