using Bogus;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace BogusTestApp.Models
{
    public class SampleCustomerRepository
    {
        public IEnumerable<Customer> GetCustomers()
        {
            Randomizer.Seed = new Random(123456); // Seed 갯수를 지정 123456은 마음대로 지정가능
            // 아래와 같은 규칙으로 주문 더미데이터를 만들겠다.
            var orderGen = new Faker<Order>()
                .RuleFor(o => o.ID, Guid.NewGuid) // ID 값은 GUID로 자동생성
                .RuleFor(o => o.Date, f => f.Date.Past(3)) // 날짜를 3년전으로 셋팅 생성
                .RuleFor(o => o.OrderValue, f => f.Finance.Amount(1, 10000)) // 1부터 10000까지 숫자 중에서 랜덤하게 세팅
                .RuleFor(o => o.Shipped, f => f.Random.Bool(0.8f)); // 80% true
                                                                    //0.5f라면 true/false가 반반

            // 고객 더미데이터 생성 규칙
            var customerGen = new Faker<Customer>()
                .RuleFor(c => c.ID, Guid.NewGuid())
                .RuleFor(c => c.Name, f => f.Company.CompanyName()) // 자기가 알아서 만들어줌
                .RuleFor(c => c.Address, f => f.Address.FullAddress())
                .RuleFor(c => c.Phone, f => f.Phone.PhoneNumber())
                .RuleFor(c => c.ContactName, f => f.Name.FullName())
                .RuleFor(c => c.Orders, f => orderGen.Generate(f.Random.Number(1, 2)).ToList()); // 주문갯수가 1또는 2

            return customerGen.Generate(10); // 10개의 가짜 고객데이터를 생성, 리턴
        }
    }
}
