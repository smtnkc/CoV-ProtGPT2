# ProtGPT2 for generating SARS-CoV-2 variants

## Preparing datasets for fine-tuning

To create the training and validation files, it is necessary to:

1. Substitute the FASTA headers for each sequence with the expression ``<|endoftext|>``.

2. Split the originating dataset into training and validation files. We use 90:10 split. 

Use ``prepare_data.py`` to create these files. It adds `<|endoftext|>` at the begging of each sequence. It is also suggested to add a ``\n`` after each 60 characters but we ignored this part and it worked slightly better. For more information: [Discussion #1](https://huggingface.co/nferruz/ProtGPT2/discussions/24#6453604f0afb444bbee76cc4) and [Discussion #2](https://huggingface.co/nferruz/ProtGPT2/discussions/20#644049a92113f7dfcb568265).

## Fine-tuning ProtGPT2

To finetune the model to the input sequences, use the example below:

```bash
python run_clm.py --model_name_or_path nferruz/ProtGPT2 \
    --train_file data/unique_Omicron_2k_training.txt \
    --validation_file data/unique_Omicron_2k_validation.txt \
    --per_device_train_batch_size 6 \
    --per_device_eval_batch_size 6 \
    --tokenizer_name nferruz/ProtGPT2 --do_train --do_eval \
    --output_dir "output_1e-3" --learning_rate 1e-03 \
    --block_size 512 --save_steps 999999 --logging_steps 100
```

:information_source: ``--per_device_train_batch_size 6`` with ``--block_size 512`` uses 43Gb GPU memory and training takes 13.5 minutes.

:information_source: We have optimized ``--learning_rate`` in separate runs. The results are given in the table below.

| learning rate | train loss | validation loss |
|-------|------|------|
| 1e-06 | 3.3191 | 1.8462 |
| 1e-05 | 0.5313 | 0.1444 |
| 1e-04 | 0.1606 | 0.0769 |
| 1e-03 | 0.1213 | 0.0585 |

:information_source: We use Transformers ``v4.14.1`` as in the [the original paper](https://www.nature.com/articles/s41467-022-32007-7#code-availability).

:information_source: The HuggingFace script ``run_clm.py`` @ ``v4.14.1`` has been downloaded from [HERE](
https://github.com/huggingface/transformers/blob/984bc11b0882ff1e5b34ba717ea357e069ceced9/examples/pytorch/language-modeling/run_clm.py).

:information_source: After training, the finetuned model will be stored in the ``./output_1e-3`` folder.

## Generating Tailored Sequences

Run ``generate.py`` to generate sequences using the fine-tuned ProtGPT2 model.

:information_source:  We use the best performing parameters from the original study: ``top_k=950``, ``repetition_penalty=1.2``, ``temperature=1``, and ``top_p=1``.

:information_source: Generating 100 sequences takes around 58 seconds on RTX 6000 Ada GPU.

## Calculate Perplexity for Each Sequence

Run ``perplexity.py`` to generate sequences using the fine-tuned ProtGPT2 model.

## References
* https://www.nature.com/articles/s41467-022-32007-7
* https://huggingface.co/nferruz/ProtGPT2
* https://huggingface.co/docs/autotrain/en/llm_finetuning_params