from flask import Flask,render_template
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')

def index():
    

    url = URL(
        user='RahulDeoKundan',
        password='Rahul@1990',
        account='fn48416.southeast-asia.azure',
        warehouse='COMPUTE_WH',
        database='DATALOAD',
        schema='PUBLIC',
        role = 'ACCOUNTADMIN'
    )
    engine = create_engine(url)
    connection = engine.connect()

    results = connection.execute('select * from PUBLIC.JSONLOAD; ').fetchall()
    
    df = pd.DataFrame(results)
    print(df)
    
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = json.loads(json_records)
#    context = {'d': data}
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)