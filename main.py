# guess the secret number - web app
import random
from flask import Flask, render_template, request, make_response


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    number = request.cookies.get("number")

    response = make_response(render_template("index.html"))
    if not number:
        new_number = random.randint(1, 30)
        response.set_cookie("number", str(new_number))

    return response

@app.route("/game", methods=["POST"])
def game():
    guess = int(request.form.get("guess"))
    number = int(request.cookies.get("number"))

    if guess == number:
        message = "Correct! The secret number is {0}".format(str(number))
        response = make_response(render_template("game.html", message=message))
        response.set_cookie("number", str(random.randint(1, 30)))
        response.set_cookie("number", expires=0)
        return response
    elif guess > number:
        message = "Wrong! Try something smaller."
        return render_template("game.html", message=message)
    elif guess < number:
        message = "Wrong! Try something bigger."
        return render_template("game.html", message=message)

    return render_template("game.html")

if __name__=="__main__":
    app.run()
