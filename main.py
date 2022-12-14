from flask import Flask, request
import hashlib

app = Flask(__name__)

# dictionary to store hashes and messages
hash_dict = {}

@app.route('/messages', methods=['POST'])
def post_message() -> str:
    # get the message from the request
    message = request.form['message']
    
    # SHA256 hash of the message
    digest = hashlib.sha256().hexdigest()
    
    # store the message and hash in the dictionary
    hash_dict[digest] = message
    
    # return the hash
    return digest

@app.route('/messages/<hash>', methods=['GET'])
def get_message(hash : str) -> str:
    # check if the hash exists in the dictionary
    if hash in hash_dict:
        # return the message if it exists
        return hash_dict[hash]
    else:
        # return a 404 error if the hash does not exist
        return "Error: 404 Hash not found", 404

if __name__ == '__main__':
    app.run()
