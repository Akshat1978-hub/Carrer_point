# CareerPredict AI — Explore Your Future

Streamlit exhibition prototype for career exploration, illustrative forecasting, scenario simulation, and a learning quiz.

## Data note

The included trend series is **synthetic demonstration data**. It is not official labour-market data and must not be presented as factual job-demand statistics. The predictor uses a simple linear-trend baseline to teach extrapolation. The scenario simulator is an illustrative formula, not a trained ML model.

## Features

- Interest-based career recommendations with explanations
- Trend chart with selectable 1, 3, 5, or 10 year horizon
- Interactive what-if simulator
- Career Quest quiz and result badges
- Educational explanation of forecasting and uncertainty
- Responsive Streamlit UI
- Unit tests

## Run locally

Python 3.10–3.12 recommended.

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

macOS/Linux:
```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests:
```bash
pytest -q
```

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository named `CareerPredict-AI`.
2. Upload all project files and folders.
3. Sign in to Streamlit Community Cloud with GitHub.
4. Create a new app; choose your repository, branch, and `app.py`.
5. Deploy. No API keys are needed for core features.

## Replace demo data responsibly

Before making real-world forecasts:
1. Select an official, documented dataset for the relevant geography and occupation definitions.
2. Record the source URL, publication date, units, and licence.
3. Update `src/careers.py` or add a data loader.
4. Backtest using time-based splits and compare against a simple baseline.
5. Report suitable error metrics and uncertainty.

Never present synthetic values as official data.

## Structure

```text
CareerPredict-AI/
├── app.py
├── src/
│   ├── __init__.py
│   ├── careers.py
│   ├── forecasting.py
│   └── quiz.py
├── tests/
│   └── test_core.py
├── requirements.txt
├── README.md
└── .gitignore
```
