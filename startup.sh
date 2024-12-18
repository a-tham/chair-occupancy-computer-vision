apt-get update && apt-get install -y ffmpeg x264 libx264-dev libgl1-mesa-glx
pip install --no-cache-dir -r requirements.txt
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0 --server.enableCORS=false --server.enableXsrfProtection=false