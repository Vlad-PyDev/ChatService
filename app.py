from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

messages = []


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
  if request.method == 'POST':
    username = request.form.get('username', 'Аноним')
    message = request.form.get('message')
    if message:
      messages.append({'username': username, 'message': message})
    return redirect(url_for('main'))
  return render_template('main.html', messages=messages)


@app.route('/api/messages')
def api_messages():
  return jsonify(messages)


if __name__ == '__main__':
  app.run(debug=True)