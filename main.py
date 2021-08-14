from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}

# @는 바로 아래 있는 함수를 찾게된다
# 기본 주소에 괄호안의 문자를 입력하면 @이 바로 아래 있는 함수를 찾아서
# 해당 기능을 동작하게 되는 원리
@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
          jobs = existingJobs
        else:
          jobs = get_jobs(word)
          db[word] = jobs
    else:
        return redirect('/')
    return render_template('report.html',        searchingBy=word,
      resultsNumber=len(jobs),
      jobs=jobs
    )


# /contact 로 접속 요청이 들어오면
# 파이썬이 아~ 바로 아래있는 함수 contact를 실행하면 되겠구나~
# 라고 생각하는것임
# @app.route("/<username>")
# def contact(username):
#   return

  

app.run(host="0.0.0.0")