from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import PromptForm
import openai


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PromptForm()
    if form.validate_on_submit():
        occasionData = form.occasion.data
        contentData = form.content.data
        length = form.length.data
        openai.api_key = "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" //old key
        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.5,
        max_tokens = 1000,
        messages = [{"role": "system", "content": f"You are writing a card with"},
                    {"role": "user", "content": f"Write a {length} card for a {occasionData} that is about: {contentData}"}])
        text = response['choices'][0]['message']['content']
        print(text)
        text.replace('>', '')
        flash(text)
    return render_template('index.html', title='Home', form=form)



