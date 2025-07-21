from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Auto-create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file and uploaded_file.filename != '':
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            filename = f"{timestamp}_{uploaded_file.filename}"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(save_path)
            message = f"✅ File Successfully Uploaded as {filename}!"
        else:
            message = "❌ No file selected!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    print("[+] Server running at http://localhost:8000")
    print("[+] Powered by Hasnain Dark Net")
    app.run(host='0.0.0.0', port=8000)
