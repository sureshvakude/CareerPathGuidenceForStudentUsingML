from flask import Flask,render_template,request,redirect
import mysql.connector
from predict import PredictPath

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="careerguide"
    )
mycursor = mydb.cursor()

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signUp',methods=['GET','POST'])
def signupNewUser():
	if(request.method=='POST'):
		name = request.form.get('name')
		email = request.form.get('email')
		username = request.form.get('username')
		password = request.form.get('password')
		sql = "INSERT INTO student_info (name, email,username,password) VALUES (%s, %s,%s, %s)"
		val = (name,email,username,password)
		mycursor.execute(sql, val)
		mydb.commit()
		return redirect('/')
	return render_template('SignUpPage.html')

@app.route('/Login',methods=['GET','POST'])
def loginpage():
	if(request.method=='POST'):
		email = request.form.get('email')
		password = request.form.get('password')
		mycursor.execute(f'SELECT * FROM student_info where email=%s and password=%s',(email,password))
		global studentdetail
		studentdetail = mycursor.fetchall()
		if(studentdetail!=[]):
			return render_template('Loginhome.html',name=studentdetail[0][3])
	return render_template('LoginPage.html')


maths10ans = ["7","angle of elevation","negative","1/3","75 degree","1350","22","10","28","17/5"]
eng10ans = ["False","POK","LXMB","JTT","True","2362.5","1","186","170","False"]
sci10ans = ["A burning splinter","white","Baking Soda","Oxalic acid","washing soda","Crop field","Cowdung"\
	    ,"sulphur and nitrogen","Chloro fluoru carbon","5th June"]
log10ans = ["Snake","21","15264","24","EIGHT","Twig","Ocean","5","5","True"]
@app.route('/aptitude-test/10th-student/notice',methods=['GET','POST'])
def questionapti():
	return render_template('notice.html')

@app.route('/aptitude-test/10-student/mathspaper',methods=['GET','POST'])
def mathsPaper():
	global mcount
	mcount=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(maths10ans)):
			if(maths10ans[i]==answer[i]):
				mcount+=1
		return render_template('McqEngQuestionPaper10th.html')
	return render_template('McqMathQuestionPaper10th.html')

@app.route('/aptitude-test/10-student/engpaper',methods=['GET','POST'])
def engPaper():
	global ecount
	ecount=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(eng10ans)):
			if(eng10ans[i]==answer[i]):
				ecount+=1
		return render_template('McqSciQuestionPaper10th.html')
	return redirect('/')
	
@app.route('/aptitude-test/10-student/scipaper',methods=['GET','POST'])
def sciPaper():
	global scount
	scount=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(sci10ans)):
			if(sci10ans[i]==answer[i]):
				scount+=1
		return render_template('McqlogQuestionPaper10th.html')
	return redirect('/')

@app.route('/aptitude-test/10-student/logpaper',methods=['GET','POST'])
def logPaper():
	global lcount
	lcount=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(log10ans)):
			if(log10ans[i]==answer[i]):
				lcount+=1
		return render_template('preloading.html')
	return redirect('/')

@app.route('/result/10std/student')
def result10std():
	tp = []#-----[5,6,8,2]
	tp.append(mcount)
	tp.append(ecount)
	tp.append(scount)
	tp.append(lcount)
	result = PredictPath(tp)
	result = result[0]
	if(result=='B.Ed' or result =='D.Ed' or result=='LLB' or result=='Mask Communication'):
		result = "Arts"
	elif(result=='BBA' or result=='BCOM' or result=='BCOM'):
		result = "Commerce"
	elif(result=='Software Engineering' or result=='Data Science' or result=='Engineer' or result=='software Developer'):
		result = 'diploma'
	else:
		result = "Science"
	return render_template('result10.html',result=result)

@app.route('/aptitude-test/12th-student/notice',methods=['GET','POST'])
def notice12thtest():
	return render_template('notice12.html')

@app.route('/aptitude-test/12-student/mathspaper',methods=['GET','POST'])
def maths12thpaper():
	return render_template('McqEngQuestionPaper12.html')

eng12ans = ["By practice","stopped","did you drink","I said to him, You are not working hard.",\
	    "Peter was surprised at her selection in the crew","have been steadily increasing","with tears in her eyes",\
			"Talkative","Introvert","they"]
sci12ans = ["Both (a) and (c)","Gamma rays have the least penetration power.","NAND","100110","Ice","Homogeneous,\
	     anisotropic","Lewis acid","Earthworm, sponge, leech","Ophioglossum","both (a) and (b)."]
mat12ans = ["60.66","40","5","Monday","12 years","112","7","27, 189","42","17/5"]
log12ans = ["False","POK","LXMB","JTT","True","2362.5","1","186","170","False"]

@app.route('/aptitude-test/12-student/engpaper',methods=['GET','POST'])
def aptitude12eng():
	global ecount12
	ecount12=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(eng12ans)):
			if(eng12ans[i]==answer[i]):
				ecount12+=1
		return render_template('McqsciQuestionPaper12th.html')
	
@app.route('/aptitude-test/student/scipaper-12-paper',methods=['GET','POST'])
def aptitude12sci():
	global scount12
	scount12=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(sci12ans)):
			if(sci12ans[i]==answer[i]):
				scount12+=1
		return render_template('McqmathQuestionPaper12th.html')
	
@app.route('/aptitude-test/12-student/mathspaper-test',methods=['GET','POST'])
def math12aptitude():
	global mcount12
	mcount12=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(mat12ans)):
			if(mat12ans[i]==answer[i]):
				mcount12+=1
		return render_template('McqlogQuestionPaper12th.html')
	
@app.route('/aptitude-test/12-student/logpaper',methods=['GET','POST'])
def log12aptitudetest():
	global lcount12
	lcount12=0
	if request.method=='POST':
		q1 = request.form.get('que1')
		q2 = request.form.get('que2')
		q3 = request.form.get('que3')
		q4 = request.form.get('que4')
		q5 = request.form.get('que5')
		q6 = request.form.get('que6')
		q7 = request.form.get('que7')
		q8 = request.form.get('que8')
		q9 = request.form.get('que9')
		q10 = request.form.get('que10')
		answer = []
		answer.append(q1)
		answer.append(q2)
		answer.append(q3)
		answer.append(q4)
		answer.append(q5)
		answer.append(q6)
		answer.append(q7)
		answer.append(q8)
		answer.append(q9)
		answer.append(q10)
		for i in range(len(log12ans)):
			if(log12ans[i]==answer[i]):
				lcount12+=1
		return render_template('preloading12.html')
	
@app.route('/result/12std/student')
def result12():
	tp = []
	tp.append(mcount12)
	tp.append(ecount12)
	tp.append(scount12)
	tp.append(lcount12)
	result = PredictPath(tp)
	result = result[0]
	return render_template('result12.html',result=result)

@app.route('/Careers-paths')
def career():
	return render_template('ExtraDetailsCareer.html')

@app.route('/consultation')
def consultation():
	return render_template('consultation.html')

if __name__ == '__main__':
	app.run(debug=True)
