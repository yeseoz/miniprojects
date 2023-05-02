using System;

namespace BogusTestApp.Models
{
    public class Order
    {
        public Guid ID { get; set; }        // Guid 유니크한 아이디를 만들어줌
        public DateTime Date { get; set; } // 주문일자
        public decimal OrderValue { get; set; } // 주문 갯수
        public bool Shipped { get; set; } // 선적여부
    }
}
