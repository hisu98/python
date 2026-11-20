# 실습 1
# 1번
log = " [WARNing] "
print(log.strip(" []").upper()) # WARNING
print(log.upper()[2:9])
# 2번
sensors = 'temp,pressure,vibration'
print(" / ".join(sensors.upper().split(",")[::-1])) # VIBRATION / PRESSURE / TEMP
# 3번
data = " EQP-01 , NORMAL , 85.5 "
print(data.split(",")[1].strip().lower()) # normal
# 4번
text = " ###[PUMP-07]### "
print(text.strip(" #[]").lower().replace("-","_")) # pump_07
# 5번
data = " TEMP / Pressure | vibration "
print(data.replace(" / ",",").replace(" | ",",").lower().strip()) 
# temp,pressure,vibration