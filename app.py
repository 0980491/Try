from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first_page')
def home():
    return render_template('first_page.php')


@app.route('/recomendados')
def appsrecomendadas():
    return render_template('appsrecomendadas.php')


@app.route('/contact')
def contact():
    return render_template('contact.php')


@app.route('/about')
def about():
    return render_template('about.php')


@app.route('/Informatica_tecnologia')
def teninformatica():
    return render_template('informatica.php')


@app.route('/6')
def six():
    return render_template('6.php')


@app.route('/6/Biologia_Quimica')
def sixbiologia():
    return render_template('6biologia.php')


@app.route('/6/Sociales_integradas')
def sixhistoria():
    return render_template('6historia.php')


@app.route('/6/Español')
def sixepanol():
    return render_template('6epanol.php')


@app.route('/6/Filosofia')
def sixfilosofia():
    return render_template('6filosofia.php')


@app.route('/7')
def seven():
    return render_template('7.php')


@app.route('/7/Biologia_Quimica')
def sevenbiologia():
    return render_template('7biologia.php')


@app.route('/7/Sociales_integradas')
def sevenhistoria():
    return render_template('7historia.php')


@app.route('/7/Español')
def sevenepanol():
    return render_template('7epanol.php')


@app.route('/7/Filosofia')
def sevenfilosofia():
    return render_template('7filosofia.php')


@app.route('/8')
def eight():
    return render_template('8.php')


@app.route('/8/Biologia_Quimica')
def eightbiologia():
    return render_template('8biologia.php')


@app.route('/8/Sociales_integradas')
def eighthistoria():
    return render_template('8historia.php')


@app.route('/8/Español')
def eightepanol():
    return render_template('8epanol.php')


@app.route('/8/Filosofia')
def eightfilosofia():
    return render_template('8filosofia.php')


@app.route('/9')
def nine():
    return render_template('9.php')


@app.route('/9/Biologia_Quimica')
def ninebiologia():
    return render_template('9biologia.php')


@app.route('/9/Sociales_integradas')
def ninehistoria():
    return render_template('9historia.php')


@app.route('/9/Español')
def nineepanol():
    return render_template('9epanol.php')


@app.route('/9/Filosofia')
def ninefilosofia():
    return render_template('9filosofia.php')


@app.route('/10')
def ten():
    return render_template('10.php')


@app.route('/10/Biologia_Quimica')
def tenbiologia():
    return render_template('10biologia.php')


@app.route('/10/Sociales_integradas')
def tenhistoria():
    return render_template('10historia.php')


@app.route('/10/Español')
def tenepanol():
    return render_template('10epanol.php')


@app.route('/10/Filosofia')
def tenfilosofia():
    return render_template('10filosofia.php')


@app.route('/11')
def eleven():
    return render_template('11.php')


@app.route('/11/Biologia_Quimica')
def elevenbiologia():
    return render_template('11biologia.php')


@app.route('/11/Sociales_integradas')
def elevenhistoria():
    return render_template('11historia.php')


@app.route('/11/Español')
def elevenepanol():
    return render_template('11epanol.php')


@app.route('/11/Filosofia')
def elevenfilosofia():
    return render_template('11filosofia.php')


if __name__ == "__main__":
    app.run(debug=True)