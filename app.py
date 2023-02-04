from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/volunteer', methods=['GET'])
def volunteer():
    return render_template('volunteer.html')

@app.route('/propose', methods=['GET'])
def propose():
    return render_template('propose.html')

if __name__ == '__main__':
    app.run(debug=True)