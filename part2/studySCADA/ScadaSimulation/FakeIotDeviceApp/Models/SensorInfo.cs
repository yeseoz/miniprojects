using System;

namespace FakeIotDeviceApp.Models
{
    public class SensorInfo
    {
        public string Home_Id { get; set; } //D101H101  101-101~104, 201~204...
        public string Room_Name { get; set; } // Living, Dining, Bed, Bath
        public DateTime Sensing_DateTime { get; set; } // 시 분 초
        public float Temp { get; set; } // 온도
        public float Humid { get; set; } // 습도
    }
}
