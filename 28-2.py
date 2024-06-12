import numpy_financial as npf


future_value = 15692.93 
PMT = 100  
annual_rate = 0.05  
monthly_rate = annual_rate / 12  
n = 10 * 12  


PV = npf.pv(monthly_rate, n, -PMT, future_value)

print(PV)