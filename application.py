from flask import Flask, render_template, request

app = Flask(__name__)
app.config[...] = database typeof
db = ...(app)...

# Database model...

# Set up homepage at index.html

if __name__ == '__main__':
    app.debug = True
    app.run()