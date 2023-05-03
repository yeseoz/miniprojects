using Bogus;
using FakeIotDeviceApp.Models;
using MahApps.Metro.Controls;
using MahApps.Metro.Controls.Dialogs;
using System.Diagnostics;
using System.Threading;
using uPLibrary.Networking.M2Mqtt;

namespace FakeIotDeviceApp
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        Faker<SensorInfo> FakeHomeSensor = null; // 가짜 스마트홈 센서 값 변수
        MqttClient client;
        Thread MqttThread { get; set; }

        public MainWindow()
        {
            InitializeComponent();

            InitFakeData(); // 전체 초기화
        }

        private void InitFakeData()
        {
            var Rooms = new[] { "Bed", "Bath", "Living", "Dining" };

            FakeHomeSensor = new Faker<SensorInfo>()
                .RuleFor(s => s.Home_Id, "D101H703") // 임의로 픽스된 홈 아이디 101동 703호
                .RuleFor(s => s.Room_Name, f => f.PickRandom(Rooms)) // 실행할때 마다 방 이름이 게속 바뀜
                .RuleFor(s => s.Sensing_DateTime, f => f.Date.Past(0)) // 현재 시각이 생성됨
                .RuleFor(s => s.Temp, f => f.Random.Float(20.0f, 30.0f)) // 20도에서 30도 사이의 실수 값 생성
                .RuleFor(s => s.Humid, f => f.Random.Float(40.0f, 64.0f));
        }

        private void MetroWindow_Loaded(object sender, System.Windows.RoutedEventArgs e)
        {
            TxtMqttBrokerIp.Focus();
        }

        private async void BtnConnect_Click(object sender, System.Windows.RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(TxtMqttBrokerIp.Text))
            {
                await this.ShowMessageAsync("오류", "브로커 IP를 입력하세요");
                return;
            }

            // 브로커 아이피로 접속
            ConnectMqttBroker();

            // 무한 반복 하위의 로직을
            StartPublish();
        }
        private void ConnectMqttBroker()
        {
            client = new MqttClient(TxtMqttBrokerIp.Text);
            client.Connect("SmartHomeDev"); // publish client ID를 지정
        }

        private void StartPublish()
        {
            MqttThread = new Thread(() =>
            {
                while (true)
                {
                    // 가짜 스마트홈 센서값 생성
                    SensorInfo info = FakeHomeSensor.Generate();
                    Debug.WriteLine($"{info.Home_Id} / {info.Room_Name} / {info.Sensing_DateTime} / {info.Temp}");

                    // 센서값 MQTT 브로커에 전송

                    // RtbLog에 출력
                    //1초 동안 대기
                    Thread.Sleep(1000);
                }
            });
            MqttThread.Start();
        }

        private void MetroWindow_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            if (client != null && client.IsConnected == true)
            {
                client.Disconnect(); // 접속을 끊어주고
            }
            if (MqttThread != null)
            {
                MqttThread.Abort(); // 여기가 없으면 프로그램 종료후에도 메모리에 남아있음!!!
            }
        }
    }
}
