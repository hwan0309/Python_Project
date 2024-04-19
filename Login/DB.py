import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='seungheeui-MacBookAir.local',  # 호스트 주소
    user='root',  # 사용자 이름
    password='wlghks12',  # 비밀번호
    db='test04',  # 데이터베이스 이름
    charset='utf8'  # 문자 인코딩
)

try:
    with conn.cursor() as cursor:
        # INSERT 문 실행을 위한 SQL 쿼리
        sql = "INSERT INTO city (name, countryCode, district, population) VALUES (%s, %s, %s, %s)"
        # INSERT할 데이터: 튜플의 리스트
        cities = [
            ('test 01', 'KOR', 'test 011', 10000000),
            ('test 02', 'KOR', 'test 021', 20000000),
            ('test 03', 'KOR', 'test 031', 30000000),
            ('test 04', 'KOR', 'test 041', 40000000)
        ]
        # 여러 데이터를 한 번에 데이터베이스에 삽입
        cursor.executemany(sql, cities)

    # 변경사항 커밋
    conn.commit()
finally:
    # 데이터베이스 연결 종료
    conn.close()


#     #### created ciy table view
# try:
#     # 커서 생성
#     with conn.cursor() as cursor:
#         # SQL 쿼리 실행
#         sql = "SELECT * FROM city"
#         cursor.execute(sql)
#         # 결과 모두 가져오기
#         result = cursor.fetchall()
#         # 결과 출력
#         for row in result:
#             print(row)
# finally:
#     # 데이터베이스 연결 닫기
#     conn.close()