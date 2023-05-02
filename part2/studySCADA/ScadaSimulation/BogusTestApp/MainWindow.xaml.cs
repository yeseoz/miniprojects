﻿using BogusTestApp.Models;
using MahApps.Metro.Controls;
using Newtonsoft.Json;

namespace BogusTestApp
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

        private void BtnGenDummyData_Click(object sender, System.Windows.RoutedEventArgs e)
        {
            var repo = new SampleCustomerRepository();
            var customers = repo.GetCustomers();
            var result = JsonConvert.SerializeObject(customers,Formatting.Indented);
            RtbResult.Text = result;
        }
    }
}
