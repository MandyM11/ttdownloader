from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return "❌ No se recibió ningún enlace"

        try:
            response = requests.get(url, stream=True)
            return Response(
                response.iter_content(chunk_size=1024),
                content_type=response.headers.get("content-type", "video/mp4"),
                headers={"Content-Disposition": "attachment; filename=video.mp4"}
            )
        except Exception as e:
            return f"⚠️ Ocurrió un error: {e}"

    return render_template("index.html")








