from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello(): return 'Book API działa'

if __name__ == '__main__': app.run()