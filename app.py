from flask import Flask, render_template, abort
from data import platforms, combosDuos, combosTrios

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html",platforms=platforms, combosDuos=combosDuos, combosTrios=combosTrios) 

@app.route("/detalle/<tipo>/<int:item_id>")
def detalle(tipo, item_id):
    """
    tipo: 'platform' o 'combo'
    item_id: índice en la lista
    """
    if tipo == 'platform':
        lista = platforms
        
    elif tipo == 'combosDuo':
        lista = combosDuos
        
    elif tipo == 'combotres':
        lista = combosTrios
       
    else:
        abort(404)

    if item_id < 0 or item_id >= len(lista):
        abort(404)

    try:
        item = lista[item_id]
    except IndexError:
        abort(404)
    
    relacionados = [
        p for i, p in enumerate(lista) if i != item_id
    ]

    return render_template("detalle.html", item=item,relacionados=relacionados,tipo=tipo)

@app.route("/quienesomos")
def quienesomos():
    return render_template("quienesomos.html") 

if __name__ == "__main__":
    app.run(debug=True)