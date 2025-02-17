from app.config import *

MAIN_URL = "https://flight.naver.com/"

INITIAL_STR = '''
█▀▀ █ █▄░█ █▀▄  █▀▀ █░░ █ █▀▀ █░█ ▀█▀
█▀░ █ █░▀█ █▄▀  █▀░ █▄▄ █ █▄█ █▀█ ░█░
by Youngwoo\n
'''

HELP_STR = f'''
🥇 네이버 왕복 항공권 자동 검색 ({INTERVAL}분마다)\n
🥈 사용 방법 : !항공권 [도시] [출발일] [시간대...] [도착일] [시간대...]\n
🥉 사용 예시 : !항공권 오사카 23-01-26 06-09,09-12 23-01-29 15-18,18-21
        - [인천 <-> 오사카]
        - [23년 01월 26일, 06시-09시, 09시-12시 인천 출발]
        - [23년 01월 29일, 15시-18시, 18시-21시 오사카 출발]\n
🏅 적용 가능한 [시간대]
        [ 00-06 | 06-09 | 09-12 | 12-15 | 15-18 | 18-21 | 21-00 ]\n
📄 목록 조회 : !목록
❌ 목록 삭제 : !삭제 [ID]
'''