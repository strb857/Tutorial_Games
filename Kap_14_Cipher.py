#Ceasar Cipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö'
#Mer avancerad symbolsamling inkl shuffle:
#SYMBOLS = 'rnc@"_]xb2-WjPIkgl}oÅdäTCUB#¥J49f1a*¤KDh,M></\ötvNiQÄÖG)V$å.3&q%HXs6LYAm7F;{Z=?zOEp(8[ €0SuyR£:ew!5'

MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Vill du (k)ryptera, (d)ekryptera eller genomföra en (b)rute-force?')
        mode = input().lower()
        if mode in ('kryptera', 'k', 'dekryptera', 'd', 'brute-force', 'b'):
            return mode
        else:
            print('Skriv "k"/"d"/"b".')
            
def getMessage():
    print('Skriv ditt meddelande:')
    return input()

def getKey():
    key = 0
    while True:
        print('Välj nyckel (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key
        
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Symbol not found in SYMBOLS
            # Just add symbol w/out change
            translated += symbol
        else:
            #encrypt or decrypt
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
                    
            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Ditt meddelande lyder:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))

