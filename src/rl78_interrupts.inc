.section .text, "a"

@INTWDTI:
@INTLVI:
@INTP0:
@INTP1:
@INTP2:
@INTP3:
@INTP4:
@INTP5:
@INTST2:
@INTSR2:
@INTSRE2:
@INTDMA0:
@INTDMA1:
@INTST0:
@INTTM00:
@INTSR0:
@INTTM01H:
@INTST1:
@INTSR1:
@INTTM03H:
@INTIICA0:
@INTRTIT:
@INTTM01:
@INTTM02:
@INTTM03:
@INTAD:
@INTRTC:
@INTIT:
@INTKR:
@INTTKB20:
@INTTM04:
@INTTM05:
@INTP6:
@INTP7:
@INTLCD0:
@INTCMP0:
@INTCMP1:
@INTTM06:
@INTTM07:
@INTMD:
@INTFL:
@INTDMA2:
@INTDMA3:
  reti;

@INTBRK:
  retb;



.section .vects, "a"
  .short  @RESET,    0xFFFF,     @INTWDTI,   @INTLVI
  .short  @INTP0,    @INTP1,     @INTP2,     @INTP3
  .short  @INTP4,    @INTP5,     @INTST2,    @INTSR2
  .short  @INTSRE2,  @INTDMA0,   @INTDMA1,   @INTST0
  .short  @INTTM00,  @INTSR0,    @INTTM01H,  @INTST1
  .short  @INTSR1,   @INTTM03H,  @INTIICA0,  @INTRTIT
  .short  0xFFFF,    @INTTM01,   @INTTM02,   @INTTM03
  .short  @INTAD,    @INTRTC,    @INTIT,     @INTKR
  .short  0xFFFF,    0xFFFF,     @INTTKB20,  @INTTM04
  .short  @INTTM05,  @INTP6,     @INTP7,     @INTLCD0
  .short  @INTCMP0,  @INTCMP1,   @INTTM06,   @INTTM07
  .short  0xFFFF,    0xFFFF,     0xFFFF,     @INTMD
  .short  0xFFFF,    @INTFL,     @INTDMA2,   @INTDMA3
  .short  0xFFFF,    0xFFFF,     0xFFFF,     0xFFFF
  .short  0xFFFF,    0xFFFF,     0xFFFF,     0xFFFF
  .short  0xFFFF,    0xFFFF,     0xFFFF,     @INTBRK

