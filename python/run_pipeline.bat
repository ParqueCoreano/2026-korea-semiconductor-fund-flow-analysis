@echo off
cd /d "%~dp0"       

"..\.venv\Scripts\python.exe" "01_collect_market_data.py"

if errorlevel 1 (
    echo Pipeline failed.
    pause
    exit /b 1
)

echo Pipeline completed.
pause

:: cd /d "%~dp0" : 현재경로에서 배치파일을 진행
:: cd /d "C:\Users\~~" : 해당 경로로 이동하여 배치파일을 진행  (" "를 붙여 경로에 공백이 있어도 하나의 경로로 처리)
:: . : 현재폴더 / .. : 한 단계 위 폴더
:: : errorlevel 1 : 앞서 실행한 프로그램이 오류 상태를 반환했는지 확인
:: : echo — 화면에 문구를 출력 / pause — 키 입력을 대기 / exit /b 1 — 현재 배치파일을 오류 상태로 종료
:: : echo는 사용자에게 실행 결과를 보여주기 / pause는 결과를 확인할 수 있게 창이 바로 닫히지 않게 해.
