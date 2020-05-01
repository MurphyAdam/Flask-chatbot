import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from config import Config, Development


seasurf = SeaSurf()
talisman = Talisman()

csp = {
    'default-src': [
        '\'self\'',
        '*.cloudflare.com',
        '*.jsdelivr.net',
        '*.jquery.com',
        '*.gravatar.com',
        '*.googleapis.com',
        '*.w3.org',
        '*.github.com'
    ],
    'script-src': [
        '\'self\'',
        '*.cloudflare.com',
        '*.jsdelivr.net',
        '*.jquery.com',
        '*.gravatar.com',
        '*.googleapis.com',
        '*.w3.org',
        '*.github.com'
    ],
    'style-src': [
        '\'unsafe-inline\' \'self\'',
        '*.cloudflare.com',
        '*.jsdelivr.net',
        '*.jquery.com',
        '*.gravatar.com',
        '*.googleapis.com',
        '*.w3.org',
        '*.github.com'],
}

def create_app(config_class=Development):
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True, static_url_path='')

    # Application Configuration
    app.config.from_object(config_class)
    with app.app_context():
        # Initialize Plugins
        seasurf.init_app(app)
        talisman.init_app(app, content_security_policy=csp, content_security_policy_nonce_in=['script-src'])
        # Register Blueprints
        # MAIN BP
        from app.main import main as main_blueprint
        app.register_blueprint(main_blueprint)
        # CHATBOT BP
        from app.chatbot import chatbot as chatbot_blueprint
        app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot')
        # PWA BP
        from app.pwa import pwa as pwa_blueprint
        app.register_blueprint(pwa_blueprint, url_prefix='')
        # ERRORS BP
        from app.errors import errors as errors_blueprint
        app.register_blueprint(errors_blueprint)
        # Configute Debugging
        if app.debug or app.testing:
            if app.config['LOG_TO_STDOUT']:
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(logging.INFO)
                app.logger.addHandler(stream_handler)
            else:
                if not os.path.exists('logs'):
                    os.mkdir('logs')
                file_handler = RotatingFileHandler('logs/app.log',
                                                   maxBytes=20480, backupCount=20)
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s %(levelname)s: %(message)s '
                    '[in %(pathname)s:%(lineno)d]'))
                file_handler.setLevel(logging.INFO)
                app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('app startup')
        return app
