# 필요한 외부 라이브러리 및 패키지 불러오기
from flask import Flask, request, jsonify
import urllib.parse
import urllib.request
import json
import pdairp
from geopy.geocoders import Nominatim # geopy 모듈 (위치확인)

# flask 초기 설정
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'
 
app.run()

# 환경공단 데이터에 접근하기 위한 API키
a = pdairp.PollutionData("Xw%2FEwzmpdYhZzRl2Gh7ImRs%2BkkU%2F5JFrWAZzJmDWTgStFhfXkwA2J02LvidsMnqVLKV40imtar0WoUQmi%2FYxOg%3D%3D")


#외부 패키지 정렬

# stationinfo
class StationInfo(object):

    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/'

    def nearby(self, tm_x, tm_y, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getNearbyMsrstnList?', 'tmX=', str(tm_x), '&tmY=', str(tm_y),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json'
        ]
        url = 'https://data.go.kr'.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'stationName', 'addr', 'tm'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata

    def detail(self, addr, station_name, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getMsrstnList?', 'addr=', urllib.parse.quote(addr),
            '&stationName=', urllib.parse.quote(station_name), '&pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'addr', 'dmX', 'dmY', 'item', 'mangName',
                'map', 'oper', 'photo', 'stationName', 'vrml',
                'year'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata

    def tmcode(self, umd_name, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getTMStdrCrdnt?', 'umdName=', urllib.parse.quote(umd_name),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'sidoName', 'sggName', 'umdName', 'tmX', 'tmY'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][i][j]

        return returndata

# pollution_stats
class PollutionStats(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnStatsSvc/'

    def station(self, station_name, searchCondition, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getMsrstnAcctoLastDcsnDnsty?', 'stationName=', urllib.parse.quote(station_name),
            "&searchCondition=", searchCondition, '&pageNo=', page_no, '&numOfRows=', num_of_rows,
            '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'so2Avg', 'coAvg', 'o3Avg', 'no2Avg',
                'pm10Avg'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def period(self, searchDataTime, statArticleCondition, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getDatePollutnStatInfo?', 'searchDataTime=', searchDataTime,
            "&statArticleCondition=", urllib.parse.quote(statArticleCondition), '&pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'sidoName', 'dataTime', 'so2Avg', 'coAvg', 'o3Avg',
                'no2Avg', 'pm10Avg', 'so2Max', 'coMax', 'o3Max',
                'no2Max', 'pm10Max', 'so2Min', 'coMin', 'o3Min',
                'no2Min', 'pm10Min'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

# pollution_data
class PollutionData(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/'

    def station(self, station_name, data_term, page_no='1', num_of_rows='10', ver='1.2'):
        verurl = '&ver=' + ver
        # It's for changing version, It seems like version system doesn't work on OpenAPI, so I comment them.
        # verurl = '&ver='
        # if ver == '0': verurl = ''
        # else: ver_url += ver

        urllist = [
            self._mainurl + 'getMsrstnAcctoRltmMesureDnsty?', 'stationName=', urllib.parse.quote(station_name),
            "&dataTerm=", data_term, '&pageNo=', page_no, '&numOfRows=', num_of_rows,
            '&ServiceKey=', self._service_key, '&_returnType=json', verurl
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'mangName', 'khaiGrade', 'khaiValue', 'coGrade',
                'coValue', 'no2Grade', 'no2Value', 'o3Grade', 'o3Value',
                'pm10Grade', 'pm10Value', 'pm10Value24', 'pm25Grade', 'pm25Value',
                'pm25Value24', 'so2Grade', 'so2Value'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def strangelist(self, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl, 'getUnityAirEnvrnIdexSnstiveAboveMsrstnList?', 'pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'addr', 'stationName'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def sido(self, sido_name, page_no='1', num_of_rows='10', ver='1.2'):
        verurl = '&ver=' + ver
        # It's for changing version, It seems like version system doesn't work on OpenAPI, so I comment them.
        # verurl = '&ver='
        # if ver == '0': verurl = ''
        # else: verurl += ver

        urllist = [
            self._mainurl, 'getCtprvnRltmMesureDnsty?', 'sidoName=', urllib.parse.quote(sido_name),
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json', verurl
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'mangName', 'stationName', 'khaiGrade', 'khaiValue',
                'coGrade', 'coValue', 'no2Grade', 'no2Value', 'o3Grade',
                'o3Value', 'pm10Grade', 'pm10Value', 'pm10Value24', 'pm25Grade',
                'pm25Value', 'pm25Value24', 'so2Grade', 'so2Value'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def forecastlist(self, inform_code, search_date='0', page_no='1', num_of_rows='10'):
        dateurl = '&searchDate='
        if search_date == '0':
            dateurl = ''
        else:
            dateurl += search_date

        urllist = [
            self._mainurl, 'getMinuDustFrcstDspth?', 'InformCode=', inform_code, dateurl,
            '&pageNo=', page_no, '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key,
            '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'imageUrl1', 'imageUrl2', 'imageUrl3', 'imageUrl4',
                'imageUrl5', 'imageUrl6', 'informCause', 'informData', 'informGrade',
                'informOverall', 'actionKnack'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

# o3occurinfo
class O3YOccurInfo(object):
    def __init__(self, imported_key):
        self._service_key = str(imported_key)
        self._mainurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/OzYlwsndOccrrncInforInqireSvc/'

    def o3(self, year, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getOzAdvsryOccrrncInfo?', 'year=', year, '&pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'districtName', 'moveName', 'issueTime', 'issueVal',
                'clearTime', 'clearVal', 'maxVal'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata

    def yellow(self, year, page_no='1', num_of_rows='10'):
        urllist = [
            self._mainurl + 'getYlwsndAdvsryOccrrncInfo?', 'year=', year, '&pageNo=', page_no,
            '&numOfRows=', num_of_rows, '&ServiceKey=', self._service_key, '&_returnType=json'
        ]
        url = ''.join(urllist)

        response = urllib.request.urlopen(url).read().decode("utf-8")
        jsondata = json.loads(response)

        returndata = dict()
        returndata['totalCount'] = jsondata['totalCount']

        for i in range(0, returndata['totalCount']):
            returndata[str(i)] = dict()
            list = [
                'dataTime', 'tmCnt', 'tmArea'
            ]
            for j in list:
                returndata[str(i)][j] = jsondata['list'][0][j]

        return returndata



# 주소확인 함수
def input_location(user_message):

    geolocator = Nominatim(user_agent="my_geocoder")
    
    try:
        
        # 원하는 지역 입력 (ex. 수지구)
        input_address = input("원하는 장소의 주소를 입력하세요: ")
        location = geolocator.geocode(input_address, language="ko-KR")
        
        tm_a = location.address
        tm_x = location.latitude
        tm_y = location.longitude
        
        if not location:
            print("입력하신 주소를 찾을 수 없습니다.")
            return None, None, None
        
        return tm_a, tm_x, tm_y
        
    except Exception as e:
        print(f"알 수 없는 오류가 발생하였습니다: {e}")
        return None, None, None



# 위치에 따른 환경정보 출력
def aircondition(input_address, a):

    pollution_stats = PollutionStats(a)

    # 입력받은 지역의 대기 오염 통계 정보 가져오기 (ex. 수지구)
    result = pollution_stats.station(
        station_name=input_address, searchCondition='DAILY', page_no='1', num_of_rows='1')

    # return값을 통한 데이터 넘기기 (단순 출력 방지)
     if result['totalCount'] > 0:
        return f"측정일: {result['0']['dataTime']}\n" \
               f"통합대기환경 지수: {result['0']['khaiGrade']}\n" \
               f"일산화탄소 지수: {result['0']['coGrade']}\n" \
               f"오존 지수: {result['0']['o3Grade']}\n" \
               f"PM 10(미세먼지) 수치: {result['0']['pm10Grade']}\n" \
               f"PM 2.5(미세먼지) 수치: {result['0']['pm25Grade']}"
    else:
        return "해당 위치에 대한 데이터가 없습니다."
    
    

# 카카오톡 챗봇에서 사용하기 위한 스킬서버 및 응답 
def generate_response():
    # 사용자의 메시지에 따라 적절한 응답을 생성하는 로직을 작성하세요.
    if "미세먼지" in user_message:
        
        if "미세먼지" in user_message:
        tm_a, tm_x, tm_y = input_location(user_message)
        
        if tm_a and tm_x and tm_y:
            a = pdairp.PollutionData("Xw%2FEwzmpdYhZzRl2Gh7ImRs%2BkkU%2F5JFrWAZzJmDWTgStFhfXkwA2J02LvidsMnqVLKV40imtar0WoUQmi%2FYxOg%3D%3D")
            pollution_info = aircondition(tm_a, a)
            return pollution_info
            
        else:
            return "죄송해요. 위치 정보를 찾을 수 없어요."        
       
    else:
        return "죄송해요. 이해할 수 없는 메시지에요."

@app.route('/webhook', methods=['POST'])
def webhook():
    # 카카오톡 서버에서 전송한 데이터를 JSON 형식으로 파싱합니다.
    data = request.get_json()

    # 사용자가 전송한 메시지 텍스트를 추출합니다.
    message_text = data['userRequest']['utterance']

    # generate_response 함수를 사용하여 응답 메시지를 생성합니다.
    response_text = generate_response(message_text)

    # 생성된 응답을 JSON 형식으로 구성합니다.
    response = {
        'version': '2.0',
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': response_text
                    }
                }
            ]
        }
    }

    return jsonify(response) 응답을 반환합니다.
    return jsonify(response)

# flask로 변환한 앱을 실행하기 위한 main    
if __name__ == '__main__':
    app.run()
