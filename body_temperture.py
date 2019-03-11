import Adafruit_DHT

while(1):
  h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
  print('TEMPERATURE :{0:0.1f}'.format(t))
  
