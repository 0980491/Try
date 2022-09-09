from multiprocessing import context
from flask import Flask, redirect, render_template, request, url_for
import smtplib, ssl

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if (request.form['username']=="GNF_Apuntes") and (request.form['password']=="29080"):
            return redirect(url_for('home'))
        else:
            return render_template("first_page.html")
    else:
        return render_template("first_page.html")

@app.route('/form', methods=['POST'])
def form():
    
    Name = request.form.get('nombre')
    Grado = request.form.get('grado')
    Email = request.form.get('correo')
    Message = request.form.get('mensaje')
    if Name != None or Email != None or Message != None:
        message = ("Hola soy " + Name + ", de grado " + Grado +"\n" +"Mi correo es: " + Email +"\n" + Message)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login("banco.de.ovas.gnf@gmail.com", "bfkbeqnvjgdsofpf")
            server.sendmail(Email, "banco.de.ovas.gnf@gmail.com", message)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('contact'))

@app.route('/first_page')
def home():
    return render_template('index.html')


@app.route('/recomendados')
def appsrecomendadas():
    return render_template('appsrecomendadas.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Informatica_tecnologia')
def teninformatica():
    return render_template('informatica.html')


@app.route('/Prae')
def Prae():
    return render_template('prae.html')


@app.route('/6')
def six():
    return render_template('6.html')


@app.route('/6/Biologia_Quimica')
def sixbiologia():
    return render_template('6biologia.html')


@app.route('/6/Sociales_integradas')
def sixhistoria():
    return render_template('6historia.html')


@app.route('/6/Español')
def sixepanol():
    return render_template('6epanol.html')


@app.route('/6/Filosofia')
def sixfilosofia():
    return render_template('6filosofia.html')


@app.route('/7')
def seven():
    return render_template('7.html')


@app.route('/7/Biologia_Quimica')
def sevenbiologia():
    return render_template('7biologia.html')


@app.route('/7/Sociales_integradas')
def sevenhistoria():
    return render_template('7historia.html')


@app.route('/7/Español')
def sevenepanol():
    return render_template('7epanol.html')


@app.route('/7/Filosofia')
def sevenfilosofia():
    return render_template('7filosofia.html')


@app.route('/8')
def eight():
    return render_template('8.html')


@app.route('/8/Biologia_Quimica')
def eightbiologia():
    return render_template('8biologia.html')


@app.route('/8/Sociales_integradas')
def eighthistoria():
    return render_template('8historia.html')


@app.route('/8/Español')
def eightepanol():
    return render_template('8epanol.html')


@app.route('/8/Filosofia')
def eightfilosofia():
    return render_template('8filosofia.html')


@app.route('/9')
def nine():
    return render_template('9.html')


@app.route('/9/Biologia_Quimica')
def ninebiologia():
    return render_template('9biologia.html')


@app.route('/9/Sociales_integradas')
def ninehistoria():
    return render_template('9historia.html')


@app.route('/9/Español')
def nineepanol():
    return render_template('9epanol.html')


@app.route('/9/Filosofia')
def ninefilosofia():
    return render_template('9filosofia.html')


@app.route('/10')
def ten():
    return render_template('10.html')


@app.route('/10/Biologia_Quimica')
def tenbiologia():
    return render_template('10biologia.html')


@app.route('/10/Sociales_integradas')
def tenhistoria():
    return render_template('10historia.html')


@app.route('/10/Español')
def tenepanol():
    return render_template('10epanol.html')


@app.route('/10/Filosofia')
def tenfilosofia():
    return render_template('10filosofia.html')


@app.route('/11')
def eleven():
    return render_template('11.html')


@app.route('/11/Biologia_Quimica')
def elevenbiologia():
    return render_template('11biologia.html')


@app.route('/11/Sociales_integradas')
def elevenhistoria():
    return render_template('11historia.html')


@app.route('/11/Español')
def elevenepanol():
    return render_template('11epanol.html')


@app.route('/11/Filosofia')
def elevenfilosofia():
    return render_template('11filosofia.html')

@app.route('/11/Metodologia')
def elevenmeto():
    return render_template('11metodologia.html')


if __name__ == "__main__":
    app.run(debug=True)
