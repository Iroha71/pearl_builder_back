FROM python:3.7
#バイナリレイヤ下での標準出力とエラー出力を無効化
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
# appディレクトリに移動 (=cd /app)
WORKDIR /app
# requirements.txt(pipライブラリをまとめたもの)をコンテナ/appに反映
ADD requirements.txt /app
# pip install
RUN pip install -r requirements.txt
# ローカルのディレクトリをコンテナに反映
ADD . /app