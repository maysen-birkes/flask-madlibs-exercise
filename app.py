from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "top-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def madlib_questions():
    """Generate the form to ask questions"""

    questions = story.prompts

    return render_template('questions.html', prompts=questions)

@app.route('/story')
def completed_story():
    """Show the completed story"""
    
    text = story.generate(request.args)

    return render_template('story.html', text=text)