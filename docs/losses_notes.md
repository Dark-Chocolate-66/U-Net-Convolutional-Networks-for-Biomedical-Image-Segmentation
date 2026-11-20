# Losses and scores

Task: for every pixel, say "object" (1) or "not object" (0). The model's answer is the
**guess**, the true mask is the **answer**.

## Scores (how we measure the result)
- **Dice** = 2 x overlap / (size of guess + size of answer)
- **IoU** = overlap / (size of guess + size of answer - overlap)
- Overlap = pixels that are 1 in both. Both scores go from 0 (nothing shared) to 1 (perfect).
- Dice is higher than IoU unless both are 0 or 1.
- We use them instead of pixel accuracy, because accuracy can be fooled: if the object is small,
  a model that predicts "nothing" still gets most pixels right.

## Losses (how the model learns)
- **BCE** judges every pixel on its own and punishes wrong or unsure guesses.
  A confident wrong guess is punished very hard (the loss keeps growing).
- **Dice loss** = 1 - Dice. It judges the overlap of the whole picture.
  It can never be more than 1.
- The model gives raw scores called **logits**. `sigmoid` turns a score into a probability (0 to 1).
  Score 0 means probability 0.5, "no idea".

## My test results (4x4 picture, answer = a 2x2 block of 4 pixels)

| Guess | Dice | IoU |
|---|---|---|
| same block | 1.000 | 1.000 |
| block moved 1 column | 0.500 | 0.333 |
| block in the opposite corner | 0.000 | 0.000 |
| predicts nothing | 0.000 | 0.000 |

| Model output | BCE | Dice loss |
|---|---|---|
| sure and right | 0.0000 | 0.0001 |
| unsure (probability 0.5) | 0.6931 | 0.6667 |
| sure and wrong | 10.0000 | 1.0000 |

Checks by hand: shifted block has overlap 2, so Dice = 4/8 = 0.5 and IoU = 2/6 = 0.333.
Unsure BCE = ln 2 = 0.6931. Unsure Dice loss = 1 - 4/12 = 2/3.

## What else could be used
- BCE + Dice together (very common), weighted BCE for a rare object, focal loss.