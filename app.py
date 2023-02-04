from flask import Flask, render_template, request, redirect
app = Flask(__name__)

proposals = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/volunteer', methods=['GET'])
def volunteer():
    return render_template('volunteer.html')

@app.route('/propose', methods=['GET'])
def propose():
    return render_template('propose.html')

@app.route('/add', methods=['GET','POST'])
def post_add():
    first_name = request.form['first_name']
    print("Received %s"%first_name)
    return redirect('/success')

@app.route('/success', methods=['GET'])
def success():
    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)