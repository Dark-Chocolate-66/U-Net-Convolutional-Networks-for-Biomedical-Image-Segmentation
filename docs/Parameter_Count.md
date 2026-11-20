# U-Net parameter count 

**Version used:** padded U-Net (every 3x3 conv uses padding=1, so the picture size does not
shrink inside a level). Input 1x512x512 (grey image), base = 64 channels, 4 pool steps,
**1 output channel** (cell / not cell, for BCE or Dice loss).

## The two formulas

- 3x3 convolution: `(3 x 3 x C_in + 1) x C_out`  (the `+1` is the bias of each output channel)
- 2x2 up-convolution: `(2 x 2 x C_in + 1) x C_out`
- 1x1 convolution: `(1 x 1 x C_in + 1) x C_out`

MaxPool, ReLU, concatenation and copying the skip connection have **0 parameters**.

## Encoder (going down)

| Level | Layer | Calculation | Parameters |
|---|---|---|---|
| 1 | conv 1 -> 64 | (9x1+1) x 64 | 640 |
| 1 | conv 64 -> 64 | (9x64+1) x 64 | 36,928 |
| 2 | conv 64 -> 128 | (9x64+1) x 128 | 73,856 |
| 2 | conv 128 -> 128 | (9x128+1) x 128 | 147,584 |
| 3 | conv 128 -> 256 | (9x128+1) x 256 | 295,168 |
| 3 | conv 256 -> 256 | (9x256+1) x 256 | 590,080 |
| 4 | conv 256 -> 512 | (9x256+1) x 512 | 1,180,160 |
| 4 | conv 512 -> 512 | (9x512+1) x 512 | 2,359,808 |
| 5 (bottom) | conv 512 -> 1024 | (9x512+1) x 1024 | 4,719,616 |
| 5 (bottom) | conv 1024 -> 1024 | (9x1024+1) x 1024 | 9,438,208 |

## Decoder (going up)

After each up-conv we **concatenate** the skip copy, so the channels double before the first conv.

| Level | Layer | Calculation | Parameters |
|---|---|---|---|
| 4 | up-conv 1024 -> 512 | (4x1024+1) x 512 | 2,097,664 |
| 4 | conv 1024 -> 512 (after concat) | (9x1024+1) x 512 | 4,719,104 |
| 4 | conv 512 -> 512 | (9x512+1) x 512 | 2,359,808 |
| 3 | up-conv 512 -> 256 | (4x512+1) x 256 | 524,544 |
| 3 | conv 512 -> 256 (after concat) | (9x512+1) x 256 | 1,179,904 |
| 3 | conv 256 -> 256 | (9x256+1) x 256 | 590,080 |
| 2 | up-conv 256 -> 128 | (4x256+1) x 128 | 131,200 |
| 2 | conv 256 -> 128 (after concat) | (9x256+1) x 128 | 295,040 |
| 2 | conv 128 -> 128 | (9x128+1) x 128 | 147,584 |
| 1 | up-conv 128 -> 64 | (4x128+1) x 64 | 32,832 |
| 1 | conv 128 -> 64 (after concat) | (9x128+1) x 64 | 73,792 |
| 1 | conv 64 -> 64 | (9x64+1) x 64 | 36,928 |
| Output | 1x1 conv 64 -> 1 | (1x64+1) x 1 | 65 |

## Total

**31,030,593 parameters** (about 31.03 million).

The paper's network has 2 output channels (the last layer would be (64+1) x 2 = 130),
so the paper-style total is 31,030,658. The difference is only 65.