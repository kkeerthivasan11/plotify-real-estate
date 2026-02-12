from flask import Blueprint, render_template
from modules.models import Property   # <-- correct import

buy_bp = Blueprint(
    "buy",
    __name__,
    template_folder="../../templates"
)

# =========================
# BUY PAGE
# =========================
@buy_bp.route("/buy")
def buy():

    properties = Property.query.filter_by(category="Sell").all()


    return render_template(
        "buyer/buy.html",
        properties=properties,
        logged_in=False
    )

# =========================
# PROPERTY DETAILS PAGE
# =========================
@buy_bp.route("/property/<id>")
def property_details(id):

    prop = Property.query.get(id)

    if not prop:
        return "Property not found"

    return render_template(
        "buyer/property_details.html",
        property=prop
    )
