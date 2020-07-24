decibal= int(input())
if decibal>=130:
  print("Jackhammer")
elif decibal>=106 and decibal<=129:
  print("Gas lawnmower")
elif decibal>=41 and decibal<=105:
  print("Alarm clock")
else:
  print("Quiet room")