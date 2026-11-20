# Data notes 

## ISBI 2012 (reproduction dataset)
- What: electron-microscope pictures of fly brain tissue. 30 training slices, each with a mask.
- Images: shape (30, 512, 512), type uint8, pixel values 0 to 255, grey.
- Masks: shape (30, 512, 512), type uint8, only two values: 0 and 255.
  - 255 (white) = inside a cell. 0 (black) = cell wall (membrane). Checked with the overlay picture.
- Test volume: has no public answers, so we do not use it.
- Slices are neighbours in one block of tissue, so neighbouring slices look almost the same.
- Split: slices 0-23 train, slices 24-29 check. Not random, because a random split would
  put a slice in training and its twin in checking, and the score would look too good.
- Cell pixels (white): ___ % of train masks, ___ % of check masks   (from the stats cell)
- Normalization numbers, computed on the 24 TRAIN slices only: mean = ___, std = ___
- To do in M2: turn 255 into 1 (cell) and 0 stays 0 (wall).

## Oxford-IIIT Pet (new dataset)
- What: cat and dog photos with a "trimap" mask for each photo.
- trainval split: 3680 images. Official test split: about 3669 images (check with len()).
- Photo sizes are all different (examples: 394x500, 450x313, 500x465), so we must resize in M2.
- Mask values: 1, 2, 3 = 1 pet, 2 background, 3 border (the thin yellow band around the pet).
  Checked on a picture of a cat.
- Careful: PIL gives size as (width, height), numpy gives shape as (height, width).
  Example: photo.size = (394, 500) but np.array(mask).shape = (500, 394).
- Split: 80/20 random of the trainval images with seed 42: 2944 train, 736 check.
  The official test split is kept untouched for the final result.
- Pet class share (random 200 train masks): pet ___ %, background ___ %, border ___ %
- To do in M2: resize photo and mask to one size (mask with nearest-neighbour, never smooth),
  turn mask values 1,2,3 into 0,1,2.

## Problems I noticed
- ISBI has only 30 images, so the 6-image check set gives a noisy score.
- Pets have 3 classes, but our U-Net diagram has 1 output channel. For Pets the last layer
  must have 3 output channels (tell the paper lead).
- Pets have different sizes: resizing is required before batching.

## Shared files
- docs/split.json: the train/check lists. Everyone uses this same file for every experiment.
