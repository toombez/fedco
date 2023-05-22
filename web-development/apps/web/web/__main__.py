from flask import Flask, render_template
from datetime import datetime
from models import News, Module, Theme, ThemeMaterial, ThemeSkill

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.context_processor
def inject_models():
    return {
        'News': News,
        'Module': Module,
        'Theme': Theme,
        'ThemeMaterial': ThemeMaterial,
        'ThemeSkill': ThemeSkill,
    }

@app.route('/')
def index():
    return render_template('index.j2')

@app.route('/news')
def news():
    return render_template('news.j2')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
