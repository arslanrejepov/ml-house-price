hangzhou-rent-agency/
│
├── frontend/                  # React app (UI)
│   ├── public/
│   ├── src/
│   │   ├── components/        # Reusable UI pieces
│   │   │   ├── Form.jsx
│   │   │   ├── ResultCard.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js         # axios calls
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/                   # FastAPI / Flask API
│   ├── app/
│   │   ├── main.py            # API entry point
│   │   │
│   │   ├── routes/
│   │   │   └── predict.py
│   │   │
│   │   ├── models/            # ML model loading
│   │   │   └── predictor.py
│   │   │
│   │   ├── schemas/           # request/response schema
│   │   │   └── house.py
│   │   │
│   │   └── utils/
│   │       └── preprocessing.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── ml/                        # ML experiments + training
│   ├── notebooks/
│   │   └── eda.ipynb
│   │
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   │
│   ├── src/
│   │   ├── train.py
│   │   ├── features.py
│   │   └── evaluate.py
│   │
│   └── models/
│       └── rent_model.pkl
│
├── configs/
│   └── config.yaml            # paths, params
│
├── tests/
│   └── test_api.py
│
├── docker-compose.yml
├── README.md
└── .gitignore