from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return "❌ No se recibió ningún enlace"

        try:
            response = requests.get(url, stream=True)
            save_path = os.path.join("app/static", "video.mp4")
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return "✅ Video descargado correctamente"
        except Exception as e:
            return f"⚠️ Ocurrió un error: {e}"

    return render_template("index.html")







