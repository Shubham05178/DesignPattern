from DiscountService import DiscountService
from DiwaliDiscount import DiwaliDiscount
from FirstOrderDiscount import FirstOrderDiscount
rs=12989
a=DiscountService(DiwaliDiscount())
print("DiwaliDiscount:",a.cal_dis(rs))
a=DiscountService(FirstOrderDiscount())
print("FirstOrderDiscount",a.cal_dis(rs))