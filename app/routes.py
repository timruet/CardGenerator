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
        property1Data = form.text1.data
        property2Data = form.text2.data
        property3Data = form.text3.data
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        temperature = 0.2,
        max_tokens = 200,
        messages = [{"role": "system", "content": f"You are writing a card"},
                    {"role": "user", "content": f"Write a card for a {occasionData} that is about: {property1Data}, {property2Data}, {property3Data}"}])
        text = response['choices'][0]['message']['content']
        flash(text)
    return render_template('index.html', title='Home', form=form)



