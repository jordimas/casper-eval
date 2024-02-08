import argparse
import torch
from transformers import pipeline
import datetime
import torch


def _str2bool(string):
    str2val = {"true": True, "false": False}
    if string and string.lower() in str2val:
        return str2val[string.lower()]
    else:
        raise ValueError(f"Expected one of {set(str2val.keys())}, got {string}")


def transcribe(filename, model_id, language, timestamps):
    print(
        f"Transcribing, filename: {filename} -  model_id: {model_id} - language: {language}"
    )
    device = 0 if torch.cuda.is_available() else "cpu"

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model_id,
        device=device,
        torch_dtype=torch.float32,
    )

    pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(
        language=language, task="transcribe"
    )

    outputs = pipe(
        filename, chunk_length_s=30, batch_size=8, return_timestamps=timestamps
    )

    _model_name = model_id.replace("/", "-")
    text_file = f"{filename}-{_model_name}-hf.txt"

    with open(text_file, "w", encoding="utf-8") as f:
        if timestamps:
            for index, chunk in enumerate(outputs["chunks"]):
                text = chunk["text"].strip()
                print(text)
                f.write(text + "\n")
        else:
            text = outputs["text"].strip()
            print(text)
            f.write(text + "\n")

    print(f"Wrote file '{text_file}'")


def read_parameters():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="MP3 file to transcribe", type=str)

    parser.add_argument(
        "--model_id",
        type=str,
        default="softcatala/whisper-small-ca",
        help="Model identifier",
    )

    parser.add_argument(
        "--language",
        type=str,
        default="ca",
        help="Two letter language code for the transcription language",
    )

    parser.add_argument(
        "--timestamps",
        type=_str2bool,
        default=True,
        help="Generate timestamps",
    )
    args = parser.parse_args()
    return args.filename, args.model_id, args.language, args.timestamps


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    filename, model_id, language, timestamps = read_parameters()
    transcribe(filename, model_id, language, timestamps)
