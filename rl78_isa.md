## ADD

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ADD A, #byte        | 2 | 1 | × | × | × | A, CY ← A + byte
ADD saddr, #byte    | 3 | 2 | × | × | × | (saddr), CY ← (saddr) + byte
ADD X, A            | 2 | 1 | × | × | × | X, CY ← X + A
ADD B, A            | 2 | 1 | × | × | × | B, CY ← B + A
ADD C, A            | 2 | 1 | × | × | × | C, CY ← C + A
ADD D, A            | 2 | 1 | × | × | × | D, CY ← D + A
ADD E, A            | 2 | 1 | × | × | × | E, CY ← E + A
ADD H, A            | 2 | 1 | × | × | × | H, CY ← H + A
ADD L, A            | 2 | 1 | × | × | × | L, CY ← L + A
ADD A, X            | 2 | 1 | × | × | × | A, CY ← A + X
ADD A, B            | 2 | 1 | × | × | × | A, CY ← A + B
ADD A, C            | 2 | 1 | × | × | × | A, CY ← A + C
ADD A, D            | 2 | 1 | × | × | × | A, CY ← A + D
ADD A, E            | 2 | 1 | × | × | × | A, CY ← A + E
ADD A, H            | 2 | 1 | × | × | × | A, CY ← A + H
ADD A, L            | 2 | 1 | × | × | × | A, CY ← A + L
ADD A, saddr        | 2 | 1 | × | × | × | A, CY ← A + (saddr)
ADD A, !addr16      | 3 | 1 | × | × | × | A, CY ← A + (addr16)
ADD A, [HL]         | 1 | 1 | × | × | × | A, CY ← A + (HL)
ADD A, [HL+B]       | 2 | 1 | × | × | × | A, CY ← A + (HL + B)
ADD A, [HL+C]       | 2 | 1 | × | × | × | A, CY ← A + (HL + C)
ADD A, [HL+byte]    | 2 | 1 | × | × | × | A, CY ← A + (HL + byte)
ADD A, ES:!addr16   | 4 | 2 | × | × | × | A, CY ← A + (ES, addr16)
ADD A, ES:[HL]      | 2 | 2 | × | × | × | A, CY ← A + (ES, HL)
ADD A, ES:[HL+B]    | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + B)
ADD A, ES:[HL+C]    | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + C)
ADD A, ES:[HL+byte] | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + byte)

## ADDC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ADDC A, #byte        | 2 | 1 | × | × | × | A, CY ← A + byte + CY
ADDC saddr, #byte    | 3 | 2 | × | × | × | (saddr), CY ← (saddr) + byte + CY
ADDC X, A            | 2 | 1 | × | × | × | X, CY ← X + A + CY
ADDC B, A            | 2 | 1 | × | × | × | B, CY ← B + A + CY
ADDC C, A            | 2 | 1 | × | × | × | C, CY ← C + A + CY
ADDC D, A            | 2 | 1 | × | × | × | D, CY ← D + A + CY
ADDC E, A            | 2 | 1 | × | × | × | E, CY ← E + A + CY
ADDC H, A            | 2 | 1 | × | × | × | H, CY ← H + A + CY
ADDC L, A            | 2 | 1 | × | × | × | L, CY ← L + A + CY
ADDC A, X            | 2 | 1 | × | × | × | A, CY ← A + X + CY
ADDC A, B            | 2 | 1 | × | × | × | A, CY ← A + B + CY
ADDC A, C            | 2 | 1 | × | × | × | A, CY ← A + C + CY
ADDC A, D            | 2 | 1 | × | × | × | A, CY ← A + D + CY
ADDC A, E            | 2 | 1 | × | × | × | A, CY ← A + E + CY
ADDC A, H            | 2 | 1 | × | × | × | A, CY ← A + H + CY
ADDC A, L            | 2 | 1 | × | × | × | A, CY ← A + L + CY
ADDC A, saddr        | 2 | 1 | × | × | × | A, CY ← A + (saddr) + CY
ADDC A, !addr16      | 3 | 1 | × | × | × | A, CY ← A + (addr16) + CY
ADDC A, [HL]         | 1 | 1 | × | × | × | A, CY ← A + (HL) + CY
ADDC A, [HL+B]       | 2 | 1 | × | × | × | A, CY ← A + (HL + B) + CY
ADDC A, [HL+C]       | 2 | 1 | × | × | × | A, CY ← A + (HL + C) + CY
ADDC A, [HL+byte]    | 2 | 1 | × | × | × | A, CY ← A + (HL + byte) + CY
ADDC A, ES:!addr16   | 4 | 2 | × | × | × | A, CY ← A + (ES, addr16) + CY
ADDC A, ES:[HL]      | 2 | 2 | × | × | × | A, CY ← A + (ES, HL) + CY
ADDC A, ES:[HL+B]    | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + B) + CY
ADDC A, ES:[HL+C]    | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + C) + CY
ADDC A, ES:[HL+byte] | 3 | 2 | × | × | × | A, CY ← A + ((ES, HL) + byte) + CY

## ADDW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ADDW SP, #byte        | 2 | 1 |   |   |   | SP ← SP + byte
ADDW AX, #word        | 3 | 1 | × | × | × | AX, CY ← AX + word
ADDW AX, AX           | 1 | 1 | × | × | × | AX, CY ← AX + AX
ADDW AX, BC           | 1 | 1 | × | × | × | AX, CY ← AX + BC
ADDW AX, DE           | 1 | 1 | × | × | × | AX, CY ← AX + DE
ADDW AX, HL           | 1 | 1 | × | × | × | AX, CY ← AX + HL
ADDW AX, saddrp       | 2 | 1 | × | × | × | AX, CY ← AX + (saddrp)
ADDW AX, !addr16      | 3 | 1 | × | × | × | AX, CY ← AX + (addr16)
ADDW AX, [HL+byte]    | 3 | 1 | × | × | × | AX, CY ← AX + (HL + byte)
ADDW AX, ES:!addr16   | 4 | 2 | × | × | × | AX, CY ← AX + (ES, addr16)
ADDW AX, ES:[HL+byte] | 4 | 2 | × | × | × | AX, CY ← AX + ((ES, HL) + byte)

## AND

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
AND A, #byte        | 2 | 1 | × |   |   | A ← A ∧ byte
AND saddr, #byte    | 3 | 2 | × |   |   | (saddr) ← (saddr) ∧ byte
AND X, A            | 2 | 1 | × |   |   | X ← X ∧ A
AND B, A            | 2 | 1 | × |   |   | B ← B ∧ A
AND C, A            | 2 | 1 | × |   |   | C ← C ∧ A
AND D, A            | 2 | 1 | × |   |   | D ← D ∧ A
AND E, A            | 2 | 1 | × |   |   | E ← E ∧ A
AND H, A            | 2 | 1 | × |   |   | H ← H ∧ A
AND L, A            | 2 | 1 | × |   |   | L ← L ∧ A
AND A, X            | 2 | 1 | × |   |   | A ← A ∧ X
AND A, B            | 2 | 1 | × |   |   | A ← A ∧ B
AND A, C            | 2 | 1 | × |   |   | A ← A ∧ C
AND A, D            | 2 | 1 | × |   |   | A ← A ∧ D
AND A, E            | 2 | 1 | × |   |   | A ← A ∧ E
AND A, H            | 2 | 1 | × |   |   | A ← A ∧ H
AND A, L            | 2 | 1 | × |   |   | A ← A ∧ L
AND A, saddr        | 2 | 1 | × |   |   | A ← A ∧ (saddr)
AND A, !addr16      | 3 | 1 | × |   |   | A ← A ∧ (addr16)
AND A, [HL]         | 1 | 1 | × |   |   | A ← A ∧ (HL)
AND A, [HL+B]       | 2 | 1 | × |   |   | A ← A ∧ (HL + B)
AND A, [HL+C]       | 2 | 1 | × |   |   | A ← A ∧ (HL + C)
AND A, [HL+byte]    | 2 | 1 | × |   |   | A ← A ∧ (HL + byte)
AND A, ES:!addr16   | 4 | 2 | × |   |   | A ← A ∧ (ES, addr16)
AND A, ES:[HL]      | 2 | 2 | × |   |   | A ← A ∧ (ES, HL)
AND A, ES:[HL+B]    | 3 | 2 | × |   |   | A ← A ∧ ((ES, HL) + B)
AND A, ES:[HL+C]    | 3 | 2 | × |   |   | A ← A ∧ ((ES, HL) + C)
AND A, ES:[HL+byte] | 3 | 2 | × |   |   | A ← A ∧ ((ES, HL) + byte)

## AND1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
AND1 CY, A.bit       | 2 | 1 |   |   | × | CY ← CY ∧ A.bit
AND1 CY, PSW.bit     | 3 | 1 |   |   | × | CY ← CY ∧ PSW.bit
AND1 CY, sfr.bit     | 3 | 1 |   |   | × | CY ← CY ∧ sfr.bit
AND1 CY, saddr.bit   | 3 | 1 |   |   | × | CY ← CY ∧ (saddr).bit
AND1 CY, [HL].bit    | 2 | 1 |   |   | × | CY ← CY ∧ (HL).bit
AND1 CY, ES:[HL].bit | 3 | 2 |   |   | × | CY ← CY ∧ (ES, HL).bit

## B*

mnemonic | bytes | clocks, T | clocks, F | Z | AC | CY | condition | description
---------|:-----:|:---------:|:---------:|:-:|:--:|:--:|:---------:|------------
1                          |   |   |   |   |   |   |                  |
BR AX                      | 2 | 3 | 3 |   |   |   | (unconditional)  | PC ← CS, AX
BR !addr16                 | 3 | 3 | 3 |   |   |   | (unconditional)  | PC ← 0000, addr16
BR $addr20                 | 2 | 3 | 3 |   |   |   | (unconditional)  | PC ← PC+2 + jdisp8
BR $!addr20                | 3 | 3 | 3 |   |   |   | (unconditional)  | PC ← PC+3 + jdisp16
BR !!addr20                | 4 | 3 | 3 |   |   |   | (unconditional)  | PC ← addr20
2                          |   |   |   |   |   |   |                  |
BTCLR A.bit, $addr20       | 3 | 5 | 3 |   |   |   | A.bit = 1        | PC ← PC+3 + jdisp8, A.bit ← 0
BTCLR PSW.bit, $addr20     | 4 | 5 | 3 | × | × | × | PSW.bit = 1      | PC ← PC+4 + jdisp8, PSW.bit ← 0
BTCLR sfr.bit, $addr20     | 4 | 5 | 3 |   |   |   | sfr.bit = 1      | PC ← PC+4 + jdisp8, sfr.bit ← 0
BTCLR saddr.bit, $addr20   | 4 | 5 | 3 |   |   |   | saddr.bit = 1    | PC ← PC+4 + jdisp8, saddr.bit ← 0
BTCLR [HL].bit, $addr20    | 3 | 5 | 3 |   |   |   | (HL).bit = 1     | PC ← PC+3 + jdisp8, (HL).bit ← 0
BTCLR ES:[HL].bit, $addr20 | 4 | 6 | 4 |   |   |   | (ES, HL).bit = 1 | PC ← PC+4 + jdisp8, (ES, HL).bit ← 0
3                          |   |   |   |   |   |   |                  |
BT A.bit, $addr20          | 3 | 5 | 3 |   |   |   | A.bit = 1        | PC ← PC+3 + jdisp8
BT PSW.bit, $addr20        | 4 | 5 | 3 |   |   |   | PSW.bit = 1      | PC ← PC+4 + jdisp8
BT sfr.bit, $addr20        | 4 | 5 | 3 |   |   |   | sfr.bit = 1      | PC ← PC+4 + jdisp8
BT saddr.bit, $addr20      | 4 | 5 | 3 |   |   |   | saddr.bit = 1    | PC ← PC+4 + jdisp8
BT [HL].bit, $addr20       | 3 | 5 | 3 |   |   |   | (HL).bit = 1     | PC ← PC+3 + jdisp8
BT ES:[HL].bit, $addr20    | 4 | 6 | 4 |   |   |   | (ES, HL).bit = 1 | PC ← PC+4 + jdisp8
4                          |   |   |   |   |   |   |                  |
BF A.bit, $addr20          | 3 | 5 | 3 |   |   |   | A.bit = 0        | PC ← PC+3 + jdisp8
BF PSW.bit, $addr20        | 4 | 5 | 3 |   |   |   | PSW.bit = 0      | PC ← PC+4 + jdisp8
BF sfr.bit, $addr20        | 4 | 5 | 3 |   |   |   | sfr.bit = 0      | PC ← PC+4 + jdisp8
BF saddr.bit, $addr20      | 4 | 5 | 3 |   |   |   | saddr.bit = 0    | PC ← PC+4 + jdisp8
BF [HL].bit, $addr20       | 3 | 5 | 3 |   |   |   | (HL).bit = 0     | PC ← PC+3 + jdisp8
BF ES:[HL].bit, $addr20    | 4 | 6 | 4 |   |   |   | (ES, HL).bit = 0 | PC ← PC+4 + jdisp8
5                          |   |   |   |   |   |   |                  |
BC $addr20                 | 2 | 4 | 2 |   |   |   | CY = 1           | PC ← PC+2 + jdisp8
BNC $addr20                | 2 | 4 | 2 |   |   |   | CY = 0           | PC ← PC+2 + jdisp8
BZ $addr20                 | 2 | 4 | 2 |   |   |   | Z = 1            | PC ← PC+2 + jdisp8
BNZ $addr20                | 2 | 4 | 2 |   |   |   | Z = 0            | PC ← PC+2 + jdisp8
BH $addr20                 | 2 | 4 | 2 |   |   |   | (Z ∨ CY) = 0     | PC ← PC+2 + jdisp8
BNH $addr20                | 2 | 4 | 2 |   |   |   | (Z ∨ CY) = 1     | PC ← PC+2 + jdisp8

## BRK

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
BRK | 2 | 5 |   |   |   | (SP–1) ← PSW,<br>(SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC<sub>S</sub> ← 0000, PC<sub>H</sub> ← (0x0007F), PC<sub>L</sub> ← (0x0007E),<br>SP ← SP–4, IE ← 0

## CALL

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CALL AX | 2 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← CS, AX,<br>SP ← SP–4
CALL BC | 2 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← CS, BC,<br>SP ← SP–4
CALL DE | 2 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← CS, DE,<br>SP ← SP–4
CALL HL | 2 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← CS, HL,<br>SP ← SP–4
CALL !addr16 | 3 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← PC + 0000, addr16,<br>SP ← SP–4
CALL $!addr20 | 3 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← PC + 3 + jdisp16,<br>SP ← SP–4
CALL !!addr20 | 4 | 3 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC ← PC + addr20,<br>SP ← SP–4

## CALLT

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CALLT [addr5] | 2 | 5 |   |   |   | (SP–2) ← (PC+2)<sub>S</sub>, (SP–3) ← (PC+2)<sub>H</sub>, (SP–4) ← (PC+2)<sub>L</sub>,<br>PC<sub>S</sub> ← 0000, PC<sub>H</sub> ← (0000, addr5+1), PC<sub>L</sub> ← (0000, addr5),<br>SP ← SP–4

## CLRB

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CLRB A          | 1 | 1 |   |   |   | A ← 0x00
CLRB X          | 1 | 1 |   |   |   | X ← 0x00
CLRB B          | 1 | 1 |   |   |   | B ← 0x00
CLRB C          | 1 | 1 |   |   |   | C ← 0x00
CLRB saddr      | 2 | 1 |   |   |   | (saddr) ← 0x00
CLRB !addr16    | 3 | 1 |   |   |   | (addr16) ← 0x00
CLRB ES:!addr16 | 4 | 2 |   |   |   | (ES, addr16) ← 0x00

## CLRW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CLRW AX | 1 | 1 |   |   |   | AX ← 0x0000
CLRW BC | 1 | 1 |   |   |   | BC ← 0x0000

## CLR1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CLR1 CY             | 2 | 1 |   |   | 0 | CY ← 0
CLR1 A.bit          | 2 | 1 |   |   |   | A.bit ← 0
CLR1 PSW.bit        | 3 | 4 | × | × | × | PSW.bit ← 0
CLR1 sfr.bit        | 3 | 2 |   |   |   | sfr.bit ← 0
CLR1 saddr.bit      | 3 | 2 |   |   |   | (saddr).bit ← 0
CLR1 !addr16.bit    | 4 | 2 |   |   |   | (addr16).bit ← 0
CLR1 ES:!addr16.bit | 5 | 3 |   |   |   | (ES, addr16).bit ← 0
CLR1 [HL].bit       | 2 | 2 |   |   |   | (HL).bit ← 0
CLR1 ES:[HL].bit    | 3 | 3 |   |   |   | (ES, HL).bit ← 0

## CMP / CMPS

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CMP A, #byte          | 2 | 1 | × | × | × | Z, AC, CY ← A – byte
CMP saddr, #byte      | 3 | 1 | × | × | × | Z, AC, CY ← (saddr) – byte
CMP !addr16, #byte    | 4 | 1 | × | × | × | Z, AC, CY ← (addr16) – byte
CMP ES:!addr16, #byte | 5 | 2 | × | × | × | Z, AC, CY ← (ES:addr16) – byte
CMP X, A              | 2 | 1 | × | × | × | Z, AC, CY ← X – A
CMP B, A              | 2 | 1 | × | × | × | Z, AC, CY ← B – A
CMP C, A              | 2 | 1 | × | × | × | Z, AC, CY ← C – A
CMP D, A              | 2 | 1 | × | × | × | Z, AC, CY ← D – A
CMP E, A              | 2 | 1 | × | × | × | Z, AC, CY ← E – A
CMP H, A              | 2 | 1 | × | × | × | Z, AC, CY ← H – A
CMP L, A              | 2 | 1 | × | × | × | Z, AC, CY ← L – A
CMP A, X              | 2 | 1 | × | × | × | Z, AC, CY ← A – X
CMP A, B              | 2 | 1 | × | × | × | Z, AC, CY ← A – B
CMP A, C              | 2 | 1 | × | × | × | Z, AC, CY ← A – C
CMP A, D              | 2 | 1 | × | × | × | Z, AC, CY ← A – D
CMP A, E              | 2 | 1 | × | × | × | Z, AC, CY ← A – E
CMP A, H              | 2 | 1 | × | × | × | Z, AC, CY ← A – H
CMP A, L              | 2 | 1 | × | × | × | Z, AC, CY ← A – L
CMP A, saddr          | 2 | 1 | × | × | × | Z, AC, CY ← A – (saddr)
CMP A, !addr16        | 3 | 1 | × | × | × | Z, AC, CY ← A – (addr16)
CMP A, [HL]           | 1 | 1 | × | × | × | Z, AC, CY ← A – (HL)
CMP A, [HL+B]         | 2 | 1 | × | × | × | Z, AC, CY ← A – (HL + B)
CMP A, [HL+C]         | 2 | 1 | × | × | × | Z, AC, CY ← A – (HL + C)
CMP A, [HL+byte]      | 2 | 1 | × | × | × | Z, AC, CY ← A – (HL + byte)
CMP A, ES:!addr16     | 4 | 2 | × | × | × | Z, AC, CY ← A – (ES, addr16)
CMP A, ES:[HL]        | 2 | 2 | × | × | × | Z, AC, CY ← A – (ES, HL)
CMP A, ES:[HL+B]      | 3 | 2 | × | × | × | Z, AC, CY ← A – ((ES, HL) + B)
CMP A, ES:[HL+C]      | 3 | 2 | × | × | × | Z, AC, CY ← A – ((ES, HL) + C)
CMP A, ES:[HL+byte]   | 3 | 2 | × | × | × | Z, AC, CY ← A – ((ES, HL) + byte)
CMPS X, [HL+byte]     | 3 | 1 | × | × | × | Z, AC, CY ← X – (HL + byte)
CMPS X, ES:[HL+byte]  | 4 | 2 | × | × | × | Z, AC, CY ← X – ((ES, HL) + byte)

## CMPW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CMPW AX, #word        | 3 | 1 | × | × | × | Z, AC, CY ← AX – word
CMPW AX, BC           | 1 | 1 | × | × | × | Z, AC, CY ← AX – BC
CMPW AX, DE           | 1 | 1 | × | × | × | Z, AC, CY ← AX – DE
CMPW AX, HL           | 1 | 1 | × | × | × | Z, AC, CY ← AX – HL
CMPW AX, saddrp       | 2 | 1 | × | × | × | Z, AC, CY ← AX – (saddrp)
CMPW AX, !addr16      | 3 | 1 | × | × | × | Z, AC, CY ← AX – (addr16)
CMPW AX, [HL+byte]    | 3 | 1 | × | × | × | Z, AC, CY ← AX – (HL + byte)
CMPW AX, ES:!addr16   | 4 | 2 | × | × | × | Z, AC, CY ← AX – (ES, addr16)
CMPW AX, ES:[HL+byte] | 4 | 2 | × | × | × | Z, AC, CY ← AX – ((ES, HL) + byte)

## CMP0

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
CMP0 A          | 1 | 1 | × | 0 | 0 | Z ← A – 0x00
CMP0 X          | 1 | 1 | × | 0 | 0 | Z ← X – 0x00
CMP0 B          | 1 | 1 | × | 0 | 0 | Z ← B – 0x00
CMP0 C          | 1 | 1 | × | 0 | 0 | Z ← C – 0x00
CMP0 saddr      | 2 | 1 | × | 0 | 0 | Z ← (saddr) – 0x00
CMP0 !addr16    | 3 | 1 | × | 0 | 0 | Z ← (addr16) – 0x00
CMP0 ES:!addr16 | 4 | 2 | × | 0 | 0 | Z ← (ES:addr16) – 0x00

## DEC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
DEC A            | 1 | 1 | × | × |   | A ← A – 1
DEC X            | 1 | 1 | × | × |   | X ← X – 1
DEC B            | 1 | 1 | × | × |   | B ← B – 1
DEC C            | 1 | 1 | × | × |   | C ← C – 1
DEC D            | 1 | 1 | × | × |   | D ← D – 1
DEC E            | 1 | 1 | × | × |   | E ← E – 1
DEC H            | 1 | 1 | × | × |   | H ← H – 1
DEC L            | 1 | 1 | × | × |   | L ← L – 1
DEC saddr        | 2 | 2 | × | × |   | (saddr) ← (saddr) – 1
DEC !addr16      | 3 | 2 | × | × |   | (addr16) ← (addr16) – 1
DEC [HL+byte]    | 3 | 2 | × | × |   | (HL + byte) ← (HL + byte) – 1
DEC ES:!addr16   | 4 | 3 | × | × |   | (ES, addr16) ← (ES, addr16) – 1
DEC ES:[HL+byte] | 4 | 3 | × | × |   | ((ES, HL) + byte) ← ((ES, HL) + byte) – 1

## DECW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
DECW AX           | 1 | 1 |   |   |   | AX ← AX – 1
DECW BC           | 1 | 1 |   |   |   | BC ← BC – 1
DECW DE           | 1 | 1 |   |   |   | DE ← DE – 1
DECW HL           | 1 | 1 |   |   |   | HL ← HL – 1
DECW saddrp       | 2 | 2 |   |   |   | (saddrp) ← (saddrp) – 1
DECW !addr16      | 3 | 2 |   |   |   | (addr16) ← (addr16) – 1
DECW [HL+byte]    | 3 | 2 |   |   |   | (HL + byte) ← (HL + byte) – 1
DECW ES:!addr16   | 4 | 3 |   |   |   | (ES, addr16) ← (ES, addr16) – 1
DECW ES:[HL+byte] | 4 | 3 |   |   |   | ((ES, HL) + byte) ← ((ES, HL) + byte) – 1

## DI

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
DI   | 3 | 4 |   |   |   | IE ← 0 (Disable Interrupts)

## EI

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
EI   | 3 | 4 |   |   |   | IE ← 1 (Enable Interrupts)

## HALT

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
HALT | 2 | 3 |   |   |   | Set HALT Mode

## INC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
INC A            | 1 | 1 | × | × |   | A ← A + 1
INC X            | 1 | 1 | × | × |   | X ← X + 1
INC B            | 1 | 1 | × | × |   | B ← B + 1
INC C            | 1 | 1 | × | × |   | C ← C + 1
INC D            | 1 | 1 | × | × |   | D ← D + 1
INC E            | 1 | 1 | × | × |   | E ← E + 1
INC H            | 1 | 1 | × | × |   | H ← H + 1
INC L            | 1 | 1 | × | × |   | L ← L + 1
INC saddr        | 2 | 2 | × | × |   | (saddr) ← (saddr) + 1
INC !addr16      | 3 | 2 | × | × |   | (addr16) ← (addr16) + 1
INC [HL+byte]    | 3 | 2 | × | × |   | (HL + byte) ← (HL + byte) + 1
INC ES:!addr16   | 4 | 3 | × | × |   | (ES, addr16) ← (ES, addr16) + 1
INC ES:[HL+byte] | 4 | 3 | × | × |   | ((ES, HL) + byte) ← ((ES, HL) + byte) + 1

## INCW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
INCW AX           | 1 | 1 |   |   |   | AX ← AX + 1
INCW BC           | 1 | 1 |   |   |   | BC ← BC + 1
INCW DE           | 1 | 1 |   |   |   | DE ← DE + 1
INCW HL           | 1 | 1 |   |   |   | HL ← HL + 1
INCW saddrp       | 2 | 2 |   |   |   | (saddrp) ← (saddrp) + 1
INCW !addr16      | 3 | 2 |   |   |   | (addr16) ← (addr16) + 1
INCW [HL+byte]    | 3 | 2 |   |   |   | (HL + byte) ← (HL + byte) + 1
INCW ES:!addr16   | 4 | 3 |   |   |   | (ES, addr16) ← (ES, addr16) + 1
INCW ES:[HL+byte] | 4 | 3 |   |   |   | ((ES, HL) + byte) ← ((ES, HL) + byte) + 1

## MOV / MOVS

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
1                       |   |   |   |   |   |
MOV A, #byte            | 2 | 1 |   |   |   | A ← byte
MOV X, #byte            | 2 | 1 |   |   |   | X ← byte
MOV B, #byte            | 2 | 1 |   |   |   | B ← byte
MOV C, #byte            | 2 | 1 |   |   |   | C ← byte
MOV D, #byte            | 2 | 1 |   |   |   | D ← byte
MOV E, #byte            | 2 | 1 |   |   |   | E ← byte
MOV H, #byte            | 2 | 1 |   |   |   | H ← byte
MOV L, #byte            | 2 | 1 |   |   |   | L ← byte
MOV PSW, #byte          | 3 | 3 | × | × | × | PSW ← byte
MOV CS, #byte           | 3 | 1 |   |   |   | CS ← byte
MOV ES, #byte           | 2 | 1 |   |   |   | ES ← byte
MOV sfr, #byte          | 3 | 1 |   |   |   | sfr ← byte
MOV saddr, #byte        | 3 | 1 |   |   |   | (saddr) ← byte
MOV !addr16, #byte      | 4 | 1 |   |   |   | (addr16) ← byte
MOV [SP+byte], #byte    | 3 | 1 |   |   |   | (SP + byte) ← byte
MOV [DE+byte], #byte    | 3 | 1 |   |   |   | (DE + byte) ← byte
MOV [HL+byte], #byte    | 3 | 1 |   |   |   | (HL + byte) ← byte
MOV word[B], #byte      | 4 | 1 |   |   |   | (B + word) ← byte
MOV word[C], #byte      | 4 | 1 |   |   |   | (C + word) ← byte
MOV word[BC], #byte     | 4 | 1 |   |   |   | (BC + word) ← byte
MOV ES:!addr16, #byte   | 5 | 2 |   |   |   | (ES, addr16) ← byte
MOV ES:[DE+byte], #byte | 4 | 2 |   |   |   | ((ES, DE) + byte) ← byte
MOV ES:[HL+byte], #byte | 4 | 2 |   |   |   | ((ES, HL) + byte) ← byte
MOV ES:word[B], #byte   | 5 | 2 |   |   |   | ((ES, B) + word) ← byte
MOV ES:word[C], #byte   | 5 | 2 |   |   |   | ((ES, C) + word) ← byte
MOV ES:word[BC], #byte  | 5 | 2 |   |   |   | ((ES, BC) + word) ← byte
2                       |   |   |   |   |   |
MOV X, A                | 1 | 1 |   |   |   | X ← A
MOV B, A                | 1 | 1 |   |   |   | B ← A
MOV C, A                | 1 | 1 |   |   |   | C ← A
MOV D, A                | 1 | 1 |   |   |   | D ← A
MOV E, A                | 1 | 1 |   |   |   | E ← A
MOV H, A                | 1 | 1 |   |   |   | H ← A
MOV L, A                | 1 | 1 |   |   |   | L ← A
MOV PSW, A              | 2 | 3 | × | × | × | PSW ← A
MOV CS, A               | 2 | 1 |   |   |   | CS ← A
MOV ES, A               | 2 | 1 |   |   |   | ES ← A
MOV sfr, A              | 2 | 1 |   |   |   | sfr ← A
MOV saddr, A            | 2 | 1 |   |   |   | (saddr) ← A
MOV !addr16, A          | 3 | 1 |   |   |   | (addr16) ← A
MOV [SP+byte], A        | 2 | 1 |   |   |   | (SP + byte) ← A
MOV [DE], A             | 1 | 1 |   |   |   | (DE) ← A
MOV [DE+byte], A        | 2 | 1 |   |   |   | (DE + byte) ← A
MOV [HL], A             | 1 | 1 |   |   |   | (HL) ← A
MOV [HL+B], A           | 2 | 1 |   |   |   | (HL + B) ← A
MOV [HL+C], A           | 2 | 1 |   |   |   | (HL + C) ← A
MOV [HL+byte], A        | 2 | 1 |   |   |   | (HL + byte) ← A
MOV word[B], A          | 3 | 1 |   |   |   | (B + word) ← A
MOV word[C], A          | 3 | 1 |   |   |   | (C + word) ← A
MOV word[BC], A         | 3 | 1 |   |   |   | (BC + word) ← A
MOV ES:!addr16, A       | 4 | 2 |   |   |   | (ES, addr16) ← A
MOV ES:[DE], A          | 2 | 2 |   |   |   | (ES, DE) ← A
MOV ES:[DE+byte], A     | 3 | 2 |   |   |   | ((ES, DE) + byte) ← A
MOV ES:[HL], A          | 2 | 2 |   |   |   | (ES, HL) ← A
MOV ES:[HL+B], A        | 3 | 2 |   |   |   | ((ES, HL) + B) ← A
MOV ES:[HL+C], A        | 3 | 2 |   |   |   | ((ES, HL) + C) ← A
MOV ES:[HL+byte], A     | 3 | 2 |   |   |   | ((ES, HL) + byte) ← A
MOV ES:word[B], A       | 4 | 2 |   |   |   | ((ES, B) + word) ← A
MOV ES:word[C], A       | 4 | 2 |   |   |   | ((ES, C) + word) ← A
MOV ES:word[BC], A      | 4 | 2 |   |   |   | ((ES, BC) + word) ← A
3                       |   |   |   |   |   |
MOVS [HL+byte], X       | 3 | 1 | × |   | × | (HL + byte) ← X
MOVS ES:[HL+byte], X    | 4 | 2 | × |   | × | ((ES, HL) + byte) ← X
4                       |   |   |   |   |   |
MOV A, X                | 1 | 1 |   |   |   | A ← X
MOV A, B                | 1 | 1 |   |   |   | A ← B
MOV A, C                | 1 | 1 |   |   |   | A ← C
MOV A, D                | 1 | 1 |   |   |   | A ← D
MOV A, E                | 1 | 1 |   |   |   | A ← E
MOV A, H                | 1 | 1 |   |   |   | A ← H
MOV A, L                | 1 | 1 |   |   |   | A ← L
MOV A, PSW              | 2 | 1 |   |   |   | A ← PSW
MOV A, CS               | 2 | 1 |   |   |   | A ← CS
MOV A, ES               | 2 | 1 |   |   |   | A ← ES
MOV A, sfr              | 2 | 1 |   |   |   | A ← sfr
MOV A, saddr            | 2 | 1 |   |   |   | A ← (saddr)
MOV A, !addr16          | 3 | 1 |   |   |   | A ← (addr16)
MOV A, [SP+byte]        | 2 | 1 |   |   |   | A ← (SP + byte)
MOV A, [DE]             | 1 | 1 |   |   |   | A ← (DE)
MOV A, [DE+byte]        | 2 | 1 |   |   |   | A ← (DE + byte)
MOV A, [HL]             | 1 | 1 |   |   |   | A ← (HL)
MOV A, [HL+B]           | 2 | 1 |   |   |   | A ← (HL + B)
MOV A, [HL+C]           | 2 | 1 |   |   |   | A ← (HL + C)
MOV A, [HL+byte]        | 2 | 1 |   |   |   | A ← (HL + byte)
MOV A, word[B]          | 3 | 1 |   |   |   | A ← (B + word)
MOV A, word[C]          | 3 | 1 |   |   |   | A ← (C + word)
MOV A, word[BC]         | 3 | 1 |   |   |   | A ← (BC + word)
MOV A, ES:!addr16       | 4 | 2 |   |   |   | A ← (ES, addr16)
MOV A, ES:[DE]          | 2 | 2 |   |   |   | A ← (ES, DE)
MOV A, ES:[DE+byte]     | 3 | 2 |   |   |   | A ← ((ES, DE) + byte)
MOV A, ES:[HL]          | 2 | 2 |   |   |   | A ← (ES, HL)
MOV A, ES:[HL+B]        | 3 | 2 |   |   |   | A ← ((ES, HL) + B)
MOV A, ES:[HL+C]        | 3 | 2 |   |   |   | A ← ((ES, HL) + C)
MOV A, ES:[HL+byte]     | 3 | 2 |   |   |   | A ← ((ES, HL) + byte)
MOV A, ES:word[B]       | 4 | 2 |   |   |   | A ← ((ES, B) + word)
MOV A, ES:word[C]       | 4 | 2 |   |   |   | A ← ((ES, C) + word)
MOV A, ES:word[BC]      | 4 | 2 |   |   |   | A ← ((ES, BC) + word)
5                       |   |   |   |   |   |
MOV ES, saddr           | 3 | 1 |   |   |   | ES ← (saddr)
MOV X, saddr            | 2 | 1 |   |   |   | X ← (saddr)
MOV B, saddr            | 2 | 1 |   |   |   | B ← (saddr)
MOV C, saddr            | 2 | 1 |   |   |   | C ← (saddr)
MOV X, !addr16          | 3 | 1 |   |   |   | X ← (addr16)
MOV B, !addr16          | 3 | 1 |   |   |   | B ← (addr16)
MOV C, !addr16          | 3 | 1 |   |   |   | C ← (addr16)
MOV X, ES:!addr16       | 4 | 2 |   |   |   | X ← (ES, addr16)
MOV B, ES:!addr16       | 4 | 2 |   |   |   | B ← (ES, addr16)
MOV C, ES:!addr16       | 4 | 2 |   |   |   | C ← (ES, addr16)

## MOVW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
1                     |   |   |   |   |   |
MOVW SP, #word        | 4 | 1 |   |   |   | SP ← word
MOVW AX, #word        | 3 | 1 |   |   |   | AX ← word
MOVW BC, #word        | 3 | 1 |   |   |   | BC ← word
MOVW DE, #word        | 3 | 1 |   |   |   | DE ← word
MOVW HL, #word        | 3 | 1 |   |   |   | HL ← word
MOVW sfrp, #word      | 4 | 1 |   |   |   | sfrp ← word
MOVW saddrp, #word    | 4 | 1 |   |   |   | (saddrp) ← word
2                     |   |   |   |   |   |
MOVW SP, AX           | 2 | 1 |   |   |   | SP ← AX
MOVW BC, AX           | 1 | 1 |   |   |   | BC ← AX
MOVW DE, AX           | 1 | 1 |   |   |   | DE ← AX
MOVW HL, AX           | 1 | 1 |   |   |   | HL ← AX
MOVW sfrp, AX         | 2 | 1 |   |   |   | sfrp ← AX
MOVW saddrp, AX       | 2 | 1 |   |   |   | (saddrp) ← AX
MOVW !addr16, AX      | 3 | 1 |   |   |   | (addr16) ← AX
MOVW [SP+byte], AX    | 2 | 1 |   |   |   | (SP + byte) ← AX
MOVW [DE], AX         | 1 | 1 |   |   |   | (DE) ← AX
MOVW [DE+byte], AX    | 2 | 1 |   |   |   | (DE + byte) ← AX
MOVW [HL], AX         | 1 | 1 |   |   |   | (HL) ← AX
MOVW [HL+byte], AX    | 2 | 1 |   |   |   | (HL + byte) ← AX
MOVW word[B], AX      | 3 | 1 |   |   |   | (B + word) ← AX
MOVW word[C], AX      | 3 | 1 |   |   |   | (C + word) ← AX
MOVW word[BC], AX     | 3 | 1 |   |   |   | (BC + word) ← AX
MOVW ES:!addr16, AX   | 4 | 2 |   |   |   | (ES, addr16) ← AX
MOVW ES:[DE], AX      | 2 | 2 |   |   |   | (ES, DE) ← AX
MOVW ES:[DE+byte], AX | 3 | 2 |   |   |   | ((ES, DE) + byte) ← AX
MOVW ES:[HL], AX      | 2 | 2 |   |   |   | (ES, HL) ← AX
MOVW ES:[HL+byte], AX | 3 | 2 |   |   |   | ((ES, HL) + byte) ← AX
MOVW ES:word[B], AX   | 4 | 2 |   |   |   | ((ES, B) + word) ← AX
MOVW ES:word[C], AX   | 4 | 2 |   |   |   | ((ES, C) + word) ← AX
MOVW ES:word[BC], AX  | 4 | 2 |   |   |   | ((ES, BC) + word) ← AX
3                     |   |   |   |   |   |
MOVW AX, SP           | 2 | 1 |   |   |   | AX ← SP
MOVW AX, BC           | 1 | 1 |   |   |   | AX ← BC
MOVW AX, DE           | 1 | 1 |   |   |   | AX ← DE
MOVW AX, HL           | 1 | 1 |   |   |   | AX ← HL
MOVW AX, sfrp         | 2 | 1 |   |   |   | AX ← sfrp
MOVW AX, saddrp       | 2 | 1 |   |   |   | AX ← (saddrp)
MOVW AX, !addr16      | 3 | 1 |   |   |   | AX ← (addr16)
MOVW AX, [SP+byte]    | 2 | 1 |   |   |   | AX ← (SP + byte)
MOVW AX, [DE]         | 1 | 1 |   |   |   | AX ← (DE)
MOVW AX, [DE+byte]    | 2 | 1 |   |   |   | AX ← (DE+byte)
MOVW AX, [HL]         | 1 | 1 |   |   |   | AX ← (HL)
MOVW AX, [HL+byte]    | 2 | 1 |   |   |   | AX ← (HL + byte)
MOVW AX, word[B]      | 3 | 1 |   |   |   | AX ← (B + word)
MOVW AX, word[C]      | 3 | 1 |   |   |   | AX ← (C + word)
MOVW AX, word[BC]     | 3 | 1 |   |   |   | AX ← (BC + word)
MOVW AX, ES:!addr16   | 4 | 2 |   |   |   | AX ← (ES, addr16)
MOVW AX, ES:[DE]      | 2 | 2 |   |   |   | AX ← (ES, DE)
MOVW AX, ES:[DE+byte] | 3 | 2 |   |   |   | AX ← ((ES, DE) + byte)
MOVW AX, ES:[HL]      | 2 | 2 |   |   |   | AX ← (ES, HL)
MOVW AX, ES:[HL+byte] | 3 | 2 |   |   |   | AX ← ((ES, HL) + byte)
MOVW AX, ES:word[B]   | 4 | 2 |   |   |   | AX ← ((ES, B) + word)
MOVW AX, ES:word[C]   | 4 | 2 |   |   |   | AX ← ((ES, C) + word)
MOVW AX, ES:word[BC]  | 4 | 2 |   |   |   | AX ← ((ES, BC) + word)
4                     |   |   |   |   |   |
MOVW BC, SP           | 3 | 1 |   |   |   | BC ← SP
MOVW DE, SP           | 3 | 1 |   |   |   | DE ← SP
MOVW HL, SP           | 3 | 1 |   |   |   | HL ← SP
MOVW BC, saddrp       | 2 | 1 |   |   |   | BC ← (saddrp)
MOVW DE, saddrp       | 2 | 1 |   |   |   | DE ← (saddrp)
MOVW HL, saddrp       | 2 | 1 |   |   |   | HL ← (saddrp)
MOVW BC, !addr16      | 3 | 1 |   |   |   | BC ← (addr16)
MOVW DE, !addr16      | 3 | 1 |   |   |   | DE ← (addr16)
MOVW HL, !addr16      | 3 | 1 |   |   |   | HL ← (addr16)
MOVW BC, ES:!addr16   | 4 | 2 |   |   |   | BC ← (ES, addr16)
MOVW DE, ES:!addr16   | 4 | 2 |   |   |   | DE ← (ES, addr16)
MOVW HL, ES:!addr16   | 4 | 2 |   |   |   | HL ← (ES, addr16)

## MOV1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
MOV1 A.bit, CY       | 2 | 1 |   |   |   | A.bit ← CY
MOV1 PSW.bit, CY     | 3 | 4 | × | × |   | PSW.bit ← CY
MOV1 sfr.bit, CY     | 3 | 2 |   |   |   | sfr.bit ← CY
MOV1 saddr.bit, CY   | 3 | 2 |   |   |   | (saddr).bit ← CY
MOV1 [HL].bit, CY    | 2 | 2 |   |   |   | (HL).bit ← CY
MOV1 ES:[HL].bit, CY | 3 | 3 |   |   |   | (ES, HL).bit ← CY
MOV1 CY, A.bit       | 2 | 1 |   |   | × | CY ← A.bit
MOV1 CY, PSW.bit     | 3 | 1 |   |   | × | CY ← PSW.bit
MOV1 CY, sfr.bit     | 3 | 1 |   |   | × | CY ← sfr.bit
MOV1 CY, saddr.bit   | 3 | 1 |   |   | × | CY ← (saddr).bit
MOV1 CY, [HL].bit    | 2 | 1 |   |   | × | CY ← (HL).bit
MOV1 CY, ES:[HL].bit | 3 | 2 |   |   | × | CY ← (ES, HL).bit

## MULU

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
MULU X | 1 | 1 |   |   |   | AX ← A × X

## NOP

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
NOP  | 1 | 1 |   |   |   | No Operation

## NOT1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
NOT1 CY | 2 | 1 |   |   | × | CY ← ¬CY

## ONEB

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ONEB A          | 1 | 1 |   |   |   | A ← 0x01
ONEB X          | 1 | 1 |   |   |   | X ← 0x01
ONEB B          | 1 | 1 |   |   |   | B ← 0x01
ONEB C          | 1 | 1 |   |   |   | C ← 0x01
ONEB saddr      | 2 | 1 |   |   |   | (saddr) ← 0x01
ONEB !addr16    | 3 | 1 |   |   |   | (addr16) ← 0x01
ONEB ES:!addr16 | 4 | 2 |   |   |   | (ES, addr16) ← 0x01

## ONEW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ONEW AX | 1 | 1 |   |   |   | AX ← 0x0001
ONEW BC | 1 | 1 |   |   |   | BC ← 0x0001

## OR

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
OR A, #byte        | 2 | 1 | × |   |   | A ← A ∨ byte
OR saddr, #byte    | 3 | 2 | × |   |   | (saddr) ← (saddr) ∨ byte
OR X, A            | 2 | 1 | × |   |   | X ← X ∨ A
OR B, A            | 2 | 1 | × |   |   | B ← B ∨ A
OR C, A            | 2 | 1 | × |   |   | C ← C ∨ A
OR D, A            | 2 | 1 | × |   |   | D ← D ∨ A
OR E, A            | 2 | 1 | × |   |   | E ← E ∨ A
OR H, A            | 2 | 1 | × |   |   | H ← H ∨ A
OR L, A            | 2 | 1 | × |   |   | L ← L ∨ A
OR A, X            | 2 | 1 | × |   |   | A ← A ∨ X
OR A, B            | 2 | 1 | × |   |   | A ← A ∨ B
OR A, C            | 2 | 1 | × |   |   | A ← A ∨ C
OR A, D            | 2 | 1 | × |   |   | A ← A ∨ D
OR A, E            | 2 | 1 | × |   |   | A ← A ∨ E
OR A, H            | 2 | 1 | × |   |   | A ← A ∨ H
OR A, L            | 2 | 1 | × |   |   | A ← A ∨ L
OR A, saddr        | 2 | 1 | × |   |   | A ← A ∨ (saddr)
OR A, !addr16      | 3 | 1 | × |   |   | A ← A ∨ (addr16)
OR A, [HL]         | 1 | 1 | × |   |   | A ← A ∨ (HL)
OR A, [HL+B]       | 2 | 1 | × |   |   | A ← A ∨ (HL + B)
OR A, [HL+C]       | 2 | 1 | × |   |   | A ← A ∨ (HL + C)
OR A, [HL+byte]    | 2 | 1 | × |   |   | A ← A ∨ (HL + byte)
OR A, ES:!addr16   | 4 | 2 | × |   |   | A ← A ∨ (ES, addr16)
OR A, ES:[HL]      | 2 | 2 | × |   |   | A ← A ∨ (ES, HL)
OR A, ES:[HL+B]    | 3 | 2 | × |   |   | A ← A ∨ ((ES, HL) + B)
OR A, ES:[HL+C]    | 3 | 2 | × |   |   | A ← A ∨ ((ES, HL) + C)
OR A, ES:[HL+byte] | 3 | 2 | × |   |   | A ← A ∨ ((ES, HL) + byte)

## OR1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
OR1 CY, A.bit       | 2 | 1 |   |   | × | CY ← CY ∨ A.bit
OR1 CY, PSW.bit     | 3 | 1 |   |   | × | CY ← CY ∨ PSW.bit
OR1 CY, sfr.bit     | 3 | 1 |   |   | × | CY ← CY ∨ sfr.bit
OR1 CY, saddr.bit   | 3 | 1 |   |   | × | CY ← CY ∨ (saddr).bit
OR1 CY, [HL].bit    | 2 | 1 |   |   | × | CY ← CY ∨ (HL).bit
OR1 CY, ES:[HL].bit | 3 | 2 |   |   | × | CY ← CY ∨ (ES, HL).bit

## POP

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
POP AX  | 1 | 1 |   |   |   | A ← (SP), X ← (SP+1), SP ← SP+2
POP BC  | 1 | 1 |   |   |   | B ← (SP), C ← (SP+1), SP ← SP+2
POP DE  | 1 | 1 |   |   |   | D ← (SP), E ← (SP+1), SP ← SP+2
POP HL  | 1 | 1 |   |   |   | H ← (SP), L ← (SP+1), SP ← SP+2
POP PSW | 2 | 3 | R | R | R | PSW ← (SP+1), SP ← SP+2

## PUSH

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
PUSH AX  | 1 | 1 |   |   |   | (SP–1) ← X, (SP–2) ← A, SP ← SP–2
PUSH BC  | 1 | 1 |   |   |   | (SP–1) ← C, (SP–2) ← B, SP ← SP–2
PUSH DE  | 1 | 1 |   |   |   | (SP–1) ← E, (SP–2) ← D, SP ← SP–2
PUSH HL  | 1 | 1 |   |   |   | (SP–1) ← L, (SP–2) ← H, SP ← SP–2
PUSH PSW | 2 | 1 |   |   |   | (SP–1) ← PSW, (SP–2) ← 0x00, SP ← SP–2

## RET

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
RET | 1 | 6 |   |   |   | PC<sub>L</sub> ← (SP), PC<sub>H</sub> ← (SP+1), PC<sub>S</sub> ← (SP+2),<br>SP ← SP+4

## RETB

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
RETB | 2 | 6 | R | R | R | PC<sub>L</sub> ← (SP), PC<sub>H</sub> ← (SP+1), PC<sub>S</sub> ← (SP+2),<br>PSW ← (SP+3), SP ← SP+4

## RETI

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
RETI | 2 | 6 | R | R | R | PC<sub>L</sub> ← (SP), PC<sub>H</sub> ← (SP+1), PC<sub>S</sub> ← (SP+2),<br>PSW ← (SP+3), SP ← SP+4

## ROL

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ROL A, 1 | 2 | 1 |   |   | × | (CY, A<sub>0</sub> ← A<sub>7</sub>, A<sub>m+1</sub> ← A<sub>m</sub>) × 1

## ROLC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ROLC A, 1 | 2 | 1 |   |   | × | (CY ← A<sub>7</sub>, A<sub>m+1</sub> ← A<sub>m</sub>, A<sub>0</sub> ← CY) × 1

## ROLWC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ROLWC AX, 1 | 2 | 1 |   |   | × | (CY ← AX<sub>15</sub>, AX<sub>m+1</sub> ← AX<sub>m</sub>, AX<sub>0</sub> ← CY) × 1
ROLWC BC, 1 | 2 | 1 |   |   | × | (CY ← BC<sub>15</sub>, BC<sub>m+1</sub> ← BC<sub>m</sub>, BC<sub>0</sub> ← CY) × 1

## ROR

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
ROR A, 1 | 2 | 1 |   |   | × | (CY, A<sub>7</sub> ← A<sub>0</sub>, A<sub>m–1</sub> ← A<sub>m</sub>) × 1

## RORC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
RORC A, 1 | 2 | 1 |   |   | × | (CY ← A<sub>0</sub>, A<sub>m–1</sub> ← A<sub>m</sub>, A<sub>7</sub> ← CY) × 1

## SAR

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SAR A, cnt | 2 | 1 |   |   | × | (CY ← A<sub>0</sub>, A<sub>m–1</sub> ← A<sub>m</sub>, A<sub>7</sub> ← A<sub>7</sub>) × cnt

## SARW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SARW AX, cnt | 2 | 1 |   |   | × | (CY ← AX<sub>0</sub>, AX<sub>m–1</sub> ← AX<sub>m</sub>, AX<sub>15</sub> ← AX<sub>15</sub>) × cnt

## SEL

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SEL RB0 | 2 | 1 |   |   |   | RBS[1:0] ← 0
SEL RB1 | 2 | 1 |   |   |   | RBS[1:0] ← 1
SEL RB2 | 2 | 1 |   |   |   | RBS[1:0] ← 2
SEL RB3 | 2 | 1 |   |   |   | RBS[1:0] ← 3

## SET1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SET1 CY             | 2 | 1 |   |   | 1 | CY ← 1
SET1 A.bit          | 2 | 1 |   |   |   | A.bit ← 1
SET1 PSW.bit        | 3 | 4 | × | × | × | PSW.bit ← 1
SET1 sfr.bit        | 3 | 2 |   |   |   | sfr.bit ← 1
SET1 saddr.bit      | 3 | 2 |   |   |   | (saddr).bit ← 1
SET1 !addr16.bit    | 4 | 2 |   |   |   | (addr16).bit ← 1
SET1 ES:!addr16.bit | 5 | 3 |   |   |   | (ES, addr16).bit ← 1
SET1 [HL].bit       | 2 | 2 |   |   |   | (HL).bit ← 1
SET1 ES:[HL].bit    | 3 | 3 |   |   |   | (ES, HL).bit ← 1

## SHL

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SHL A, cnt | 2 | 1 |   |   | × | (CY ← A<sub>7</sub>, A<sub>m+1</sub> ← A<sub>m</sub>, A<sub>0</sub> ← 0) × cnt
SHL B, cnt | 2 | 1 |   |   | × | (CY ← B<sub>7</sub>, B<sub>m+1</sub> ← B<sub>m</sub>, B<sub>0</sub> ← 0) × cnt
SHL C, cnt | 2 | 1 |   |   | × | (CY ← C<sub>7</sub>, C<sub>m+1</sub> ← C<sub>m</sub>, C<sub>0</sub> ← 0) × cnt

## SHLW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SHLW AX, cnt | 2 | 1 |   |   | × | (CY ← AX<sub>15</sub>, AX<sub>m+1</sub> ← AX<sub>m</sub>, AX<sub>0</sub> ← 0) × cnt
SHLW BC, cnt | 2 | 1 |   |   | × | (CY ← BC<sub>15</sub>, BC<sub>m+1</sub> ← BC<sub>m</sub>, BC<sub>0</sub> ← 0) × cnt

## SHR

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SHR A, cnt | 2 | 1 |   |   | × | (CY ← A<sub>0</sub>, A<sub>m–1</sub> ← A<sub>m</sub>, A<sub>7</sub> ← 0) × cnt

## SHRW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SHRW AX, cnt | 2 | 1 |   |   | × | (CY ← AX<sub>0</sub>, AX<sub>m–1</sub> ← AX<sub>m</sub>, AX<sub>15</sub> ← 0) × cnt

## SK*

mnemonic | bytes | clocks, T | clocks, F | Z | AC | CY | condition | description
---------|:-----:|:---------:|:---------:|:-:|:--:|:--:|:---------:|------------
SKC  | 2 | 1 | 1 |   |   |   | CY = 1           | PC ← PC+2 + (size of next op)
SKNC | 2 | 1 | 1 |   |   |   | CY = 0           | PC ← PC+2 + (size of next op)
SKZ  | 2 | 1 | 1 |   |   |   | Z = 1            | PC ← PC+2 + (size of next op)
SKNZ | 2 | 1 | 1 |   |   |   | Z = 0            | PC ← PC+2 + (size of next op)
SKH  | 2 | 1 | 1 |   |   |   | (Z ∨ CY) = 0     | PC ← PC+2 + (size of next op)
SKNH | 2 | 1 | 1 |   |   |   | (Z ∨ CY) = 1     | PC ← PC+2 + (size of next op)

## STOP

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
STOP | 2 | 3 |   |   |   | Set STOP Mode

## SUB

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SUB A, #byte        | 2 | 1 | × | × | × | A, CY ← A – byte
SUB saddr, #byte    | 3 | 2 | × | × | × | (saddr), CY ← (saddr) – byte
SUB X, A            | 2 | 1 | × | × | × | X, CY ← X – A
SUB B, A            | 2 | 1 | × | × | × | B, CY ← B – A
SUB C, A            | 2 | 1 | × | × | × | C, CY ← C – A
SUB D, A            | 2 | 1 | × | × | × | D, CY ← D – A
SUB E, A            | 2 | 1 | × | × | × | E, CY ← E – A
SUB H, A            | 2 | 1 | × | × | × | H, CY ← H – A
SUB L, A            | 2 | 1 | × | × | × | L, CY ← L – A
SUB A, X            | 2 | 1 | × | × | × | A, CY ← A – X
SUB A, B            | 2 | 1 | × | × | × | A, CY ← A – B
SUB A, C            | 2 | 1 | × | × | × | A, CY ← A – C
SUB A, D            | 2 | 1 | × | × | × | A, CY ← A – D
SUB A, E            | 2 | 1 | × | × | × | A, CY ← A – E
SUB A, H            | 2 | 1 | × | × | × | A, CY ← A – H
SUB A, L            | 2 | 1 | × | × | × | A, CY ← A – L
SUB A, saddr        | 2 | 1 | × | × | × | A, CY ← A – (saddr)
SUB A, !addr16      | 3 | 1 | × | × | × | A, CY ← A – (addr16)
SUB A, [HL]         | 1 | 1 | × | × | × | A, CY ← A – (HL)
SUB A, [HL+B]       | 2 | 1 | × | × | × | A, CY ← A – (HL + B)
SUB A, [HL+C]       | 2 | 1 | × | × | × | A, CY ← A – (HL + C)
SUB A, [HL+byte]    | 2 | 1 | × | × | × | A, CY ← A – (HL + byte)
SUB A, ES:!addr16   | 4 | 2 | × | × | × | A, CY ← A – (ES, addr16)
SUB A, ES:[HL]      | 2 | 2 | × | × | × | A, CY ← A – (ES, HL)
SUB A, ES:[HL+B]    | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + B)
SUB A, ES:[HL+C]    | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + C)
SUB A, ES:[HL+byte] | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + byte)

## SUBC

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SUBC A, #byte        | 2 | 1 | × | × | × | A, CY ← A – byte – CY
SUBC saddr, #byte    | 3 | 2 | × | × | × | (saddr), CY ← (saddr) – byte – CY
SUBC X, A            | 2 | 1 | × | × | × | X, CY ← X – A – CY
SUBC B, A            | 2 | 1 | × | × | × | B, CY ← B – A – CY
SUBC C, A            | 2 | 1 | × | × | × | C, CY ← C – A – CY
SUBC D, A            | 2 | 1 | × | × | × | D, CY ← D – A – CY
SUBC E, A            | 2 | 1 | × | × | × | E, CY ← E – A – CY
SUBC H, A            | 2 | 1 | × | × | × | H, CY ← H – A – CY
SUBC L, A            | 2 | 1 | × | × | × | L, CY ← L – A – CY
SUBC A, X            | 2 | 1 | × | × | × | A, CY ← A – X – CY
SUBC A, B            | 2 | 1 | × | × | × | A, CY ← A – B – CY
SUBC A, C            | 2 | 1 | × | × | × | A, CY ← A – C – CY
SUBC A, D            | 2 | 1 | × | × | × | A, CY ← A – D – CY
SUBC A, E            | 2 | 1 | × | × | × | A, CY ← A – E – CY
SUBC A, H            | 2 | 1 | × | × | × | A, CY ← A – H – CY
SUBC A, L            | 2 | 1 | × | × | × | A, CY ← A – L – CY
SUBC A, saddr        | 2 | 1 | × | × | × | A, CY ← A – (saddr) – CY
SUBC A, !addr16      | 3 | 1 | × | × | × | A, CY ← A – (addr16) – CY
SUBC A, [HL]         | 1 | 1 | × | × | × | A, CY ← A – (HL) – CY
SUBC A, [HL+B]       | 2 | 1 | × | × | × | A, CY ← A – (HL + B) – CY
SUBC A, [HL+C]       | 2 | 1 | × | × | × | A, CY ← A – (HL + C) – CY
SUBC A, [HL+byte]    | 2 | 1 | × | × | × | A, CY ← A – (HL + byte) – CY
SUBC A, ES:!addr16   | 4 | 2 | × | × | × | A, CY ← A – (ES, addr16) – CY
SUBC A, ES:[HL]      | 2 | 2 | × | × | × | A, CY ← A – (ES, HL) – CY
SUBC A, ES:[HL+B]    | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + B) – CY
SUBC A, ES:[HL+C]    | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + C) – CY
SUBC A, ES:[HL+byte] | 3 | 2 | × | × | × | A, CY ← A – ((ES, HL) + byte) – CY

## SUBW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
SUBW SP, #byte        | 2 | 1 |   |   |   | SP ← SP – byte
SUBW AX, #word        | 3 | 1 | × | × | × | AX, CY ← AX – word
SUBW AX, BC           | 1 | 1 | × | × | × | AX, CY ← AX – BC
SUBW AX, DE           | 1 | 1 | × | × | × | AX, CY ← AX – DE
SUBW AX, HL           | 1 | 1 | × | × | × | AX, CY ← AX – HL
SUBW AX, saddrp       | 2 | 1 | × | × | × | AX, CY ← AX – (saddrp)
SUBW AX, !addr16      | 3 | 1 | × | × | × | AX, CY ← AX – (addr16)
SUBW AX, [HL+byte]    | 3 | 1 | × | × | × | AX, CY ← AX – (HL + byte)
SUBW AX, ES:!addr16   | 4 | 2 | × | × | × | AX, CY ← AX – (ES, addr16)
SUBW AX, ES:[HL+byte] | 4 | 2 | × | × | × | AX, CY ← AX – ((ES, HL) + byte)

## XCH

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
XCH A, X            | 1 | 1 |   |   |   | A ↔ X
XCH A, B            | 2 | 1 |   |   |   | A ↔ B
XCH A, C            | 2 | 1 |   |   |   | A ↔ C
XCH A, D            | 2 | 1 |   |   |   | A ↔ D
XCH A, E            | 2 | 1 |   |   |   | A ↔ E
XCH A, H            | 2 | 1 |   |   |   | A ↔ H
XCH A, L            | 2 | 1 |   |   |   | A ↔ L
XCH A, sfr          | 3 | 2 |   |   |   | A ↔ sfr
XCH A, saddr        | 3 | 2 |   |   |   | A ↔ (saddr)
XCH A, !addr16      | 4 | 2 |   |   |   | A ↔ (addr16)
XCH A, [DE]         | 2 | 2 |   |   |   | A ↔ (DE)
XCH A, [DE+byte]    | 3 | 2 |   |   |   | A ↔ (DE + byte)
XCH A, [HL]         | 2 | 2 |   |   |   | A ↔ (HL)
XCH A, [HL+B]       | 2 | 2 |   |   |   | A ↔ (HL + B)
XCH A, [HL+C]       | 2 | 2 |   |   |   | A ↔ (HL + C)
XCH A, [HL+byte]    | 3 | 2 |   |   |   | A ↔ (HL + byte)
XCH A, ES:!addr16   | 5 | 3 |   |   |   | A ↔ (ES, addr16)
XCH A, ES:[DE]      | 3 | 3 |   |   |   | A ↔ (ES, DE)
XCH A, ES:[DE+byte] | 4 | 3 |   |   |   | A ↔ ((ES, DE) + byte)
XCH A, ES:[HL]      | 3 | 3 |   |   |   | A ↔ (ES, HL)
XCH A, ES:[HL+B]    | 3 | 3 |   |   |   | A ↔ ((ES, HL) + B)
XCH A, ES:[HL+C]    | 3 | 3 |   |   |   | A ↔ ((ES, HL) + C)
XCH A, ES:[HL+byte] | 4 | 3 |   |   |   | A ↔ ((ES, HL) + byte)

## XCHW

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
XCHW AX, BC | 1 | 1 |   |   |   | AX ↔ BC
XCHW AX, DE | 1 | 1 |   |   |   | AX ↔ DE
XCHW AX, HL | 1 | 1 |   |   |   | AX ↔ HL

## XOR

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
XOR A, #byte        | 2 | 1 | × |   |   | A ← A ⊕ byte
XOR saddr, #byte    | 3 | 2 | × |   |   | (saddr) ← (saddr) ⊕ byte
XOR X, A            | 2 | 1 | × |   |   | X ← X ⊕ A
XOR B, A            | 2 | 1 | × |   |   | B ← B ⊕ A
XOR C, A            | 2 | 1 | × |   |   | C ← C ⊕ A
XOR D, A            | 2 | 1 | × |   |   | D ← D ⊕ A
XOR E, A            | 2 | 1 | × |   |   | E ← E ⊕ A
XOR H, A            | 2 | 1 | × |   |   | H ← H ⊕ A
XOR L, A            | 2 | 1 | × |   |   | L ← L ⊕ A
XOR A, X            | 2 | 1 | × |   |   | A ← A ⊕ X
XOR A, B            | 2 | 1 | × |   |   | A ← A ⊕ B
XOR A, C            | 2 | 1 | × |   |   | A ← A ⊕ C
XOR A, D            | 2 | 1 | × |   |   | A ← A ⊕ D
XOR A, E            | 2 | 1 | × |   |   | A ← A ⊕ E
XOR A, H            | 2 | 1 | × |   |   | A ← A ⊕ H
XOR A, L            | 2 | 1 | × |   |   | A ← A ⊕ L
XOR A, saddr        | 2 | 1 | × |   |   | A ← A ⊕ (saddr)
XOR A, !addr16      | 3 | 1 | × |   |   | A ← A ⊕ (addr16)
XOR A, [HL]         | 1 | 1 | × |   |   | A ← A ⊕ (HL)
XOR A, [HL+B]       | 2 | 1 | × |   |   | A ← A ⊕ (HL + B)
XOR A, [HL+C]       | 2 | 1 | × |   |   | A ← A ⊕ (HL + C)
XOR A, [HL+byte]    | 2 | 1 | × |   |   | A ← A ⊕ (HL + byte)
XOR A, ES:!addr16   | 4 | 2 | × |   |   | A ← A ⊕ (ES, addr16)
XOR A, ES:[HL]      | 2 | 2 | × |   |   | A ← A ⊕ (ES, HL)
XOR A, ES:[HL+B]    | 3 | 2 | × |   |   | A ← A ⊕ ((ES, HL) + B)
XOR A, ES:[HL+C]    | 3 | 2 | × |   |   | A ← A ⊕ ((ES, HL) + C)
XOR A, ES:[HL+byte] | 3 | 2 | × |   |   | A ← A ⊕ ((ES, HL) + byte)

## XOR1

mnemonic | bytes | clocks | Z | AC | CY | description
---------|:-----:|:------:|:-:|:--:|:--:|------------
XOR1 CY, A.bit       | 2 | 1 |   |   | × | CY ← CY ⊕ A.bit
XOR1 CY, PSW.bit     | 3 | 1 |   |   | × | CY ← CY ⊕ PSW.bit
XOR1 CY, sfr.bit     | 3 | 1 |   |   | × | CY ← CY ⊕ sfr.bit
XOR1 CY, saddr.bit   | 3 | 1 |   |   | × | CY ← CY ⊕ (saddr).bit
XOR1 CY, [HL].bit    | 2 | 1 |   |   | × | CY ← CY ⊕ (HL).bit
XOR1 CY, ES:[HL].bit | 3 | 2 |   |   | × | CY ← CY ⊕ (ES, HL).bit

