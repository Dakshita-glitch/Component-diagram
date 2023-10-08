from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get user inputs from the form
    group_name = request.form['group_name']
    component1_name = request.form['component1_name']
    component2_name = request.form['component2_name']
    component3_name = request.form['component3_name']
    component4_name = request.form['component4_name']
    component5_name = request.form['component5_name']
    component6_name = request.form['component6_name']
    component7_name = request.form['component7_name']
    component8_name = request.form['component8_name']
    component9_name = request.form['component9_name']
    example1_name = request.form['example1_name']
    folder3_name = request.form['folder3_name']
    frame4_name = request.form['frame4_name']

    # Generating PlantUML code
    plantuml_code = f'''
@startuml
package "{group_name}" {{
  HTTP - [{component1_name}]
  [{component2_name}]
}}

node "Other Groups" {{
  FTP - [{component3_name}]
  [{component1_name}] --> FTP
}}

cloud {{
  [{example1_name}]
}}

database "MySql" {{
  folder "This is my folder" {{
    [{folder3_name}]
  }}
  frame "Foo" {{
    [{frame4_name}]
  }}
}}

[{component2_name}] --> [{example1_name}]
[{example1_name}] --> [{folder3_name}]
[{folder3_name}] --> [{frame4_name}]
@enduml
'''

    return render_template('index.html', plantuml_code=plantuml_code)

if __name__ == '__main__':
    app.run(debug=True)
