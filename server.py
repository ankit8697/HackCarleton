from flask import Flask, render_template
import CarletonCalendarScrape
import json
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return render_template("index.html", all_data=all_data)

# @app.route('/data')
# def data():
#     return CarletonCalendarScrape.getAllData()

@app.route('/graph')
def graphServer():
    f1 = open("2019_04_data.json")
    f1_data = json.loads(f1.read())
    f1.close()
    f2 = open("2019_05_data.json")
    f2_data = json.loads(f2.read())
    f2.close()
    f3 = open("2019_06_data.json")
    f3_data = json.loads(f3.read())
    f3.close()
    final_data = f1_data + f2_data + f3_data
    return render_template("graph.html", all_data=final_data)

@app.route('/stylesheet.css')
def style():
    return render_template("stylesheet.css", all_data=all_data)

if __name__ == "__main__":
    all_data = CarletonCalendarScrape.getAllDataPython()
    all_categories = CarletonCalendarScrape.add_to_categories(all_data)
    #CarletonCalendarScrape.main()
    app.run(debug = True)
    
