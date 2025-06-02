alphabet= "abcdefghijklmnopqrstuvwxyz"
key = 'GYSMNASTIQUES'.lower()
ciphered = "Kl qsfwm, r'qc hm s'ynfefmmh wej rc peahxik xi eg lmgigg i uni voqevmmem fuv vkq srnk jcy psmryurnl yiyli hkppee ehv fuck ! Syuf ahkmi orw rmztuw kmsbijifq, w'aa xvvcr ha jq eelkwkpij. Rc hbiub : 404KJZ{RwBmxrzHtaBywVxybramqAlj}"
kord = [71, 89, 83, 77, 78, 65, 83, 84, 73, 81, 85, 69, 83]

for offset in range(13):

    deciphered = []
    i = 0 + offset  
    for enum, c in enumerate(ciphered.lower()):

        if c.isalpha():
            k = key[ i % len(key) ]
            d = alphabet[ (ord(c) - ord(k)) % 26 ]


            if c.isalpha() and ciphered[enum].isupper():
                d = d.upper()

            deciphered.append( d )
            i += 1
        else:    
            deciphered.append( c )

    print( ''.join(deciphered) )


# 404CTF{NeVolezPasLesDrapeauxSvp}
 