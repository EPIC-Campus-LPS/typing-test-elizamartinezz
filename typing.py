import time
start = time.time()
hello = input("Type: The quick brown fox jumps over the lazy dog. Also I think Eliza Martinez is really cool")
end = time.time()
words = 17 / 60
new_time = end - start
round = round(new_time, 2)
print("This took you: " + str(new_time))
