from flask import *
from translated import get_translation
from gtts import gTTS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MINKALEXVINA'

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    languageInp = data['slang']
    text_input = data['text']
    translation_output = data['to']
    response = get_translation(languageInp, text_input, translation_output)
    return jsonify(response)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text_input = data['text']
    voice_font = data['voice']

    tts = gTTS(text=text_input, lang=voice_font)
    tts.save('output.mp3')

    return send_file('output.mp3', mimetype='audio/mpeg')
