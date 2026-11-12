from flask import Blueprint, render_template
from app.services.product_service import get_products_by_category

public_bp = Blueprint('public', __name__)

@public_bp.route("/")
def inicio():
    platforms = get_products_by_category('platform')
    combos_duos = get_products_by_category('combosDuo')
    combos_trios = get_products_by_category('combotres')
    
    return render_template(
        "inicio.html",
        platforms=platforms,
        combosDuos=combos_duos,
        combosTrios=combos_trios
    )

@public_bp.route("/quienesomos")
def quienesomos():
    return render_template("quienesomos.html")

@public_bp.route("/comofunciona")
def comofunciona():
    return render_template("comofunciona.html")

@public_bp.route("/politicas")
def politicas():
    return render_template("politicas.html")
