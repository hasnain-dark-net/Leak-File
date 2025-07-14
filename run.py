from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Auto create uploads folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(save_path)
            message = "✅ File Successfully Uploaded!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    print("[+] Running on http://localhost:8000")
    app.run(host='0.0.0.0', port=8000)
