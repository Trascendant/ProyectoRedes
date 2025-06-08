from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

# Template HTML simple
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Proyecto Redes UNA - Python App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 600px; margin: 0 auto; }
        .status { padding: 20px; background: #e8f5e8; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Aplicación Python - Proyecto Redes</h1>
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
        "proyecto": "Comunicaciones y Redes - UNA",
        "tecnologias": ["Docker", "Kubernetes", "CI/CD", "Azure"],
        "estudiantes": "Grupo #X"  # Cambiar por su número de grupo
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
