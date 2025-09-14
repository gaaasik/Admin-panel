import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "Нет файла"
        file = request.files["file"]
        if file.filename == "":
            return "Файл не выбран"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        return redirect(url_for("viewer", filename=file.filename))
    return render_template("index.html")

@app.route("/viewer/<filename>")
def viewer(filename):
    return render_template("viewer.html", filename=filename)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
