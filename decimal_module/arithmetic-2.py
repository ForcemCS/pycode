import decimal
from  decimal import Decimal


##code1
curret_rounding = decimal.getcontext().rounding

decimal.getcontext().rounding  = decimal.ROUND_UP
print(round(Decimal('1.445'),2))
decimal.getcontext().rounding  = decimal.ROUND_HALF_EVEN
print(round(Decimal('1.445'),2))

##code2

print("Before:", decimal.getcontext())

with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    ctx.prec = 6
    
    print("Local context :",ctx )
    print(round(Decimal('1.445'),2))
print(round(Decimal('1.445'),2))
    
