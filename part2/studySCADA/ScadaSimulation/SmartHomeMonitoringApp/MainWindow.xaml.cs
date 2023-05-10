﻿using MahApps.Metro.Controls;
using System;
using System.Windows;
using System.Diagnostics;
using SmartHomeMonitoringApp.Views;
using MahApps.Metro.Controls.Dialogs;
using SmartHomeMonitoringApp.Logics;

namespace SmartHomeMonitoringApp
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void MetroWindow_Loaded(object sender, RoutedEventArgs e)
        {
            // <Frame> ==> Page.xaml
            // <ContentControl> ==> UserControl.xaml 
            //ActiveItem.Content = new Views.DataBaseControl();
        }

        // 끝내기 버튼 클릭이벤트 핸들러
        private void MnuExitProgram_Click(object sender, RoutedEventArgs e)
        {
            Process.GetCurrentProcess().Kill();  // 작업관리자에서 프로세스 종료!
            Environment.Exit(0); // 둘중하나만 쓰면 됨
        }

        // MQTT 시작메뉴 클릭이벤트 핸들러
        private void MnuStartSubscribe_Click(object sender, RoutedEventArgs e)
        {
            var mqttPopWin = new MqttPopupWindow();
            mqttPopWin.Owner = this;
            mqttPopWin.WindowStartupLocation = WindowStartupLocation.CenterOwner;
            var result = mqttPopWin.ShowDialog();

            if(result == true)
            {
                var userControl = new Views.DataBaseControl();
                ActiveItem.Content = userControl;
                StsSelScreen.Content = "DataBase Monitoring"; 
                //typeof(Views.DataBaseControl);
            }
        }

        private async void MetroWindow_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            e.Cancel = true;

            var mySettings = new MetroDialogSettings
            {
                AffirmativeButtonText = "끝내기", // 확인
                NegativeButtonText = "취소",
                AnimateShow = true,
                AnimateHide = true,
            };

            var result = await this.ShowMessageAsync("프로그램 끝내기", "프로그램을 끝내시겠습니까?",
                                                      MessageDialogStyle.AffirmativeAndNegative, mySettings);

            if(result== MessageDialogResult.Negative)
            {
                e.Cancel = true;
            }
            else if(result == MessageDialogResult.Affirmative)
            {
                if (Commons.MQTT_CLIENT != null && Commons.MQTT_CLIENT.IsConnected)
                {
                    Commons.MQTT_CLIENT.Disconnect();
                }
                Process.GetCurrentProcess().Kill(); // 가장 확실한 종료 방법
            }
        }

        private void BtnExitProgram_Click(object sender, RoutedEventArgs e)
        {
            // 확인메시지 윈도우 클로징 이벤트 핸들러 호출
            this.MetroWindow_Closing(sender,new System.ComponentModel.CancelEventArgs());
        }

        private void MnuDataBaseMon_Click(object sender, RoutedEventArgs e)
        {
            var userControl = new Views.DataBaseControl();
            ActiveItem.Content = userControl;
            StsSelScreen.Content = "DataBase Monitoring";
            //typeof(Views.DataBaseControl);
        }

        private void MnuRealTimeMon_Click(object sender, RoutedEventArgs e)
        {
            //var userControl = new Views.DataBaseControl();
            //ActiveItem.Content = userControl; // 아랫줄과 동일
            ActiveItem.Content = new Views.RealTimeControl();
            StsSelScreen.Content = "RealTime Monitoring";
        }

        private void MnuVisualizationMon_Click(object sender, RoutedEventArgs e)
        {
            ActiveItem.Content=new Views.VisualizationControl();
            StsSelScreen.Content = "Visualization View";
        }
    }
}
