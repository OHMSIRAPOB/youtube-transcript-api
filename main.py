from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/subtitles')
def get_subtitles():
    video_id = request.args.get('id')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return jsonify(transcript)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return '✅ Hello from youtube-transcript-api! Use /subtitles?id=VIDEO_ID'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
