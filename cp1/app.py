from flask import Flask, request, url_for, render_template, redirect
from des import encryption, decryption

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html')


@app.route("/encryption-page")
def encryption_page():
    return render_template('encryption.html')


@app.route("/decryption-page")
def decryption_page():
    return render_template('decryption.html')


@app.route("/decrypted", methods=['POST'])
def decryption_inputs():
    if request.method == "POST":
        if request.form['ciphertext'] != "" and request.form['key'] != "":
            cipher_text=request.form['ciphertext']
            key = request.form['key']
            decrypted_text=decryption(cipher_text,key)
            return render_template('decryption-print.html', ciphertext=decrypted_text, key=key)
        else:
            return redirect(url_for('main_page'))


@app.route("/encrypted", methods=["POST"])
def encrypted():
    if request.method == "POST":
        if request.form['plaintext'] != "" and request.form['key'] != "":
            plain_text = request.form['plaintext']
            key = request.form['key']
            cipher_text=encryption(plain_text,key)
            return render_template('encryption-print.html', plaintext=plain_text, ciphertext=cipher_text)
        else:
            return redirect(url_for('main_page'))


if __name__ == '__main__':
    app.run(debug=True)
