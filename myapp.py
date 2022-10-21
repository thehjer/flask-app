#My first applications
from flask import Flask, render_template,request

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
        book=request.form.get('book')
        print(book)
        win=True
        for i in range(len(book_list)):
            win=True
            for j in book_list[i]:
                if book_list[i][1]==book:
                    win=False
                    
            if win==True:
                l.append(book_list[i])
        book_list=l                
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

if (__name__) == '__main__':
    app.run()
 