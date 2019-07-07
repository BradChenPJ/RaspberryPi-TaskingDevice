from flask import Flask, request
import json
from grovepi import *
from grove_rgb_lcd import *

app = Flask(__name__)
@app.route("/task", methods = ["POST"])
def task():
    print(request.is_json)
    content = request.get_json()
    print(content)
    rn = content["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["rn"]
    ob = rn[:11]
    if ob == "Observation":
        result = json.loads(content["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])["result"]
        if float(result) > 30 and float(result) < 50:
            setRGB(255, 181, 0)
            setText("Waring!Temp>30")
            
        elif float(result)>= 50:
            setRGB(255,0,0)
            setText("Waring!Temp>50")
            
    else:
        con = content["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"]
        setRGB(0, 255, 0)
        setText(con)
    return "ok"
if __name__ == "__main__":
    app.run(host = "192.168.1.103",port = "8484",debug=True)
    



