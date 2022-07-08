from flask import Flask, render_template, request, url_for
app = Flask(__name__)
from consumeAll import responseGet
from consumeCreate import createBooks

@app.route('/<hi>')
def hello_world(hi):
    return render_template('index.html', name=hi)

@app.route('/library')
def holla():
    jsonObj = responseGet()
    print(jsonObj)
    return render_template('library.html', con = jsonObj)  


@app.route('/postbook', methods=['GET','POST'])
def postbook():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        image = request.form.get('image') 
        createBooks(name, price, image)

    return render_template('postBook.html')     


if __name__ == '__main__':
    app.run(debug=True)    