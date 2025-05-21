from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from youtube-transcript-api! Use /subtitles?id=VIDEO_ID'

@app.route('/subtitles')
def get_subtitles():
    video_id = request.args.get('id')
    if not video_id:
        return jsonify({'error': 'No video ID provided'}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return jsonify(transcript)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
