# anaconda를 활용하여 가상환경 설정

conda create -n venv python = 3.9

pip install --upgrade pip
pip install playwright
playwright install

git clone "https://github.com/kimjaewon96/iitp-crawl"
pip install -r requirements.txt


# mining.com 10페이지 분량 crawling
python main.py --type mining --page 10