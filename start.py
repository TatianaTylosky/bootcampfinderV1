from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bootcamps")
def template_test():
        return render_template('template.html', my_string="Welcome to bootcamp finder!",
                                           my_list=["General Assembly", "Flatiron", "Dev Bootcamp"])
@app.route("/bootcamps/<name>")
def bootcamp_page(name):
        return "Welcome to {}'s page!".format(name.title())

@app.route("/test")
def le_test():
        return "It's working"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
