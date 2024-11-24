from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://tech0-gen-8-step3-testapp-node2-20.azurewebsites.net"}})  # CORS設定を更新

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Flask start!'})

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message='Hello World by Flask')

@app.route('/api/multiply/<int:id>', methods=['GET'])
def multiply(id):
    print("multiply")
    # idの2倍の数を計算
    doubled_value = id * 2
    return jsonify({"doubled_value": doubled_value})

@app.route('/api/echo', methods=['POST'])
def echo():
    print("echo")
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # 'message' プロパティが含まれていることを確認
    message = data.get('message', 'No message provided')
    return jsonify({"message": f"echo: {message}"})

if __name__ == '__main__':
    app.run(debug=True)

# マーカーのデータを返すエンドポイント
@app.route('/api/markers', methods=['GET'])
def get_markers():
    markers = [
        {"lat": 35.6895, "lng": 139.6917},  # 東京
        {"lat": 34.0522, "lng": -118.2437},  # ロサンゼルス
        {"lat": 51.5074, "lng": -0.1278},    # ロンドン
    ]
    return jsonify(markers)

if __name__ == '__main__':
# 環境変数 PORT を取得(デフォルトは 8000)
    port = int(os.environ.get('PORT', 8080))
# デバッグモードをローカル環境では有効に、本番では無効に app.run(host='0.0.0.0', port=port, debug=False)
    app.run(host='0.0.0.0',port=port,debug=False)
