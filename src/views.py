from .models import CodeBlock, User
from .extensions import app, db, socketio
from flask_socketio import emit
from flask import jsonify, request


# Route to get all code blocks
@app.route("/get_codeblocks", methods=["GET"])
def get_codeblocks():
    codeblocks = CodeBlock.query.all()
    codeblocks_data = [block.as_dict() for block in codeblocks]
    return jsonify(data=codeblocks_data)


@app.route("/user_info", methods=["GET", "POST"])
def user_info():
    user = User.query.first()

    if request.method == "GET":
        return jsonify({"isMentor": user.mentor})

    else:
        data = request.get_json()
        user.mentor = data.get("isMentor")
        db.session.commit()
        return jsonify({"success": "User mentor status updated"})


# Handle client connection event
@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("server_message", {"message": "Welcome to the online code editor!"})


# Socket event to update an existing code block
@socketio.on("update_codeblock")
def update_codeblock(data):
    if data.get("codeblock_id") and data.get("code"):
        codeblock_id = data["codeblock_id"]
        codeblock = CodeBlock.query.get_or_404(codeblock_id)
        codeblock.code = data["code"]
        db.session.commit()

        emit("updated_codeblock", codeblock.as_dict(), broadcast=True)
