import time
import sys
import string

def animate_string(target):
    current = ""
    all_chars = string.printable  

    for i in range(len(target)):
        if target[i] in string.whitespace:
            current += target[i]
            print(f"\r{current:<{len(target)}}", end="", flush=True)
            time.sleep(0.1)  
            continue
        
        for char in all_chars:
            test_string = current + char + 'a' * (len(target) - len(current) - 1)
            print(f"\r{test_string:<{len(target)}}", end="", flush=True)
            time.sleep(0.01)  
            
            if char == target[i]:
                current += char
                time.sleep(0.05)  
                break
        
        if len(current) == len(target):
            break
    
    print()

if __name__ == "__main__":
    animate_string("Hello, World!")
    animate_string("Python 3.9 is awesome!")
    animate_string("100% working with numbers & special chars!")
    animate_string("I am amphibiar and this is the program kill.py")