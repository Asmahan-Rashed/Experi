from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

@app.route('/lang', methods=['POST'])
def addOne():
    rq = request.get_json()
    print(rq)
    return jsonify(rq)
#'Hello ' + rq.get('name ')+ rq.get('Noname')

if __name__ == '__main__':
  app.run(debug=True, port=8080) #run app on port 8080 in debug mode