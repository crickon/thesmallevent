from flask import Flask, render_template, request, redirect
app = Flask(__name__)

keys=['organizer', 'title', 'description', 'link', 'contact-name',
'contact-email', 'contact-phone', 'date', 'time', 'location', 'doing', 'bring-wear']

proposals = [
    {
        'id':'0',
        'organizer':'Adults Heart Association',
        'title':'One Tree Planted',
        'description':'Make a positive environmental impact in your community',
        'link':'https://google.com',
        'contact-name':'Tim Sands',
        'contact-email':'janedoe123@email.com',
        'contact-phone':'999-999-9999',
        'date':'Wed, Feb 7th, 2023 - Tue, Feb 28th, 2023',
        'time':'10 AM - 11:59 PM (EST)',
        'location':'677 South Main Street Blacksburg, Virginia 24060',
        'doing':'Upon arriving, you should dolor sit amet consectetur adipisicing elit. Aliquid beatae sequi corrupti voluptates quaerat et, sapiente voluptatum omnis reiciendis voluptatem eaque necessitatibus, unde ratione itaque nam vitae ipsa minus natus?',
        'bring-wear':'Dress comfortably dolor sit amet consectetur adipisicing elit. Aliquid beatae sequi corrupti voluptates quaerat et, sapiente voluptatum omnis reiciendis voluptatem eaque necessitatibus, unde ratione itaque nam vitae ipsa minus natus?'
    }
]

unique_id = len(proposals)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', projects=proposals)

@app.route('/about', methods=['GET'])
def volunteer():
    return render_template('about.html')

@app.route('/projects/submit', methods=['GET'])
def propose():
    return render_template('propose.html')

@app.route('/projects/add', methods=['POST'])
def post_add():
    proposal = proposals[len(proposals) - 1].copy() # copy the last entry
    for key in keys:
        proposal[key] = request.form.get(key)
    proposal['id'] = str(int(proposal.get('id')) + 1)
    proposals.append(proposal)
    return redirect('/')

@app.route('/projects/', methods=['GET'])
@app.route('/projects/list', methods=['GET'])
def get_proposalsList():
    return proposals

@app.errorhandler(404)
def not_found(e):
    return redirect('/')

@app.route('/event/<id>')
def event(id):
    id = int(id)
    return render_template("event.html", project=proposals[id])

if __name__ == '__main__':
    app.run(debug=True)