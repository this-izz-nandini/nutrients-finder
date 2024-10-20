import requests
from flask import *
import io, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask('myapp')

top_6_nutrients = []
calories = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global top_6_nutrients, calories
    if request.method == 'POST':
        ingredient = request.form.get('ingredient')
        
        app_id = os.getenv('Edamam_app_id')
        app_key = os.getenv('Edamam_app_key')
        
        url = 'https://api.edamam.com/api/nutrition-data'
        
        try:
            res = requests.get(url, params={'app_id': app_id, 'app_key': app_key, 'ingr': ingredient})
            
            if res.status_code != 200:
                return jsonify({"error": "Request failed", "status_code": res.status_code, "response": res.text}), res.status_code
            
            data = res.json()
            nutrient_data = data.get('totalNutrients', {})
            calories = data.get('calories', 0) 
            
            # Sort the nutrients by quantity in descending order and get the top 15
            sorted_nutrients = sorted(nutrient_data.items(), key=lambda x: x[1]['quantity'], reverse=True)
            top_nutrients = sorted_nutrients[:15]
            top_6_nutrients = sorted_nutrients[:6]  # Save top 6 for the pie chart
            
            return render_template('result.html', top_nutrients=top_nutrients, ingredient=ingredient)
        
        except Exception as e:
            return jsonify({"error": str(e), "response": res.text if 'res' in locals() else "No response"}), 500

    return render_template('index.html')

@app.route('/pie-chart')
def pie_chart():
    global top_6_nutrients, calories
    
    labels = [x[1]['label'] for x in top_6_nutrients]
    sizes = [x[1]['quantity'] for x in top_6_nutrients]
    colors = plt.get_cmap('tab20').colors[:len(labels)] 
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.figtext(0.5, 0.01, f"Total Calories: {calories}", ha="center", fontsize=12, color="blue")
    
    # Save the pie chart to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png')

app.run(debug=True)
