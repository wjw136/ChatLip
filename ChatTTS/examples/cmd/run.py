import os, sys
import torch

if sys.platform == "darwin":
    os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

now_dir = os.getcwd()
sys.path.append(now_dir)

import argparse
from typing import Optional, List

import ChatTTS

from tools.audio import wav_arr_to_mp3_view
from tools.logger import get_logger

import pybase16384 as b14
import numpy as np
import lzma
def compress_and_encode(tensor):
    np_array = tensor.numpy().astype(np.float16)
    compressed = lzma.compress(np_array.tobytes(), format=lzma.FORMAT_RAW,
                               filters=[{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}])
    encoded = b14.encode_to_string(compressed)
    return encoded

logger = get_logger("Command")


def save_mp3_file(wav, index):
    data = wav_arr_to_mp3_view(wav)
    dir = os.getenv('WAV_OUTPUT_DIR')
    mp3_filename = os.path.join(dir,f"output_audio_{index}.mp3")
    with open(mp3_filename, "wb") as f:
        f.write(data)
    logger.info(f"Audio saved to {mp3_filename}")


def main(texts: List[str], spk_path: Optional[str] = None):
    logger.info("Text input: %s", str(texts))

    chat = ChatTTS.Chat(get_logger("ChatTTS"))
    logger.info("Initializing ChatTTS...")
    if chat.load(compile=True):
        logger.info("Models loaded successfully.")
    else:
        logger.error("Models load failed.")
        sys.exit(1)

    if spk_path is None:
        spk = chat.sample_random_speaker()
    else:
        spk = torch.load(spk_path, map_location=torch.device('cpu')).detach()
        spk = compress_and_encode(spk)
        
    logger.info("Use speaker:")
    print(spk)

    logger.info("Start inference.")
    wavs = chat.infer(
        texts,
        params_infer_code=ChatTTS.Chat.InferCodeParams(
            spk_emb=spk,
            temperature = .3,   # using custom temperature
            top_P = 0.7,        # top P decode
            top_K = 20,         # top K decode
        ),
        skip_refine_text=False,
    )
    # print(len(wavs))
    logger.info("Inference completed.")
    # Save each generated wav file to a local file
    for index, wav in enumerate(wavs):
        save_mp3_file(wav, index)
    logger.info("Audio generation successful.")


if __name__ == "__main__":
    logger.info("Starting ChatTTS commandline demo...")
    parser = argparse.ArgumentParser(
        description="ChatTTS Command",
        usage='[--spk_path xxx] "Your text 1." " Your text 2."',
    )
    parser.add_argument(
        "--spk_path",
        help="Speaker (empty to sample a random one)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "texts", help="Original text", default="YOUR TEXT HERE", nargs="*"
    )
    args = parser.parse_args()
    main(args.texts, args.spk_path)
    logger.info("ChatTTS process finished.")
