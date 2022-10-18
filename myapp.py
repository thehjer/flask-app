#My first applications
from flask import Flask, render_template,request

app = Flask(__name__,template_folder = 'templates')


# lists=[["thehjer","abdul"],["karna","arav"]]
students_info=[["Harry Potter","Jk Rowling","August 24th"],
                ["The Hulk","Russo Brothers","July 25th"]]


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add')
def your_url():
    return render_template('add.html',st_list=students_info)


@app.route('/search',methods=['GET','POST'])
def search_url():
    global students_info
    if request.method=='POST':
        book=request.form.get('book')
        print(book)
        win=True
        for i in range(len(students_info)):
            win=True
            for j in students_info[i]:
                if students_info[i][0]!=book:
                    win=False
            if win==True:
                return('The book is availabale')
        else:
            return('The book is unavailabale')
            
        # return render_template("display.html",st_list=students_info)
    return render_template('search.html')

@app.route('/remove',methods=['GET','POST'])
def remove_url():
    global students_info
    if request.method=='POST':
        l=[]
        book=request.form.get('book')
        print(book)
        win=True
        for i in range(len(students_info)):
            win=True
            for j in students_info[i]:
                if students_info[i][1]==book:
                    win=False
                    
            if win==True:
                l.append(students_info[i])
        students_info=l                
        return render_template("display.html",st_list=students_info)
    return render_template("remove.html")

@app.route('/display',methods=['GET','POST'])
def display_url():
    if request.method=='POST':
        title=request.form.get('title')
        print(title)
        author=request.form.get("author")
        print(author)
        date=request.form.get("date")
        print(date)
        students_info.append([title,author,date])
    return render_template("display.html",st_list=students_info)  
 
@app.route('/login')
def login_url():
    return render_template("login.html")

@app.route('/contact')
def contact_url():
    return render_template("contact.html")

if (__name__) == '__main__':
    app.run()
 