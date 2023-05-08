using MahApps.Metro.Controls;
using Newtonsoft.Json;
using SmartHomeMonitoringApp.Logics;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Windows.Controls;
using uPLibrary.Networking.M2Mqtt.Messages;

namespace SmartHomeMonitoringApp.Views
{
    /// <summary>
    /// DataBaseControl.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class DataBaseControl : UserControl
    {
        public bool IsConnected { get; set; }
        public DataBaseControl()
        {
            InitializeComponent();
        }

        // 유저 컨트롤 로드 이벤트 핸들러
        private void UserControl_Loaded(object sender, System.Windows.RoutedEventArgs e)
        {
            TxbBrokerUrl.Text = Commons.BROKERHOST;
            TxbMqttTopic.Text = Commons.MQTTTOPIC;
            TxtConnString.Text = Commons.MYSQL_CONNSTRING;

            IsConnected = false; // 아직 접속이 안되었음
            BtnConnDb.IsChecked = false;
        }

        // 토글버튼 클릭(1: 접속 /2: 접속 끊김) 이벤트 핸들러
        private void BtnConnDb_Click(object sender, System.Windows.RoutedEventArgs e)
        {
            if (IsConnected == false)
            {
                // Mqtt 브로커 생성
                Commons.MQTT_CLIENT = new uPLibrary.Networking.M2Mqtt.MqttClient(Commons.BROKERHOST);

                try
                {
                    // Mqtt subscribe(구독할) 로직
                    if (Commons.MQTT_CLIENT.IsConnected == false)
                    {
                        // MQTT 접속
                        Commons.MQTT_CLIENT.MqttMsgPublishReceived += MQTT_CLIENT_MqttMsgPublishReceived; // 메시지를 받는 쪽
                        Commons.MQTT_CLIENT.Connect("MONITOR"); // clientID = 모니터
                        Commons.MQTT_CLIENT.Subscribe(new string[] { Commons.MQTTTOPIC },
                            new byte[] { MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE }); // QOS는 네트워크 통신 옵션
                        UpdateLog(">>> MQTT Broker Connected");

                        BtnConnDb.IsChecked = true;
                        IsConnected = true; // 예외 발생하면 true로 변경할 필요 없음
                        BtnConnDb.Content = "Connect";

                    }
                }
                catch
                {
                    //pass
                }

            }
            else
            {
                BtnConnDb.IsChecked = false;
                IsConnected = false;
                BtnConnDb.Content = "DisConnect";
            }
        }

        private void UpdateLog(string msg)
        {
            this.Invoke(() =>
            {
                TxtLog.Text += $"{msg}\n";
                TxtLog.ScrollToEnd();
            });
        }

        // Subscribe가 발생할 때 이벤트 핸들러
        private void MQTT_CLIENT_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
        {
            var msg = Encoding.UTF8.GetString(e.Message);
            UpdateLog(msg);
            SetToDataBase(msg, e.Topic); // 실제 DB에 저장 처리
        }

        // DB 저장처리 메서드
        private void SetToDataBase(string msg, string topic)
        {
            var currValue = JsonConvert.DeserializeObject<Dictionary<string, string>>(msg);
            if(currValue != null)
            {
                Debug.WriteLine(currValue["Home_Id"]);
                Debug.WriteLine(currValue["Room_Name"]);
                Debug.WriteLine(currValue["Sensing_DateTime"]);
                Debug.WriteLine(currValue["Temp"]);
                Debug.WriteLine(currValue["Humid"]);

            }
        }
    }
}
