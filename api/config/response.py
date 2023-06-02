from flask import jsonify
 
def response(error = "", data = "", status = 200):
    return jsonify({
        "error" : error,
        "data" : data,
        "status" : status
    })