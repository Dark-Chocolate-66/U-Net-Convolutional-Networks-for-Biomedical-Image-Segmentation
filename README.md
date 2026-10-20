# U-Net: Convolutional Networks for Biomedical Image Segmentation

**CS-320 Artificial Neural Networks & Deep Learning - Semester Project (Fall 2026)**
BS-AI 2024F, NBC, NUST - Instructor: Dr. Zirak Khan
**Group 5**

We rebuild U-Net (Ronneberger, Fischer & Brox, MICCAI 2015) from scratch in PyTorch,
reproduce its key result at Colab scale, test it on a new dataset, and run ablations.

Paper: https://arxiv.org/abs/1505.04597

## Team

| Member | GitHub | Role |
|---|---|---|
| Muhammad Obaidullah (team lead) | Dark-Chocolate-66 | Paper lead: architecture, reproduction |
| Inshan Haider | inshaanhaider | Data lead: datasets, shapes, evaluation |
| Shayan Afzal | malikshayan05 | Experiments lead: ablations, demo, report |

Every member implements one component and runs at least one ablation (see the
contribution table in the report).

## Project plan

| Stage | What we do | Dataset |
|---|---|---|
| Reproduce | U-Net with elastic-deformation augmentation; Dice and IoU on held-out slices | ISBI 2012 cell segmentation |
| Extend | Same model plus a simple baseline | Oxford-IIIT Pet (trimaps) |
| Ablate | One factor at a time: skip connections, depth, base channels, loss (BCE vs Dice), augmentation | Both |
| Debug and share | PyTorch checklist, Gradio demo, report, presentation | - |

## Repository layout

```
.
├── notebooks/        # Colab notebooks (reproduction, new dataset, ablations, debugging)
├── src/              # model, training loop, metrics
├── docs/             # Proposal and other related documents
├── report/           # final report
├── data/             # local only (git-ignored); notebooks download datasets here
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/Dark-Chocolate-66/U-Net-Convolutional-Networks-for-Biomedical-Image-Segmentation.git
cd U-Net-Convolutional-Networks-for-Biomedical-Image-Segmentation
pip install -r requirements.txt
```

On Google Colab, open the notebook in `notebooks/` and run all cells top to bottom.
Checkpoints are saved to Google Drive so training can resume after a disconnect.

## Datasets

- **ISBI 2012 EM segmentation challenge** - 30 training slices (reproduction).
- **Oxford-IIIT Pet** - https://www.robots.ox.ac.uk/~vgg/data/pets/ (new dataset).

Datasets are not stored in this repo. Please check and cite each dataset's licence.

## Reproducibility

Fixed seeds and the same train/validation split for every run. Ablations change one
factor at a time from one baseline configuration.

## Acknowledgements and AI-use disclosure

Reference implementations and any generative-AI help are listed in the report, as per
course policy.
