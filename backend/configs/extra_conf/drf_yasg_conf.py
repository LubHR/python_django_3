SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorizations',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH':None
}
