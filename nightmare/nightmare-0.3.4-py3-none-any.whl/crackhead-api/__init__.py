from flask import Flask
import ffmpeg
app = Flask('Nightmare Village')

@app.route('/test')
def start():
  return 'Nightmare Village Blog is online'

app.run(host='0.0.0.0', port=8080)