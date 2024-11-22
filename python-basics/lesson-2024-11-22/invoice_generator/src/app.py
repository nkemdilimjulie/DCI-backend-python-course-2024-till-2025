from datetime import date
from pathlib import Path

from flask import Flask, render_template
from src import utils

app = Flask(__name__)

FILE_PATH = str(Path(__file__).parent.parent / "invoice" / "invoice_template.xlsx")


@app.route("/")  # url for homepage
def home():
    data = utils.extract_excel_file(FILE_PATH)
    total_hours = sum(int(d[3]) for d in data)
    # render the invoice html page
    # by default, render_template looks into the templates folder
    return render_template(
        "invoice.html",
        data=data,
        total_hours=total_hours,
        **utils.get_company_info(),
        **utils.get_user_info(),
        **utils.get_invoice_header_info()
    )


if __name__ == "__main__":
    app.run(debug=True)
