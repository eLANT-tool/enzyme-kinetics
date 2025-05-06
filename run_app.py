import subprocess
import os
import sys

if __name__ == "__main__":
    # Streamlit アプリを起動するコマンド
    cmd = [
        "streamlit", "run",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "enzyme_kinetics_app.py"),
        "--server.headless=true",
        "--browser.serverAddress=localhost",
        "--browser.serverPort=8501",
        "--server.enableCORS=false"
    ]
    
    # サブプロセスとして Streamlit を起動
    process = subprocess.Popen(cmd)
    
    # ブラウザを開く
    import webbrowser
    webbrowser.open("http://localhost:8501")
    
    # プロセスが終了するまで待機
    process.wait()