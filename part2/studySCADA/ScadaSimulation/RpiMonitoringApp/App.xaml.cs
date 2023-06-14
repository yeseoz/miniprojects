using ControlzEx.Theming;
using System.Windows;

namespace SmartHomeMonitoringApp
{
    /// <summary>
    /// App.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);

            ThemeManager.Current.ChangeTheme(this, "Dark.Red");
        }
    }
}
