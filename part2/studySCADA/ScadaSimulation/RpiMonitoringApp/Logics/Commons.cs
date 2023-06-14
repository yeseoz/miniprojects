using MahApps.Metro.Controls;
using MahApps.Metro.Controls.Dialogs;
using System.Threading.Tasks;
using System.Windows;
using uPLibrary.Networking.M2Mqtt;

namespace SmartHomeMonitoringApp.Logics
{
    public class Commons
    {
        // 화면마다 공유할 MQTT 브로커 ip변수
        public static string BROKERHOST { get; set; } = "210.119.12.55";
        public static string MQTTTOPIC { get; set; } = "pknu/rpi/control/";
        public static string MYSQL_CONNSTRING { get; set; } = "Server=localhost;" +
                                                              "Port=3306;" +
                                                              "Database=miniproject;" +
                                                              "Uid=root;" +
                                                              "Pwd=12345";

        // MQTT 클라이언트 공용 객체(DB모니터링에도 쓰고 RealTime에도 쓸꺼라서 공용으로 만듬)
        public static MqttClient MQTT_CLIENT { get; set; }

        // userControl같이 자식 클래스면서 MetroWindow를 직접사용하지 않아, MahApps.Metro에 있는 Metro메시지창을 사용하지 못할때
        // 없으면 사용할 수 없음..ㅠ
        public static async Task<MessageDialogResult> ShowCustomMessageAsync(string title, string message,
            MessageDialogStyle style = MessageDialogStyle.Affirmative)
        {
            return await ((MetroWindow)Application.Current.MainWindow).ShowMessageAsync(title, message, style, null);
        }
    }
}
