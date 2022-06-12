from crypt import methods
from pickle import TRUE
from flask import Flask


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "kire bokachoda haaa kr boro kore"




if __name__=="__main__":
    app.run(debug=TRUE)

