import boto3  # aws와 연동하기 위한 패키지
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')  # index.html을 이용해서 파일 업로드

@app.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file']  # 업로드할 파일(html에서 파일명을 가져올 예정)
    s3 = boto3.client('s3')  # s3와 연동
    s3.put_object(  # 파일 업로드를 위한 메소드
        ACL="public-read",
        Bucket="profoundsea25v00",
        Body=file,
        Key=file.filename,
        ContentType=file.content_type)  # 파일 확장자
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run()