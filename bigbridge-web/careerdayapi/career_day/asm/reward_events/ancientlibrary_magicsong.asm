hirom

org $C99E3A

db $C8, $2E, $08                ;Display Message/Text/Dialogue 2E 08
db $B4, $29                     ;Play Background Music Fanfare 1 (short)
db $39                          ;Player pose: face down, both arms raised
db $E4, $C9                     ;Unknown
db $48                          ;Player pose: garbage
db $0F                          ;<Unknown>
db $DE, $1C				; set up reward
db $DF					; call text handler
db $A4, $51                     ;Turn on bit 02 at address 0x7e0a3e
db $FF                          ;End Event

pad $C99E4C