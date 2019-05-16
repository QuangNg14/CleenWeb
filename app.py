# -_- python 2.7.15 zz
# tải python 3.7.0 về cài đi e

from flask import Flask, render_template, request, redirect, url_for
from models.classModels import *
from mlab import *
import math
connect()
app = Flask(__name__)

record_per_page = 8 

@app.route('/test', methods = ["GET","POST"])
def test():
    if request.method == "GET":
        dataGet_post = Post.objects() 
        return render_template('homepage/test.html', data = dataGet_post)

# HomePage
@app.route('/home',methods = ["GET","POST"])
def home():
    if request.method == "GET":
        page_nb = 1 
        offset = (page_nb - 1) * record_per_page
        allPost = Post.objects()
        paginationLength = math.ceil(len(allPost) / 8)
        dataGet_post = Post.objects.skip( offset ).limit( record_per_page) #no chi lay 8 thang
        return render_template('homepage/home.html', data = dataGet_post, paginationLength = paginationLength)
    elif request.method == "POST":
             form = request.form
                # type cua input
             typePost = form["type"]
             if typePost == "signupEmail":
                     email = form["emailSignUp"]
                     newemail = Email(email = email)
                     newemail.save()
                #      Tạo model
                #  save model
                     print(email)
                     return redirect(url_for("cleenproject"))

@app.route('/',methods = ['GET','POST'])
def cleenproject():
    if request.method == "GET":
        dataGet_post = Post.objects()
        return render_template('homepage/cleenproject_home.html', data = dataGet_post)

@app.route('/home/<number>',methods = ["GET","POST"])
def home_page(number):
    if request.method == "GET":
        print(number)
        number = int(number)
        page_nb = number
        offset = (page_nb - 1) * record_per_page
        allPost = Post.objects()
        paginationLength = math.ceil(len(allPost) / 8)
        dataGet_post = Post.objects.skip( offset ).limit( record_per_page )
        return render_template('homepage/home.html', data = dataGet_post, paginationLength = paginationLength)

@app.route('/news/<idNew>', methods = ["GET", "POST"])
def new(idNew):
    if request.method == "GET":
        dataGet_post = Post.objects()
        new = Post.objects.get(id=idNew)
        return render_template('homepage/each_new.html', new = new, data = dataGet_post)

@app.route('/qa', methods = ["GET", "POST"])
def qa():
        if request.method == "GET":
                dataGet_post = Post.objects()
                return render_template('homepage/qa.html',data = dataGet_post)


@app.route('/index', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        dataGet_post = Post.objects()   
        return render_template('homepage/index.html', data = dataGet_post)


@app.route('/pending', methods = ["GET", "POST"])
def pending():
    if request.method == "GET":
        dataGet_post = Post.objects()   
        return render_template('homepage/pending.html', data = dataGet_post)

@app.route('/duyet/<userId>', methods = ["GET", "POST"])
def duyet(userId):
        if request.method == "GET":
                chooseUser = Post.objects.get(id=userId)
                chooseUser.update(set__status = True)
                return redirect(url_for("pending"))

@app.route('/add',methods = ["GET","POST"])
def add():
    if request.method == "GET": 
        dataGet_post = Post.objects()
        return render_template('action/postCreate.html', data = dataGet_post) # 1 list cac data
    elif request.method == "POST": 
        # lay data sau khi nhap vao o form 
        form = request.form 
        title = form["title"] 
        author = form["author"]
        picture_link = form["picture_link"]
        content = form["content"]
        authorize_code = form["authorize_code"]
        content_editor = form["content_editor"]
        if authorize_code == "abc123":
                postNewPost = Post(title = title, author = author,picture_link=picture_link, content = content, status=False,authorize_code = authorize_code)
                #dùng classModels để lưu lại dữ liệu 
                print(content_editor)
                postNewPost.save()
                # cho lên database trên mongoengine
                dataGet_post = Post.objects() 
                # return render_template('result.html', data = dataGet_person)
                return redirect(url_for("pending")) #chay method GET cua def index() o ben tren 
        else:
                return redirect(url_for("add"))
                                            #url for la trỏ đến hàm def 


#  In ra và hiện 1 cái nút dẫn đến thằng create
@app.route('/question',methods = ["GET","POST"])
def question():
        if request.method == "GET":
                questionGet = FAQ.objects()
                return render_template('homepage/qa.html',data = questionGet)
        if request.method == "POST":
                form = request.form
                # Search
                typeForm = form["search"]
                if typeForm == "1":
                        stringSearch = form["searchQuestion"]
                        questionSearch = FAQ.objects(question__contains=stringSearch)
                        return render_template('homepage/qa.html',data = questionSearch)

# Tạo câu hỏi và khi submit thì quay lại trang list câu hỏi
@app.route('/question/create', methods = ["GET", "POST"])
def createQuestion():
        if request.method == "GET":
                questionGet = FAQ.objects()
                return render_template('homepage/question.html',data = questionGet) # Trang form để tạo câu hỏi
        elif request.method == "POST":
                form = request.form #lấy cái form từ html của indextest
                question = form["question"]
                newquestion = FAQ(question = question, answer = '')
                newquestion.save()
                questionGet = FAQ.objects()
                return redirect(url_for('question'))



# Khi mình bấm chi tiết câu hỏi thì sẽ vào thằng này
@app.route('/qanda/<questionId>',methods = ["GET","POST"])
def qanda(questionId):
        if request.method == "GET": 
                questionGet = FAQ.objects.get(id=questionId)
                return render_template('homepage/qa.html', currentQuestion = questionGet)
        elif request.method == "POST": #post = submit #xu ly nut submit 
        # HTML -> SERVER
                form = request.form 
                question = form["question"]
                answer = form["answer"]
        #SERVER -> DATABASE
                questionGet = FAQ.objects.get(id=questionId)
                questionGet.update(set__answer = answer)
                return redirect(url_for("answer"))

@app.route('/answer/<questionId>', methods = ["GET", "POST"])
def answer(questionId):
        if request.method == "GET":
                questionGet = FAQ.objects()
                questionGet = FAQ.objects.get(id=questionId)
                return render_template('homepage/answer.html', data = questionGet)
        elif request.method == "POST":
                form = request.form #lấy cái form từ html của indextest
                answer = form["answer"]
                code = form["code"]
                questionGet = FAQ.objects.get(id=questionId)
                if code == "abc123":
                        questionGet = questionGet.update(set__answer = answer)
                        return redirect(url_for('question'))
                else: 
                        return redirect(url_for("answer", questionId = questionId))

@app.route('/donation',methods=["GET","POST"])
def donation():
        if request.method == "GET":
                questionGet = FAQ.objects()
                return render_template('homepage/donation.html', data = questionGet)

# Thằng hỏi:
#         HTML có form Đặt câu hỏi và nút submit

# Thằng trả lời:
#         Hiện ra câu hỏi
#         ở dưới:
#         HTML có form trả lời và nút submit

# E tạo 1 trang FAQ:
# Trong trang FAQ sẽ có 1 nút gọi là nút đặt câu hỏi
# khi ấn vào thì sẽ sang 1 trang mới có ô đặt câu hỏi và 1 nút submit

# FAQ - hiện ra 1 list tất cả các câu hỏi
# Nếu click vào chi tiết của 1 câu hỏi -> sang trang chi tiết câu hỏi đấy (
#         trang này thì sẽ hiện câu hỏi và ô nhập câu trả lời và 1 nút submit
# )

@app.route('/editUser/<userId>',methods = ["GET","POST"])
def editUser(userId):
    if request.method == "GET":
        userGet = Post.objects.get(id=userId)
        return render_template("action/postEdit.html", currentUser = userGet) #data cua 1 thang user

    elif request.method == "POST": #post = submit #xu ly nut submit 
        # HTML -> SERVER
        form = request.form #lấy cái form từ html của indextest
        title = form["title"] #lấy dữ liệu người dùng nhập vào 
        author = form["author"]
        picture_link = form["picture_link"]
        content = form["content"]

        #SERVER -> DATABASE
        userGet = Post.objects.get(id=userId)
        userGet.update(set__title = title, set__author = author, set__picture_link = picture_link , set__content = content)
        return redirect(url_for("index"))

@app.route('/deleteUser/<userId>',methods = ["GET","POST"])
def deleteUser(userId): #userId tu mlab
    userGet = Post.objects.get(id=userId)
    userGet.delete()  #xoa dong vua bam 
    return redirect(url_for("pending"))

@app.route('/email', methods = ["GET","POST"])
def email():
        if request.method == "GET":
                questionGet = FAQ.objects()
                return render_template("homepage/cleenproject_home.html", data = questionGet)
        elif request.method == "POST":
                form = request.form
                email = form["email"]
                newemail = Email(email = email)
                newemail.save()
                return redirect(url_for('cleenproject'))

if __name__ == '__main__':
  app.run(port=8000, debug=True)