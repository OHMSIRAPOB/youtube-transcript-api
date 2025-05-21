import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/subtitles')
def get_subtitles():
    video_id = request.args.get('id')
    try:
        res = requests.get(f'https://youtube-transcript-api.deno.dev/?id={video_id}')
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return '✅ Hello from youtube-transcript-api (proxy)! Use /subtitles?id=VIDEO_ID'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
