import argparse
from bloomberg import Bloomberg
from investing import Investing
from mining import Mining

parser = argparse.ArgumentParser()

parser.add_argument("--type", dest="type", action="store", help="크롤러 종류를 선택하세요. (bloomberg, investing, mining)")
parser.add_argument("--date", dest="date", action="store", help="년-월 (2022-09)")
parser.add_argument("--page", dest="page", action="store", help="최대 10 페이지인 경우.(10)")

args = parser.parse_args()

if __name__ == "__main__":
    if args.type == "bloomberg":
        Bloomberg().get_links(args.date).download()
    elif args.type == "investing":
        Investing(args.page).get_links().download()
    elif args.type == "mining":
        Mining(args.page).get_links().download()
    else:
        raise Exception("지원하지 않는 type입니다. (bloomberg, investing, mining) 중 선택")
