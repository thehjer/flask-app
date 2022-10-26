#My first applications
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder = 'templates')

import mysql.connector
mydb=mysql.connector.connect(    
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
book_list=[]
mycursor=mydb.cursor()

def get_allbooks():
    global book_list
    mycursor.execute("SELECT * FROM book")
    myresult=mycursor.fetchall()
    book_list=[]
    for x in myresult:
        book_list.append(x[1:])

    print(book_list)
# lists=[["thehjer","abdul"],["karna","arav"]]
# book_list=[["Harry Potter","Jk Rowling","August 24th"],
#                 ["The Hulk","Russo Brothers","July 25th"]]


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add')
def your_url():
    get_allbooks()
    return render_template('add.html',bk_list=book_list)


@app.route('/search',methods=['GET','POST'])
def search_url():
    global book_list
    get_allbooks()
    if request.method=='POST':
        book=request.form.get('book')
        print(book)
        win=True
        for i in range(len(book_list)):
            win=True
            for j in book_list[i]:
                if book_list[i][0]!=book:
                    win=False
            if win==True:
                return('The book is availabale')
        else:
            return('The book is unavailabale')
            
        # return render_template("display.html",bk_list=book_list)
    return render_template('search.html')

@app.route('/remove',methods=['GET','POST'])
def remove_url():
    global book_list
    get_allbooks()
    if request.method=='POST':
        l=[]
        name=request.form.get('book')
        print(name)
        win=True
        for i in range(len(book_list)):
            win=True
            for j in book_list[i]:
                if book_list[i][1]==name:
                    win=False
                    
            if win==True:
                l.append(book_list[i])
        book_list=l
        mycursor = mydb.cursor()
        sql = "DELETE FROM book(author)  VALUES(%s,)"
        adr = (name)

        mycursor.execute(sql,adr)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")        
        return render_template("display.html",bk_list=book_list)
    return render_template("remove.html")

@app.route('/display',methods=['GET','POST'])
def display_url():
    get_allbooks()
    if request.method=='POST':
        title=request.form.get('title')
        print(title)
        author=request.form.get("author")
        print(author)
        date=request.form.get("date")
        print(date)
        sql="INSERT INTO book(title,author,date) VALUES(%s,%s,%s)"
        val=[title,author,date]
        mycursor.execute(sql,val)
        mydb.commit()
        
    get_allbooks()
    return render_template("display.html",bk_list=book_list)  
 
@app.route('/login')
def login_url():
    return render_template("login.html")

@app.route('/contact')
def contact_url():
    return render_template("contact.html")

@app.route('/upload')
def upload_file():
    get_allbooks()
    return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
    global book_list
    # get_allbooks()
    if request.method == 'POST':
        f = request.files['file'] 
        f.save(secure_filename(f.filename))
        print(f)
        for l in f:
            l=l.strip()
            l=l.split(',')
            book_list.append(l)
        mycursor=mydb.cursor()
        sql="INSERT INTO book(title,author,date) VALUES(%s,%s,%s)"
        for book in book_list:
            mycursor.execute(sql,book)
            print(mycursor.rowcount,"record inserted")
        mydb.commit() 
    # get_allbooks()  
    return render_template("display.html",bk_list=book_list)
if (__name__) == '__main__':
    app.run(host="0.0.0.0")
 