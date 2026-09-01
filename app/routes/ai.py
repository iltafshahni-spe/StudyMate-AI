
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from app import db
from app.models import Chat
from app.services.ai_services import ask_ai


ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/chat", methods=["GET", "POST"])
def chat():

    if "id" not in session:
        return redirect(url_for("auth.login"))

    answer = None

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:
            flash("Please enter a question.", "error")

            chats = Chat.query.filter_by(user_id=session["id"]).all()

            return render_template(
                "chat.html",
                chats=chats,
                answer=None)

        answer = ask_ai(question)

        new_chat = Chat(
            user_id=session["id"],
            question=question,
            answer=answer)

        db.session.add(new_chat)
        db.session.commit()

    chats = Chat.query.filter_by(
        user_id=session["id"]).all()

    return render_template(
        "chat.html",
        chats=chats,
        answer=answer)

