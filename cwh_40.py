ch = input("Code or Decode? ")
msg = input("Enter message: ")
if ch=="code":
    if len(msg)<3:
        print("Coded: ",msg[:-1])
    else:
        code = "mnk"+msg[1:]+msg[0]+"dsk"
        print("Coded:",code)
elif ch=="decode":
    if len(msg)<3:
        print("Decoded:",msg[:-1])
    else:
        msg = msg[3:-3]
        decode = msg[-1]+msg[:-1]
        print("Decoded:", decode)
else:
    print("Invalid choice")