from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    nome = 'Betão Chico Buarque'
    stress1 = 'Eu querendo uma carreira TOP antes de conhecer a BLUE.'
    stress2 = 'Eu na carreira DEV depois da BLUE.' 
    bolado = True
    imagem1 = "static\img\Chico_Bolado.png"
    imagem2 = "static\img\Chico_Deboa.png"
    resultado1 = "Bad Total... boladasso."
    resultado2 = "Muito de boa na lagoa!"

    return render_template(
        "index.html",
        nome = nome,
        bolado = bolado,
        stress1 = stress1,
        stress2 = stress2,
        imagem1 = imagem1,
        imagem2 = imagem2,
        resultado1 = resultado1,
        resultado2 = resultado2
)

if __name__ == "__main__":
    app.run(debug=True)