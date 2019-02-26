bitset = {}
bitset['01'] = 0
bitset['02'] = 1
bitset['04'] = 2
bitset['08'] = 3
bitset['10'] = 4
bitset['20'] = 5
bitset['40'] = 6
bitset['80'] = 7

bitsetnum = {}
bitsetnum[7] = '01'
bitsetnum[6] = '02'
bitsetnum[5] = '04'
bitsetnum[4] = '08'
bitsetnum[3] = '10'
bitsetnum[2] = '20'
bitsetnum[1] = '40'
bitsetnum[0] = '80'


#address = input("Input address: ")
#bit = input("Input byte: ")
#type_set = input("Input on/off: ")
address = 'AF0'
bit = '80'
type_set = 'on'
def encrypt(address,bit,type_set):
    if "7E0" in address:
        address = address.replace("7E0","000")
    
    if len (address) <= 3:
        address = '000' + address.upper()
    else:
        address = address.upper()
        
    address_dec = int(address,base=16)
        
    
    A2A3 = int('000A34',base=16)
    A4A5 = int('000A54',base=16)
    
    if int(address,base=16) < A2A3:
        base = int('000A14',base=16)
        delta = ((address_dec - base) * 8) + bitset[bit]
        delta = hex(delta).replace("0x","$")
        if type_set == 'on':
            print("db $A2, "+delta.upper()+"            ; set address "+address+" bit ON "+bit)
        if type_set == 'off':
            print("db $A3, "+delta.upper()+"            ; set address "+address+" bit OFF "+bit)
            
    elif int(address,base=16) < A4A5:
        base = int('000A34',base=16)
        delta = ((address_dec - base) * 8) + bitset[bit]
        delta = hex(delta).replace("0x","$")
        if type_set == 'on':
            print("db $A4, "+delta.upper()+"            ; set address "+address+" bit ON "+bit)
        if type_set == 'off':
            print("db $A5, "+delta.upper()+"            ; set address "+address+" bit OFF "+bit)
            
    else:
        base = int('000A54',base=16)
        delta = ((address_dec - base) * 8) + bitset[bit]
        delta_divide = int(delta / 256)
        if delta_divide >= 1:
            arg1 = hex(int(delta_divide)).replace("0x","")
            if len(arg1) == 1:
                arg1 = '0' + arg1 
            base = base + (int('000020',base=16) * (int(delta_divide)))
            delta = ((address_dec - base) * 8) + bitset[bit]
        else:
            arg1 = '00'
        delta = hex(delta).replace("0x","")
        if len(delta)==1:
            delta = "0" + delta 
        if type_set == 'on':
            print("db $CA, $"+delta.upper()+", $"+arg1.upper()+"            ; set address "+address+" bit ON "+bit)
        if type_set == 'off':
            print("db $CB, $"+delta.upper()+", $"+arg1.upper()+"            ; set address "+address+" bit OFF "+bit)
            
            
            
            
            
            
            
            
            
            
            
            
            
before_text = """
00000000000000000000000000000000
0000000000003b300000000ac0a00093
95482400000000000000000100000000
000000000000003c28300c3000100000
0000000000000000000000c0d0000010
0783008400bffe7fdbd62bc7ff7f404e
ff757fb9f4feff93ffff0f80afe7fc82
814becc0ff197078ffff03d8feffe9ff
ff0b0400fdfefffffffffff0ff03ff6f
3fa6df23fcc38f7fffffff3f0f3e019f
fdf4ffd7ffffffdffdc7ff0103fef0c7
7ffe17000ff801000080bfbf0f180000
fffffe9ff0fffffcffff000000000000
"""

after_text = """
00000000000000000000000000000000
0000000000003b300000000ac0a00093
95482400000000000000f80100000000
000000000000003c28300c3000100000
0000000000000000000000c0d0000010
0783008400bffe7fdbd62bc7ff7f404e
ff757fb9f4feff93ffff0f80afe7fc82
814bece0ff197078ffff03d8feffe9ff
ff0b0400fdfefffffffffff0ff03ff6f
3fa6df23fcc38f7fffffff3f0f3e019f
fdf4ffd7ffffffdffdc7ff0103fef0c7
7ffe17000ff801000080bfbf0f180000
fffffe9ff0fffffcffff000000000000
"""





before_text = before_text.replace("\n","")
after_text = after_text.replace("\n","")

og_base = int('A00',base=16)
num = 0
list_of_flags = []
while num <int(len(before_text)):

    before = before_text[num:num+2]
    after = after_text[num:num+2]
    if before != after:
        #print("Delta at "+str(num))
        before_dec = int(before,base=16)
        after_dec = int(after,base=16)
        bits_to_set = abs(before_dec - after_dec)
        
        
        before_bits = bin(before_dec).replace("0b","").zfill(8)
        after_bits = bin(after_dec).replace("0b","").zfill(8)
        
        bitnum = 0
        while bitnum < len(before_bits):
            before_bitnum = int(before_bits[bitnum:bitnum+1])
            after_bitnum = int(after_bits[bitnum:bitnum+1])
            if before_bitnum != after_bitnum:
                if before_bitnum < after_bitnum :
                    type_set = "on"
                else:
                    type_set = "off"    
                #print(hex(og_base +int(num/2))+ " Bit to set: "+bitsetnum[bitnum]+" "+type_set)
                list_of_flags.append([hex(og_base +int(num/2)).replace("0x","000"),bitsetnum[bitnum],type_set])
            bitnum = bitnum + 1
        
    num = num + 2
for collection in list_of_flags:
    encrypt(collection[0],collection[1],collection[2])