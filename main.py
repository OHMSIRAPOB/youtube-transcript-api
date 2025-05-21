from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from youtube-transcript-api (proxy)! Use /subtitles?id=VIDEO_ID'

@app.route('/subtitles')
def get_subtitles():
    video_id = request.args.get('id')
    if not video_id:
        return jsonify({'error': 'No video ID provided'}), 400

    response = requests.get(f'https://youtube-transcript-api.deno.dev/?id={video_id}')
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch transcript'}), response.status_code

    return jsonify(response.json())
