
; WarpShard text
org $D11BDE
db $76, $7A, $8B, $89, $72, $81, $7A, $8B, $7D

; change text in config menu
org $E73d0E
db $64, $87, $7C, $88, $8E, $87, $8D, $7E, $8B, $8C ; "Encounters"
org $E73215
db $64, $87, $7C, $88, $8E, $87, $8D, $7E, $8B, $8C ; "Encounters"
org $E731DB
; "Rwd Mult"
db $71, $90, $7D, $96, $6C, $8E, $85, $8D, $D2


org $E730E1 ; "Rare" → "Key"
db $6a, $7e, $92, $96

  
