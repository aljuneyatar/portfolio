from time import sleep
import sys

def print_lyrics():
   
    lines = [
        ("A flower is not a flower until they bloom", 0.08),
        ("Like my first time living life the day I met you", 0.06),
        ("Hate to think that humans have to die someday", 0.07),
        ("A thousand years won't do ooh...", 0.08),
        ("No wonder I fell in love", 0.06),
        ("Even though I'm scared to love ", 0.05),
        ("Baby I know the pain is unbearable", 0.07),
        ("There's no way", 0.07),
        ("Pinsala'y ikinamada", 0.07),
        ("Oh binibining may salamangka", 0.07),
        ("You've turned my limbics into a bouquet", 0.07),
        ("Ikaw ay tila sining sa museong 'di naluluma", 0.10),
        ("Binibini kong ginto hanggang kaluluwa", 0.10,),
        ("Gonna keep you like the nu couché", 0.08),
        ("All my life...", 0.21)
        
    ]

    delays = [1, 1, 0.8, 2.0, 0.5, 0.2, 0.3, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    for i, (line, char_delay) in enumerate(lines):
       
        for char in line:
            print(char, end='')
            sys.stdout.flush() 
            sleep(char_delay)
        
        print()  
        sleep(delays[i]) 

print_lyrics()