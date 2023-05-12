# 미니프로젝트 Part2
기간 - 2023.05.02 ~ 2023.05.16


## WPF 학습
- SCADA/HMT 시뮬레이션(smartHome 시스템)
	- C# WPF 
	- MahApps.Metro(MetroUI 디자인 라이브러리)
	- Bogus(더미데이터 생성 라이브러리)
	- Newtonsoft.json
	- M2Mqtt(통신 라이브러리)
	- DB 데이터 바인딩
	- LiveCharts
	- OxyPlot
	
- SmartHome 시스템 문제점
	- 실행 후 시간이 소요되면 UI제어가 느려짐 (TextBox에 텍스트가 과도) - 해결!
	- LiveCharts는 실시간 게이지외 대용량 차트는 무리(LiveCharts ver2동일)
	- 대용량 데이터 차트는 OxyChart를 사용
	
- SmartHome 앱
<img src="https://raw.githubusercontent.com/yeseoz/miniprojects/main/imges/SmartHome.gif" width="650" />

<img src="https://raw.githubusercontent.com/yeseoz/miniprojects/main/imges/SmartHomeimg.png" width="650" />
