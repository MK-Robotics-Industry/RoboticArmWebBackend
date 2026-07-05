RoboticArmWebBackend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   │
│   ├── api/                    # API routes
│   │   ├── __init__.py
│   │   ├── robot.py
│   │   ├── serial.py
│   │   ├── settings.py
│   │   └── health.py
│   │
│   ├── services/               # Business logic
│   │   ├── serial_service.py
│   │   ├── robot_service.py
│   │   ├── wifi_service.py
│   │   └── config_service.py
│   │
│   ├── serial/                 # Serial communication
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── reader.py
│   │   └── writer.py
│   │
│   ├── models/                 # Pydantic models
│   │   ├── robot.py
│   │   ├── serial.py
│   │   └── settings.py
│   │
│   ├── core/                   # Core configuration
│   │   ├── config.py
│   │   ├── constants.py
│   │   └── logger.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   └── validators.py
│   │
│   └── websocket/
│       └── manager.py
│
├── config/
│   ├── settings.json
│   └── robot.json
│
├── logs/
│   └── app.log
│
├── tests/
│   ├── test_serial.py
│   └── test_api.py
│
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── run.py