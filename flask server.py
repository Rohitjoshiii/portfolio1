from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)
                                            #we can made link acc.to us to use route()
                                            #for add html file need to make folder called "temlates" and put html file into it
                                            #for add css and js file mfirst make static folder and put that files into in it
                                            #and can do whatever we want
                                     #{{ }} shows this is expression
@app.route("/h")
def simple():
     return "rohit is best"
@app.route("/rohit/joshi/website")
def rohit_insta():
    return "this is rohits insta"
@app.route("/<username>/<int:password>")
def read(username,password):
    return render_template('first.html',name=username,id=password)
@app.route("/")
def website():
    return render_template('index.html')
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')
@app.route("/works.html")
def works():
    return render_template('work.html')

@app.route("/<string:page_name>")                       # this is or dynamically for open the page
def info(page_name):
    return render_template(page_name)

@app.route("/submit_message",methods=['POST','GET'])    #  this part for submit the data on server
def send():                                             # when we submitted the information then return okk done!
    if request.method=='POST':                          # here we grab submitted data also to use request module
        data=request.form.to_dict()
        #print(data)
        #store_info(data)
        csv_info(data)


        return redirect('/thankyou.html')               # here we use redirect module because when user submit their
    else:                                               #info. on our pagwe then get thankyou from our side on that page
        return "something went wrong"                   # now with this code client submit their info. on server and
                                                        # server can access client's submitted info.
                                                        # we made server here
                                                        # but client's info. on server when we back from pycharm
                                                        #then info. will lost because this is main memory

                                                        # now we make database for storing hat info.
def store_info(client_info):                            # this function for storing the client info into file
    with open("web\database.txt" ,mode = 'a') as database:
        email=client_info['email']
        subject=client_info["subject"]
        message=client_info["message"]
        file=database.write(f'\n{email},{subject},{message}')

def csv_info(data):
    with open("database.csv",newline="",mode ="a") as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_obj=csv.writer(database2 )
        csv_obj.writerow([email,subject,message])


