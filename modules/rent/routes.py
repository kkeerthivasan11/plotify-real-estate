from flask import Blueprint, render_template
from modules.models import Property

rent_bp = Blueprint(
    "rent",
    __name__,
    template_folder="../../templates"
)

# =========================
# RENT PAGE
# =========================
@rent_bp.route("/rent")
def rent():

    properties = Property.query.filter_by(
        category="Rent",
        verified=True
    ).all()

    return render_template(
        "rent.html",
        properties=properties
    )

# =========================
# RENT PROPERTY DETAILS
# =========================
@rent_bp.route("/rent/<id>")
def rent_details(id):

    prop = Property.query.get(id)

    if not prop:
        return "Property not found"

    return render_template(
        "buyer/property_details.html",
        property=prop
    )
