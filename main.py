
from flask import *  

app = Flask(__name__) 

def get_dollar_rate():
    return {'rate': 5.20}

@app.route('/dollar_today',methods = ['GET'])  
def dollar_today(): 
    try:
        rate = get_dollar_rate()
        return rate
    except:
        return jsonify({
            "success":  False,
            "error": 404,
            "message": "Resource not found"
        }), 404
        
@app.route('/',methods = ['GET'])  
def home(): 
    msg = {"msg":"This is a company resourse for money"}
    return msg
 
if __name__ =='__main__':  
    app.run(debug=True,port=8080)


