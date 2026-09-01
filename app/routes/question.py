
from flask import (
    Blueprint,
    session,
    request,
    render_template,
    redirect,
    url_for,
    flash
)

from app.services.ai_services import ask_ai


question_bp = Blueprint("question", __name__)


@question_bp.route("/ai-chat", methods=["GET", "POST"])
def ai_chat():

    if "id" not in session:
        return redirect(url_for("auth.login"))

    response = None

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:
            flash("Please enter your question.", "error")

            return render_template(
                "chat.html",
                response=None
            )

        response = ask_ai(question)

    return render_template(
        "chat.html",
        response=response
    )
