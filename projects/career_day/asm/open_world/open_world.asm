hirom


; These are for permanent changes to open world


; TYCOON CASTLE
; Move the guard out of the way of the vault

org $CE685A
db $15

; ZOKK
; First Zokk cutscene flag off
org $F04B4E
db $FB, $FB
org $F0574B
db $FB, $FB
org $F05752
db $FB, $FB

; RIFT
; Stop Omega from moving
org $CE992B
db $04

; ANCIENT LIBRARY
; Change flag for checking cid mid event
;org $D8EF42
org $F04EC2
db $EE


; SYLDRA
; Change Syldra's event to be tied to $A2, $11  ($7E0A16 bit 02), which is 
; Early game Pirate cave access. Could be a quasi-key item later 
; org $D8EC45
org $F04BC5
db $11


; MUA FOREST
; Change checked flag from event code $A2, $71 to $A2, $72 ($000A22 bit 04 instead of 02)
; The reason for this is that $A22 bit 02 is connected to both guido and mua forest
; BUt Bit 04 is specifically tied to the fast 'reentrance' of mua forest
; So we can isolate mua forest as its own area, and guido can remain $A22 bit 02
; This code specifically means when Mua forest is looking for the bit, it's now checking 04 instead of 02 at $A22
; org $D8F18E
org $F0510E
db $72

; MOOGLE VILLAGE
; Event code [$A4, $3C] or setting bit 10 on $000A3B corresponds to both Tyrasaur being defeated and Moogle Village being open
; This fix allows for Tyrasaur to remain on $000A3B bit 10, while Moogle Village is swapped to another bit usually set upon 
; Finishing the Tyrasaur sequence, immediately set on new game ([$A4, $C1], or $000A4C bit 02)
;org $D8EF5C
org $F04EDC
db $C1                     ;Refer to event code [$A4, $C1]


; MOOGLE WATERWAY
; For some reason, $000A1F bit 40 (event [$A2, $5E]) is both tied to the pre-Tyrasaur cutscene (not the pre-battle cutscene, the cutscene before that) and the barrier for Exdeath's castle
; This will disable the waterway cutscene from checking that bit, so it's left only to be barrier related
; We set it to check a bit that we ALWAYS know will be set, which is event code $A2, $10 from starting_flags 
; this is address $000A16 bit $10

;org $D8F632
org $F055B2
db $10


; ZEZA FLEET
; After Gilgamesh, change one of the flags for Hiryuu spawning to normal to be based off of:
; db $A2, $AA                     ;Turn on bit 04 at address 0x7e0a29
; instead of 
; db $A2, $6D                     ;Turn on bit 20 at address 0x7e0a21
; Which is tied to Zeza allowing access to Barrier Tower
; org $D8F254
org $F051D4
db $AA

; BARRIER TOWER
; Similar to above, change barrier tower fight cutscene to deactivate from a different flag than the underwater barrier access warp tile
; org $D8F37D
org $F052FD
db $FD, $7C

; FORK TOWER
; Galuf in party causes problems. Temporarily setting access after Mua forest boss → getting Cara
; Bit 80 at address 0x7e0a4b

; org $D8F85A
org $F057DA
db $BF


; ANTLION
; Moved antlion's area tile up 1 into the river.
; This makes it so the player can only access as Boco, which avoids the regular situation forcing the player
; to be on Boco by walking on the world map (instead of accessing with Boco like vanilla)
org $CE2869 ; this changes tile
db $57
org $C8B218 ; this changes leaving cutscene to place Boco one tile right of this 
db $7A


; PYRAMID W3
; Disable conditional event for pyramid cutscene. Reused for world warps 
; This disables X Y coords and replicates the previous xy checker to overwrite
org $CE288C
db $AD, $E9, $F0, $01


; GARGOYLES
; Change each conditional event to have individual flags associated with their respective key items
; Only works for pyramid, the others had to be custom 
; Pyramid
; org $D8F3E7
org $F05367
db $BC

; Solitary Shrine
; org $D8FC64
; db $FC, $BB


; FINAL EXDEATH
; Always trigger the cutscene for the final fight
org $F05D3D
db $FF, $85, $07