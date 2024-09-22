import random
import requests
import flask
from flask import request,jsonify,Flask,send_file
protocolhttp = "https://"
TABLEOFWEBSITESTOCHECK = []
loadthisloop = True

while loadthisloop == True:
  loadinputty = int(input("1. for stopping this and 2. for continuing this"))
  if loadinputty == 2:
    newserver = input("What is the Address of the website you are getting your data from?")
    TABLEOFWEBSITESTOCHECK.append(newserver)
  else:
    loadthisloop = False
App = Flask(__name__)
@App.route("/getblocknum",methods=['GET'])
def getblocknum():
    URL = TABLEOFWEBSITESTOCHECK[random.randint(0,len(TABLEOFWEBSITESTOCHECK)-1)]
    blocknum = requests.get(protocolhttp+str(URL)+"/getblocknum")
    blocknum = blocknum.json()
    blocknum = blocknum["Success"]
    return jsonify(int(blocknum)),200
@App.route("/gettransactionsofablock",methods=['POST'])
def gettransactionsofablock():
    URL = TABLEOFWEBSITESTOCHECK[random.randint(0,len(TABLEOFWEBSITESTOCHECK)-1)]

    data = request.json
    blocknum = data["blocknum"]
    senddata = {"Blockamount":blocknum}
 
    newdata = requests.post(protocolhttp+str(URL)+"/getoneoftheblocks",json=senddata)
    
    print("newdata: "+str(newdata))
    newdata = newdata.json()
    print(newdata)
    newdata = newdata["Success"]
    return jsonify(dict(newdata))
@App.route("/explore",methods=['GET'])
def explore():
    output_file = "blockexplorer.html"
    return send_file(output_file)
if __name__ == "__main__":
    local_ip = "192.168.56.1"
    port = 7999
    App.run(host=local_ip, port=7999)