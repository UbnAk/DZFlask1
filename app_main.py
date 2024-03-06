from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/cloth/')
def cloth():
    context = {'title': 'Одежда'}
    return render_template('cloth.html', **context)

# if __name__ == '__main__':
#     app.run(debug=True)