from flask import Blueprint, render_template, abort
from modules.models import Property   # IMPORTANT IMPORT

commercial_bp = Blueprint(
    "commercial",
    __name__,
    template_folder="../../templates"
)

# -----------------------------
# COMMERCIAL LIST PAGE
# -----------------------------
@commercial_bp.route("/commercial")
def commercial():
    properties = Property.query.filter_by(category="Commercial").all()
    return render_template("commercial.html", properties=properties)


# -----------------------------
# COMMERCIAL PROPERTY DETAILS
# -----------------------------
@commercial_bp.route("/commercial/<id>")
def commercial_details(id):
    property_data = Property.query.get_or_404(id)

    return render_template(
        "buyer/property_details.html",
        property=property_data
    )
