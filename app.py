from flask import Flask, render_template_string, request

app = Flask(__name__)

# Initialize count
count = 0

# HTML template for the counter app
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .counter {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .buttons {
            margin-top: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Counter App</h1>
    <div class="counter">
        <span>{{ count }}</span>
    </div>
    <div class="buttons">
        <form method="POST" action="/increment">
            <button type="submit">Increment</button>
        </form>
        <form method="POST" action="/decrement">
            <button type="submit">Decrement</button>
        </form>
        <form method="POST" action="/reset">
            <button type="submit">Reset</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    global count
    return render_template_string(HTML_TEMPLATE, count=count)

@app.route('/increment', methods=['POST'])
def increment():
    global count
    count += 1
    return render_template_string(HTML_TEMPLATE, count=count)

@app.route('/decrement', methods=['POST'])
def decrement():
    global count
    count -= 1
    return render_template_string(HTML_TEMPLATE, count=count)

@app.route('/reset', methods=['POST'])
def reset():
    global count
    count = 0
    return render_template_string(HTML_TEMPLATE, count=count)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
