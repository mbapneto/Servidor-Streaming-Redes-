from flask import Flask, jsonify, send_from_directory, request, abort
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = rf'C:\Users\{os.getlogin()}\Downloads\\'

@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = os.listdir(DOWNLOAD_FOLDER)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/stream/<filename>', methods=['GET'])
def stream_file(filename):
    try:
        if filename.endswith('.mp4'):
            return send_from_directory(DOWNLOAD_FOLDER, filename)
        else:
            return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
