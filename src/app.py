from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# Template HTML simple
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Proyecto Redes Aplicacion Python</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .status { padding: 20px; background: #e8f5e8; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1> Proyecto Redes Aplicacion Python </h1>
        <h2> Probando push automatico 1 </h2>
        <img> src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.craiyon.com%2Fimage%2FgG-qtnrhRe28Jam23g2mmA&psig=AOvVaw3rEATrZVSrQ4QeTac2rxx6&ust=1750726471746000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJiLmtuqho4DFQAAAAAdAAAAABAE" alt="El Tigre" </img>
        <div class="status">
            <h2>Estado del Sistema</h2>
            <p><strong>Versión:</strong> {{ version }}</p>
            <p><strong>Ambiente:</strong> {{ environment }}</p>
            <p><strong>Pod:</strong> {{ pod_name }}</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, 
                                version="1.0.0",
                                environment=os.getenv('ENVIRONMENT', 'development'),
                                pod_name=os.getenv('HOSTNAME', 'local'))

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "service": "python-web-app"
    })

@app.route('/api/info')
def info():
    return jsonify({
        "proyecto": "Redes proyecto CI/CD",
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
