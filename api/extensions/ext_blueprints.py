from neil_app import NeilApp

def init_app(app: NeilApp):
    
    from flask_cors import CORS
    from controller import bp
    
    CORS(
        bp,
        allow_headers=["Content-Type", "Authorization", "X-App-Code"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    )
    
    app.register_blueprint(bp)

    

