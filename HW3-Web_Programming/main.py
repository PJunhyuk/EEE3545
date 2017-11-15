from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    return render_template("login.html")

@app.route('/status', methods=['POST'])
def status():
    form = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Logged in Status Page</title>
    </head>
    <body>
        <p>Hello 
    """ + str(request.form['id']) + """
        </p>
        <form action="/audio" method="POST">
            <input type="submit" value="Audio Button">
        </form>
        <form action="/video" method="POST">
            <input type="submit" value="Video Button">
        </form>
        <form action="/" method="GET">
            <input type="submit" value="Logout Button">
        </form>
    </body>
    </html>
    """
    return form

@app.route('/audio', methods=['POST'])
def audio():
    return render_template("audio.html")

@app.route('/video', methods=['POST'])
def video():
    return render_template("video.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
