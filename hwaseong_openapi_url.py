from flask import jsonify
from flaskext.mysql import MySQL
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Resource
from flask_restful import reqparse
import json

mysql = MySQL()




class hwaseong_data(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('KSIC', required=True, type=str)
            parser.add_argument('HsCode', required=True, type=str)
            parser.add_argument('NTS', required=True, type=str)
            parser.add_argument('IndexKor', required=True, type=str)
            args = parser.parse_args()
            cur = mysql.connect().cursor()
            cur.execute('''select a.KSIC, a.IndexKor, a.IndexEng, c.HsCode, a.HsCodeKor, a.HsCodeEng, a.NTS, a.NTSKor
                    , b.Year, c.Month, b.Class, b.Biz, b.Prod, b.DLVY, b.BL
                    , c.DE, c.Division, c.Profit, c.Price, c.Kg as T, c.CNT from codezip as a
                    left join ksic_Prod_DLVY as b on a.KSIC = b.KSIC and a.IndexKor = b.IndexKor
                    left join merge_country as c on a.HsCode = c.HsCode
                    where a.KSIC = '''+args['KSIC']+'''  and c.HsCode = '''+ args['HsCode'] +''' and a.NTS = ''' +args['NTS']+ ''' and a.IndexKor like '% '''+args['IndexKor']+''' %' ''')

            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            print(json.dumps(r, indent="\t", ensure_ascii=False))
            # print(r)
            return jsonify({'hwaseongDATA' : r})
        except Exception as e:
            return {'error': str(e)}

from flask import Flask
from flask_restful import Api

app = Flask('My First App')
api = Api(app)
app.config['JSON_AS_ASCII'] = False
api.add_resource(hwaseong_data, '/hwaseong_data')


# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'wiseadmin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Wise1357!@'
app.config['MYSQL_DATABASE_DB'] = 'hwaseong_api_DB'
app.config['MYSQL_DATABASE_HOST'] = '3.37.219.7'

mysql.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)