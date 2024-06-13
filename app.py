from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# 假定Excel文件和本Python脚本在同一目录下
# 假定第一列包含电话号码前7位，列名为phone
# 确定Excel文件名和路径
excel_file = 'phones.csv'
df = pd.read_csv(excel_file,dtype=str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        phone = request.form['phone'].strip()
        phone = phone[:7]
        row = df[df['phone'] == phone]
        if not row.empty:
            data = row.to_dict(orient='records')[0]
            return render_template('page1.html', data=data, phone=phone)
        else:
            return render_template('page1.html', error="没有找到对应的手机号段信息。")
    else:
        return render_template('page1.html')

if __name__ == '__main__':
    app.run(debug=True)