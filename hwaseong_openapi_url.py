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
            with mysql.connect().cursor() as cur:
                cur.execute('''select e.KSIC, e.IndexKor, e.IndexEng, e.HsCode, e.HsCodeKor, e.HsCodeEng, e.NTS, e.NTSKor, e.Year, e.Month
                                    , e.Class, e.Biz, e.Prod, e.DLVY, e.BL, c.DE, c.Division, c.Profit, c.Price, c.Kg, c.CNT 
                                from
                                    (select a.KSIC, a.IndexKor, a.IndexEng, a.HsCode, a.HsCodeKor, a.HsCodeEng, a.NTS, a.NTSKor
                                        , b.Year, a.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                                        from codezip as a
                                        left join ksic_Prod_DLVY as b
                                            on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor and a.Year = b.Year) as e
                                        left join merge_country as c
                                            on 1=1 
                                            where e.KSIC = '''+args['ksic']+''' and e.Year = ''' +args['year']+'''
                                            limit 100 offset 0''' )

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
            with mysql.connect().cursor() as cur:
                cur.execute('''select e.KSIC, e.IndexKor, e.IndexEng, e.HsCode, e.HsCodeKor, e.HsCodeEng, e.NTS, e.NTSKor, e.Year, e.Month
                                    , e.Class, e.Biz, e.Prod, e.DLVY, e.BL, c.DE, c.Division, c.Profit, c.Price, c.Kg, c.CNT 
                                from
                                    (select a.KSIC, a.IndexKor, a.IndexEng, a.HsCode, a.HsCodeKor, a.HsCodeEng, a.NTS, a.NTSKor
                                        , b.Year, a.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                                        from codezip as a
                                        cross join ksic_Prod_DLVY as b) as e
                                        cross join merge_country as c 
                        where e.IndexKor like '%'''+args['indexkor']+'''%'  and e.Year = ''' +args['year']+ ''' limit 100 offset 0''')

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
            with mysql.connect().cursor() as cur:
                cur.execute('''select e.KSIC, e.IndexKor, e.IndexEng, e.HsCode, e.HsCodeKor, e.HsCodeEng, e.NTS, e.NTSKor, e.Year, e.Month
                                    , e.Class, e.Biz, e.Prod, e.DLVY, e.BL, c.DE, c.Division, c.Profit, c.Price, c.Kg, c.CNT 
                                from
                                    (select a.KSIC, a.IndexKor, a.IndexEng, a.HsCode, a.HsCodeKor, a.HsCodeEng, a.NTS, a.NTSKor
                                        , b.Year, a.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                                        from codezip as a
                                        cross join ksic_Prod_DLVY as b
                                            ) as e
                                        left join merge_country as c
                                            on 1=1 
                        where e.HsCode = ''' +args['hscode'] + ''' and e.Year = ''' +args['year'] + ''' and c.Division ="'''+args['division']+'''" limit 100 offset 0''' )


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
            with mysql.connect().cursor() as cur:
                cur.execute('''select e.KSIC, e.IndexKor, e.IndexEng, e.HsCode, e.HsCodeKor, e.HsCodeEng, e.NTS, e.NTSKor, e.Year, e.Month
                                    , e.Class, e.Biz, e.Prod, e.DLVY, e.BL, c.DE, c.Division, c.Profit, c.Price, c.Kg, c.CNT 
                                from
                                    (select a.KSIC, a.IndexKor, a.IndexEng, a.HsCode, a.HsCodeKor, a.HsCodeEng, a.NTS, a.NTSKor
                                        , b.Year, a.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                                        from codezip as a
                                        left join ksic_Prod_DLVY as b
                                            on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor and a.Year = b.Year) as e
                                        left join merge_country as c
                                            on 1=1 
                        where e.NTS = '''+args['nts']+''' and e.Year = ''' +args['year']+ ''' limit 100 offset 0''')

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