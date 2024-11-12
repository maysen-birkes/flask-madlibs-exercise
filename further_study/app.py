from flask import Flask, render_template, request, redirect, url_for
from stories_fs import stories, Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "top-secret"

added_stories = [stories]

@app.route('/')
def story_selection():
    """Generate a form for user to select a story"""

    return render_template("selections.html", stories=stories.values())

@app.route('/questions')
def madlib_questions():
    """Generate the form to ask questions"""

    story_id = request.args['story_id']
    story = stories[story_id]

    questions = story.prompts

    return render_template('questions_fs.html', story_id=story_id, title=story.title, prompts=questions)

@app.route('/story')
def completed_story():
    """Show the completed story"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story_fs.html", title=story.title, text=text)

@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if request.method == 'POST':
        token = request.form['story_token'] 
        title = request.form['story_title']
        text = request.form['story_text']
        parts_of_speech = request.form['parts_of_speech'].split(',')
        
        new_story = Story(token, title, parts_of_speech, text)
        stories[token] = new_story  # Store the new story using its token as the key

        return redirect(url_for('story_selection'))  # Redirect to the root route
    return render_template('create_story.html')