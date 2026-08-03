#write a program that converts seconds into hours, minutes, and seconds
total_sec = int(input("Enter time n seconds: "))
if total_sec < 0:
   print("error")
else:
   hours = total_sec // 3600
   minutes = (total_sec // 3600) // 60
   seconds = total_sec % 60
   print("Total hours =" , f"{hours} hours , {minutes} minutes , {seconds} seconds")
