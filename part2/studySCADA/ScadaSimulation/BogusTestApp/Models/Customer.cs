using System;
using System.Collections.Generic;

namespace BogusTestApp.Models
{
    public class Customer // 고객 테이블 매핑 
    {
        public Guid ID { get; set; }
        public string Name { get; set; } // 고객 이름
        public string Address { get; set; } // 고객 주소
        public string Phone { get; set; } // 고객 번호
        public string ContactName { get; set; } // 고객 연락처명
        public IEnumerable<Order> Orders { get; set; } // 주문한 리스트

    }
}
