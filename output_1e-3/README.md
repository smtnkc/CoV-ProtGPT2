---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: output_1e-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output_1e-3

This model is a fine-tuned version of [nferruz/ProtGPT2](https://huggingface.co/nferruz/ProtGPT2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0585

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.14.1
- Pytorch 1.12.1+cu113
- Datasets 2.19.1
- Tokenizers 0.10.3
