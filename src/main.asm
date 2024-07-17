#include "rl78_registers.inc"

.equ _t_a,       0xFFEDE; // (16-bit)
.equ _dtc_cst,   0xFFEDC; // (16-bit)
.equ _event_sum, 0xFFEDA; // (16-bit)
.equ _size_curr, 0xFFED9; // ( 8-bit)
.equ _dtc_corr,  0xFFED2; // (7-byte) <-- has to be just below _size_curr



#include "cst_data_in.inc"

.section .text, "a"

  .equ CST_MAXTBL, 6;         // max CST table size = 2**6 = 64
  .equ DEFAULT_T_A, 0x0100;   // for n in $(seq 0 4095); do printf "0x%04X " $n; echo "sqrt($n/256)" | bc -l; done
  .equ DTC_CST_BASE, 0xFFB00; // the very beginning of RAM file on R5F10WLA

_dtc_table_dd:
  .byte 121,   0,   8,   5,   3,   4,   4,   5;
  .byte   4,   5,   5,   5,   5,   6,   6,   6;
  .byte   7,   7,   6,   9,   7,   8,  10,   9;
  .byte   9,  12,   9,  14,  10,  15,  13,  16;
  .byte  15,  17,  19,  18,  23,  20,  27,  23;
  .byte  31,  28,  35,  35,  41,  41,  48,  52;
  .byte  57,  62,  72,  78,  87,  98, 112, 127;
  .byte 143, 167, 190, 225,   5,  55, 116, 198;

@RESET:
  // 0xFFE20 - 0xFFF1F = SADDR
  // 0xFFF00 - 0xFFFFF = SFR
  // 0xFFB00 = 1 KB start
  // 0xFFE20 - 0xFFEDF = 192 bytes for 'short' registers



  // -- set global vars and constants -- //

  movw _t_a, #DEFAULT_T_A;
  movw _dtc_cst, #DTC_CST_BASE & 0xFFFF;
  movw _event_sum, #0;

  // ----- DTC/CST table unpacking ----- //

  movw hl, _dtc_cst;
  movw ax, #7;
  mov es, a;
  clrw bc;
  movw de, ax;
  @dtc_unpack_loop:
    mov c, a;
    mov a, es:_dtc_table_dd[b];
    add x, a;
    mov a, c;
    addc a, #0;
    inc b;
    xchw ax, de;
    addw ax, de;
    mov [hl + 0], #0; // <-- can be removed
    mov [hl + 1], #0; // <-- can be removed
    movw [hl + 2], ax;
    xchw ax, de;
    add L0, #4;
    skz;
  br $@dtc_unpack_loop;

  mov !DTC_CST_BASE + 240 + 3, #0x8B;
  mov !DTC_CST_BASE + 244 + 3, #0x96;
  mov !DTC_CST_BASE + 248 + 3, #0xA2;
  mov !DTC_CST_BASE + 252 + 3, #0xB0;

  movw _dtc_corr + 0, #252 + 232 * 256;
  movw _dtc_corr + 2, #210 + 186 * 256;
  movw _dtc_corr + 4, #157 + 122 * 256;
  movw _dtc_corr + 6, #71 + (1 << (CST_MAXTBL - 1)) * 256;

  // ----- initialization complete ----- //



  // DTC testbed
//*
  movw BC1, #0;
  movw HL1, #0xF000;
  movw ax, HL1;

  @dtc_outer_loop:
    subw ax, #0xF000;
    addw ax, BC1;
    shrw ax, 1;

    // <-- AX0 = input

    clrb !MDUC;                     // 1 <-- unsigned multiplication
    mov d, a;                       // 1
    movw bc, ax;                    // 1 <-- mov c, x (b is not needed)
    mov b, #0xFC;                   // 1
    shlw ax, 3;                     // 1
    and b, a;                       // 1 <-- Z == 1 if B0 == 0
    shlw ax, 6;                     // 1
    xch a, x;                       // 1 <-- X0 == 0
    movw MDAL, ax;                  // 1
    movw ax, #7;                    // 1
    skz;                            // 1
    movw ax, (DTC_CST_BASE - 2)[b]; // 1
    movw hl, ax;                    // 1 <-- HL0 == base
    movw ax, (DTC_CST_BASE + 2)[b]; // 1
    subw ax, hl;                    // 1
    movw MDAH, ax;                  // 1 <-- MDBH = hi, MDBL+1 = lo
    cmp0 D0;                        // 1 <-- not 2 clocks, but 1
    skz;                            // 1 <-- [18 clocks since start]
    br $@dtc_no_corr;               // 3 <-- no corrections needed past 0xFF
      clrw ax;                      // 1
      xchw ax, bc;                  // 1 <-- BC0 == 0, X0 == input
      mov a, (_dtc_corr + 3);       // 1
      cmp x, a;                     // 1
      mov1 C0.2, CY;                // 2
      mov a, (_dtc_corr + 1)[c];    // 1
      cmp x, a;                     // 1
      mov1 C0.1, CY;                // 2
      mov a, (_dtc_corr + 0)[c];    // 1
      cmp x, a;                     // 1
      mov a, c;                     // 1
      subc l, a;                    // 1
      subc H0, #0;                  // 2 <-- [16 clocks in condition block]
    @dtc_no_corr:
    mov a, MDBL + 1;                // 1
    mov x, a;                       // 1
    mov a, MDBH;                    // 1
    addw ax, hl;                    // 1 <-- [38 clocks in the worst case]

    movw hl, HL1;
    movw [hl], ax;
    movw ax, hl;
    addw ax, #2;
    movw HL1, ax;
    cmpw ax, #0xF400;
    skz;
  br $@dtc_outer_loop;

    movw HL1, #0xF000;
    movw ax, HL1;
    add B1, #4;
    cmp B1, #64;
    skz;
  br $@dtc_outer_loop;
//*/



  // CST testbed
/*
  movw ax, #0xF000;
  movw hl, ax;
  clrw bc;
  @move_cst_test_data:
    movw ax, es:_cst_test_data[bc];
    movw [hl], ax;
    incw hl;
    incw hl;
    incw bc;
    incw bc;
    movw ax, bc;
    cmpw ax, #1680;
    skz;
  br $@move_cst_test_data;

  movw ax, #0xF000;
  @cst_outer_loop:
    movw HL2, ax;
    movw hl, ax;
    movw ax, [hl];

    // <-- AX0 = input

    .equ _esp_l,     AX1;
    .equ _esp_h,     BC1;
    .equ _esn_l,     DE1;
    .equ _esn_h,     L1;
    .equ _size_next, H1;

    clrb !MDUC;                     // 1 <-- unsigned multiplication
    clrb _esn_h;                    // 1
    movw _esp_h, #0;                // 1
    movw hl, _dtc_cst;              // 1
    movw [hl], ax;                  // 1 <-- adding the new value to event_buf
    subw ax, _event_sum;            // 1
    subc _esn_h, #0;                // 2
    movw _esn_l, ax;                // 1
    movw ax, [hl];                  // 1
    addw ax, _event_sum;            // 1 <-- cannot overflow
    movw _esp_l, ax;                // 1
    mov a, _size_curr;              // 1
    mov d, a;                       // 1
    dec d;                          // 1 <-- loop counter = _size_curr - 1
    inc a;                          // 1
    mov _size_next, a;              // 1 <-- [17 clocks since start]

    // AX0 = (accumulator)
    // BC0 = t_a*esp, bytes 2 and 1
    //  E0 = t_a*esp, byte 0
    //  D0 = loop counter
    //  L0 = event_idx
    //  H0 = event_buf / 0x100 (has to be 0x100 aligned)

    @cst_loop:
      movw ax, _t_a;                // 1
      movw MDAL, ax;                // 1
      sub L0, #4;                   // 2 <-- needed for [hl] addressing 1 line below
      movw ax, [hl];                // 1
      addw ax, _event_sum;          // 1 <-- strictly positive sum, cannot overflow
      addw ax, _esp_l;              // 1
      addc _esp_h, #0;              // 2
      movw _esp_l, ax;              // 1

      movw MDAH, ax;                // 1 <-- MDBH:MDBL = t_a*esp_l
      movw bc, !MDBH;               // 1
      mov a, MDBL + 1;              // 1
      mov e, a;                     // 1
      movw ax, _esp_h;              // 1
      movw MDAH, ax;                // 1 <-- MDBH:MDBL = t_a*esp_h
      movw ax, MDBL;                // 1
      addw ax, bc;                  // 1
      movw bc, ax;                  // 1

      movw ax, [hl];                // 1
      subw ax, _event_sum;          // 1
      subc _esn_h, #0;              // 2
      addw ax, _esn_l;              // 1
      addc _esn_h, #0;              // 2
      movw _esn_l, ax;              // 1
      sknz;                         // 1 <-- [28 clocks from _cst_loop]
    br $@cst_neg_end;               // 3 <-- if _esn_h == 0 then nothing to negate
      cmp _esn_h, #0xFF;            // 1
      skz;                          // 1
    br $@cst_gt;                    // 3 <-- if 1 <= _esn_h <= 254 then esn**2 > t_a*esp
      xor X0, #0xFF;                // 2
      xor a, #0xFF;                 // 1
      incw ax;                      // 1
    @cst_neg_end:
      movw MDAL, ax;                // 1 <-- [32 if _esn_h == 0, 35 if _esn_h == 255]
      movw MDAH, ax;                // 1 <-- MDBH:MDBL = esn**2
      cmp0 !MDBH + 1;               // 1
      skz;                          // 1
    br $@cst_gt;                    // 3 <-- if esn**2 > 0xFFFFFF then esn**2 > t_a*esp
      mov a, MDBL + 1;              // 1
      mov x, a;                     // 1
      mov a, MDBH;                  // 1
      cmpw ax, bc;                  // 1
      sknc;                         // 1
    br $@cst_le;                    // 3 <-- esn**2 - t_a*esp < 0 (CY == 1)
      skz;                          // 1
    br $@cst_gt;                    // 3 <-- esn**2 - t_a*esp > 0 ((CY || Z) == 0)
      mov a, MDBL;                  // 1
      cmp a, e;                     // 1
      sknh;                         // 1 <-- esn**2 - t_a*esp <= 0 ((CY || Z) == 1)
    @cst_gt:
      dec _size_next;               // 2
    @cst_le:
      dec d;                        // 1
      skz;                          // 1
    br $@cst_loop;                  // 3 <-- [54 clocks in the worst case]

    cmp _esn_h, #0x80;              // 1 <-- '_'-s below mean CY is to be preserved
    movw ax, _esn_l;                //_1
    sknc;                           //_1
    br $@cst_positive;              //_3
      xor _esn_h, #0xFF;            //_2 <-- CY == 0 here, would've branched otherwise
      xor X0, #0xFF;                //_2
      xor a, #0xFF;                 //_1
      addw ax, #1;                  // 1
      addc _esn_h, #0;              //_2 <-- no more overflow: CY == 0 after this op
    @cst_positive:
    mov !MDUC, #0x80;               //_1
    movw MDAL, ax;                  //_1
    clrb a;                         //_1
    mov x, _esn_h;                  //_1
    movw MDAH, ax;                  //_1
    mov x, _size_curr;              //_1
    movw MDBL, ax;                  //_1
    movw MDBH, #0;                  //_1
    mov !MDUC, #0x81;               //_1 <-- division starts here

    mov a, _size_next;              //_1
    bf a.CST_MAXTBL, $@cst_size_ok; //_5/3 <-- 5 on branch, 3 on skip
      mov a, #1 << CST_MAXTBL;      //_1
      nop;                          //_1
    @cst_size_ok:
    mov _size_curr, a;              //_1 <-- _size_curr = min(_size_next, 1<<CST_MAXTBL)
    inc _dtc_cst;                   //_1
    inc _dtc_cst;                   //_1
    inc _dtc_cst;                   //_1
    inc _dtc_cst;                   //_1
    movw bc, _event_sum;            //_1
    clrb a;                         //_1
    nop;                            //_1
    nop;                            //_1 <-- [15 clocks since division start]

    or a, !MDCL;                    //_1 <-- Z == 1 means there's no remainder
    xchw ax, bc;                    //_1 <-- AX0 = _event_sum, B0 = rem, C0 = div
    sknh;                           //_1
    decw ax;                        //_1 <-- (CY || Z) == 0: SUB && remainder
    not1 CY;                        //_1 <-- ensure !CY->ADD and CY->SUB
    skc;                            //_1
    addw ax, !MDAL;                 // 1 <-- 0 <= (ax, MDAL) < 8192, so CY == 0 now
    sknc;                           // 1
    subw ax, !MDAL;                 // 1 <-- [8 clocks on SKC, 8 clocks on SKNC]

    cmp a, #0x80;                   // 1
    skc;                            // 1
    clrw ax;                        // 1 <-- do not allow negative _event_sum
    movw _event_sum, ax;            // 1 <-- [47 clocks since loop in the worst case]

    movw hl, HL2;
    movw [hl], ax;
    movw ax, hl;
    addw ax, #2;
    cmpw ax, #0xF690;
    skz;
  br $!@cst_outer_loop;
//*/



  // -------- clock init -------- //

  mov CMC, #0b00010000;     // enable XT1 oscillator pins
  mov CSC, #0b10000001;     // start XT1, stop internal oscillator
  set1 !CKC.6;              // use subsystem clock as main clock
  //mov !OSMC, #0b10000000;   // disable clock to most peripherals in low-power modes
  mov LCDM0, #0b10001101;   // cap split, 1/4 duty, 1/3 bias
  mov LCDC0, #0b00001000;   // set the largest divider where LCD flicker is not yet noticeable
  mov !ISCLCD, #0b00000001; // enable CAPL/CAPH capacitor switch
  mov LCDM1, #0b11100000;   // enable LCD driver, LCD bias supply, show pattern A

  // -------- gpio init --------- //

  // LCD function is enabled by default for all pins that support it for some weird reason
  clrw ax;
  movw !PFSEG0, ax;
  movw !PFSEG2, ax;
  movw !PFSEG4, ax;
  movw !PFSEG6, ax;

  // set all pins to defined state (output mode) to reduce leakage currents
  movw PM0, ax;
  movw PM2, #0x0200; // P31 - input
  movw PM4, #0x0401; // P40 is needed for debugging, PM5_bit.no2 = 1 (switch pin P52 to input mode)
  mov PM6, a;

  // -------- timer init -------- //

  /* !!! IN DEBUG MODE TIMER IS CLOCKED AT 32MHZ NOT 32KHZ  !!! */
  /* Timer KB20, set to Output stop function 1, trigger - INTP1 */
  set1 !PER1.4;  // enable timer KB20
  movw ax, #4;
  movw !TKBCR00, ax; // freq
  onew ax;
  movw !TKBCR01, ax; // duty
  // trigger force stop on INTP1, switch output to low level, restart on counter overflow
  movw ax, #0x004E;
  movw !TKBPACTL00, ax;
  onew ax;
  movw !TKBPACTL02, ax; // enable force output stop for TKBO00
  set1 !TKBCTL01.7;     // enable counter
  set1 !TKBIOC01.0;     // enable timer output

  // --------------------------- //

  movw ax, #0xFFFF;
  movw !SEG0, ax;
  movw !SEG2, ax;

  @loop:
    bf P3.1, $@loop;
    oneb !TKBPAHFT0;
  br $@loop;



.section .option_bytes, "a"
  .byte 0xEF, 0xFF, 0xE8, 0x85

.section .security_id, "a"
  .byte 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00

#include "rl78_interrupts.inc"

.end
