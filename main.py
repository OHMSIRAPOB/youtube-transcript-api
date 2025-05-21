from flask import Flask, request, jsonify
from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

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
        formatter = JSONFormatter()
        return jsonify(transcript)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
