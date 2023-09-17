from market.macro.plotviz_economic_indicator import PlotEconomicIdx

class ISM:
    @staticmethod
    def service_descr():
        return """ISM 서비스 보고서
50% 이상: 기업 활동의 증가
50% 이하 :기업활동 수축을 의미 한다.

[비용, PRICES]
인플레이션 위협이 점점 더 심각한 수준에 이르고 있는지 여부에 관한 경고 역할을 할 수 있다.
서비스 및 자재구입 비용이 모두 포함되기 때문에, 엄밀히 말해 이것을 인플레이션 지표로 여길 수는 없지만,
일반적으로 3개월 이상 60%를 초과하면 인플레이션이 급상승할 가능성이 있다고 해석할 수 있다.

[고용, EMPLOYMENT]
서비스 부문의 고용이 경제 전체의 고용에서 약 80%의 비중을 차지한다는 점 때문에 노동 시장 현황에 대한 선행지표로 간주되기도 한다.
"""



    @staticmethod
    def manufactoring0_descr():
        return """ISM 제조업 보고서
[채권 시장]
일반적으로 ISM 제조업 지수가 50% 이상을 유지할 때, 특히 경기가 확장국면에 있을 대 채권시장의 약세를 예상하는데, 이러한 상황이 인플레이션 압력을 심화시키고 그 결과로 금리인상을 초래할 수 있기 때문이다.
반면 이 지수가 45%와 50% 사이에 위치해 있다면 채권 시장이 동요할 가능성은 적어진다.
그러나 45% 이하를 가리키면 제조업과 경제 전반이 심각한 약화를 경험하고 있다고 해석해도 무방하며, 채권 시장은 활기를 띌 수 있다.

[주식 시장]
지수 상승에 긍정적으로 반응하는데, 이러한 경향을 미약한 경제성장기에 두드러진다.
경제가 이미 최고점에 도달해 있는 상황에서 이 지수가 급상승하면 경기 과열 우려로 주가 급락을 불러올 수도 있다.

[외환 시장]
지수가 50% 이상을 가리키면 달러가치가 급등할 가능성이 커진다.
역으로 불황을 암시한다면 달러화 연동 투자물의 일부를 매각함으로써 달러 가치가 기타 주요 통화 대비 하락할 수 있다.
"""

    @staticmethod
    def manufactoring1_descr():
        return """ISM 제조업 보고서
이 지수가 50%에서 1%증가할 때 마다 실질 GDP는 전년 대비 약 0.3% 추가 성장 한다고 본다
50 이상: 제조업과 경제가 모두 성장 중이다.
50 미만 41.1 이상: 제조업 활동은 수축하고 있으나 경제는 전반적으로 여전히 성장 중일 수 있다.
41.1미만: 제조업과 경제 모두 후퇴기에 접어들었을 가능성이 크다. 이때 FED는 경제 성장을 촉진시키지 위해 금리 인하 조치를 취할 가능성이 크다.

[신규 주문, New order]
신규 주문 급증은 보통 몇 달 후 생산 증가로 이어진다.
    
[고용, EMPLOYMENT]
기업의 신규 노동자 고용 또는 해고 여부를 판단할 때 반드시 주목해야 하는 내용이다.

[공급자 운송(공급자 효율), SUPPLIER DELIVERIES]
구매관리자가 자재 주문 시 경험하는 공급자 운송 시간의 변화를 추적하고 있다.
이 지수가 50%에 가까워지거나 그 이상을 가리키면, 구매관리자가 자재들을 공급받기 위해 전보다 더 오랜 시간을 기다려야 한다는 것으로 해석할수 있으며, 수요가 급증할 때 발생하는 경우가 많다.
이런 상황에서는 가격 결정이 주문자가 아닌 공급자들에 의해 좌우될 가능성이 크며, 인플레이션에 대한 새로운 우려를 야기할 수 있다.    

[고객재고, CUSTOMERS' INVENTORIES]
지수가 높을수록 재고 증가에 불만을 갖는 고객이 많아져 신규주문을 할 가능성이 낮아지게 되고 가까운 시일 내에 공장은 생산 속도가 감소할 수 있다.
구매관리자들은 고객 재고 지수가 50% 이하로 떨어지는 상황을 긍정적으로 받아들인다.  

[비용지수, PRICES]
제조업체들이 자재에 지불하는 비용의 변화를 반영
생산의 초기단계에 인플레이션이 가속화하고 있는지 여부를 보여준다.
비용지수가 65% 이상을 유지하면 FED가 금리를 인상하게 될 가능성이 커진다.

[신규수출주문, NEW EXPORT ORDERS]
해외로부터의 주문 급증은 국내 제조업을 부양시키고 고용을 촉진하며 GDP 성장을 자극하는 역할을 하기도 하는 반면,
미국 내의 구매자들이 미국산 제품과 자원을 놓고 외국 구매자들과 경쟁을 벌여야 하는 상황이 벌어짐에 따라 인플레이션 상승 압력 발생하기도 한다.
미국과 세계 경제가 동시에 활발한 성장세를 보이고 있는 상황에서는 높은 수준으로 뛰어오를 수 있다.
"""

    @staticmethod
    def ism_ReportOnBusiness():
        return "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business"