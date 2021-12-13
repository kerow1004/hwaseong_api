from flask import jsonify
from flaskext.mysql import MySQL
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource
from flask_restful import reqparse
import json, time

mysql = MySQL()
start = time.time()
def timecount():

    return (time.time() - start)


class hwaseong_KSIC(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('ksic', required=True, type=str)
            parser.add_argument('year', required=True, type=str)
            args = parser.parse_args()
            cur = mysql.connect().cursor()
            cur.execute('''select lpad(a.KSIC, 5,0) as KSIC, a.IndexKor, a.IndexEng, lpad(c.HsCode, 6,0) as HsCode, a.HsCodeKor, a.HsCodeEng, lpad(a.NTS, 6,0) as NTS, a.NTSKor
                    , b.Year, c.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                    , c.DE, c.Division, c.Profit, c.Price, c.Kg as T, c.CNT from codezip as a
                    left join ksic_Prod_DLVY as b on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor
                    left join merge_country as c on a.HsCode = c.HsCode
                    where a.KSIC = '''+args['ksic']+''' and b.Year = ''' +args['year'] )

            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            # print(json.dumps(r, indent="\t", ensure_ascii=False))
            print("검색성공", timecount())
            return jsonify({'hwaseongDATA' : r})
        except Exception as e:
            return {'error': str(e)}

class hwaseong_IndexKor(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('indexkor', required=True, type=str)
            parser.add_argument('year', required=True, type=str)
            args = parser.parse_args()
            cur = mysql.connect().cursor()
            cur.execute('''select lpad(a.KSIC, 5,0) as KSIC, a.IndexKor, a.IndexEng, lpad(c.HsCode, 6,0) as HsCode, a.HsCodeKor, a.HsCodeEng, lpad(a.NTS, 6,0) as NTS, a.NTSKor
                    , b.Year, c.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                    , c.DE, c.Division, c.Profit, c.Price, c.Kg as T, c.CNT from codezip as a
                    left join ksic_Prod_DLVY as b on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor
                    left join merge_country as c on a.HsCode = c.HsCode
                    where a.IndexKor like '% '''+args['indexkor']+''' %'  and b.Year = ''' +args['year'])

            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            # print(json.dumps(r, indent="\t", ensure_ascii=False))
            print("검색성공", timecount())
            return jsonify({'hwaseongDATA' : r})
        except Exception as e:
            return {'error': str(e)}

class hwaseong_Hscode(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('hscode', required=True, type=str)
            parser.add_argument('year', required=True, type=str)
            parser.add_argument('division', required=True, type=str)
            args = parser.parse_args()
            cur = mysql.connect().cursor()
            cur.execute('''select lpad(a.KSIC, 5,0) as KSIC, a.IndexKor, a.IndexEng, lpad(c.HsCode, 6,0) as HsCode, a.HsCodeKor, a.HsCodeEng, lpad(a.NTS, 6,0) as NTS, a.NTSKor
                    , b.Year, c.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                    , c.DE, c.Division, c.Profit, c.Price, c.Kg as T, c.CNT from codezip as a
                    left join ksic_Prod_DLVY as b on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor
                    left join merge_country as c on a.HsCode = c.HsCode
                    where c.HsCode = ''' +args['hscode'] + ''' and b.Year = ''' +args['year'] + ''' and c.Division like "'''+args['division']+'''" ''' )


            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            # print(json.dumps(r, indent="\t", ensure_ascii=False))
            print("검색성공", timecount())
            return jsonify({'hwaseongDATA' : r})
        except Exception as e:
            return {'error': str(e)}

class hwaseong_NTS(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('nts', required=True, type=str)
            parser.add_argument('year', required=True, type=str)
            args = parser.parse_args()
            cur = mysql.connect().cursor()
            cur.execute('''select lpad(a.KSIC, 5,0) as KSIC, a.IndexKor, a.IndexEng, lpad(c.HsCode, 6,0) as HsCode, a.HsCodeKor, a.HsCodeEng, lpad(a.NTS, 6,0) as NTS, a.NTSKor
                    , b.Year, c.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                    , c.DE, c.Division, c.Profit, c.Price, c.Kg as T, c.CNT from codezip as a
                    left join ksic_Prod_DLVY as b on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor
                    left join merge_country as c on a.HsCode = c.HsCode
                    where a.NTS = '''+args['nts']+''' and b.Year = ''' +args['year'])

            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            # print(json.dumps(r, indent="\t", ensure_ascii=False))
            print("검색성공", timecount())
            return jsonify({'hwaseongDATA' : r})
        except Exception as e:
            return {'error': str(e)}

from flask import Flask
from flask_restful import Api

app = Flask('hwaseong_api')
api = Api(app)
app.config['JSON_AS_ASCII'] = False

api.add_resource(hwaseong_KSIC, '/hwaseong_data/ksic')
api.add_resource(hwaseong_IndexKor, '/hwaseong_data/indexkor')
api.add_resource(hwaseong_Hscode, '/hwaseong_data/hscode')
api.add_resource(hwaseong_NTS, '/hwaseong_data/nts')


# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'wiseadmin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Wise1357!@'
app.config['MYSQL_DATABASE_DB'] = 'hwaseong_api_DB'
app.config['MYSQL_DATABASE_HOST'] = '13.125.244.217'

mysql.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)