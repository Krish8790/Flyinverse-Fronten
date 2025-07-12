from flask import Flask, request, render_template

app = Flask(__name__)

search_items = [
    "Flights to Europe",
    "Flights to dubai",
    "Book a Sedan Cab",
    "Football Trials in Spain",
    "Tourism Packages in Italy",
]

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = [item for item in search_items if query in item.lower()]
    return render_template('search_results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
