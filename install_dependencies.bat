    @echo off
    python.exe -m pip install --upgrade pip

    REM Install libraries (replace REM with actual commands)
    pip install xgboost
    pip install requests
    pip install beautifulsoup4
    pip install selenium
    pip install psycopg2
    pip install pytest
    pip install pandas numpy matplotlib seaborn scikit-learn scipy requests flask django beautifulsoup4 tensorflow torch

    REM Save to requirements.txt (optional)
    pip freeze > requirements.txt