cipher = 'U8Y]:8KdJHTXRI>XU#?!K_ecJH]kJG*bRH7YJH7YSH]*=93dVZ3^S8*$:8"&:9U]RH;g=8Y!U92'

def decoding(cipher):
    '''try to decoding cipher and show all result'''
    def transform(key):
        for alpha in key:
            beta = key[alpha]
            beta = chr(ord(beta) + 1)
            if ord(beta) > ord('Z'):
                beta = 'A'
            key[alpha] = beta
        return key

    key = {}
    cipherTest = ''
    for alpha in range(ord('A'), ord('A')+26):
        key[chr(alpha)] = chr(alpha)
    for i in range(26):
        cipherTest = ''
        for j in range(len(cipher)):
            cipherTest += key[cipher[j]]
        key = transform(key)
        print('{0:2} : {1}'.format(i, cipherTest))

decoding(cipher)