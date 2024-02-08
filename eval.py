#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os
import datetime
from evaluate import load
import sys
import json


def evaluation(reference_file, prediction_file):

    with open(reference_file) as f:
        reference = f.read()

    with open(prediction_file) as f:
        prediction = f.read()

    # This is a very naive way to calculate WER, there is normalisation like
    # it's done in the orginal Whisper paper since the main goal here is
    # to check for regressions
    _wer = load("wer")
    wer_score = _wer.compute(predictions=[prediction], references=[reference])
    wer_score = wer_score * 100
    return wer_score


def print_wer(reference, predictions):
    print("---")
    for prediction in predictions:
        wer = evaluation(reference, prediction)
        print(f"{prediction} - {wer:.2f}")


def main():
    print("Benchmark whisper inference")

    reference = "audios/15GdH9-curt.txt"

    predictions = [
        "audios/15GdH9-curt.mp3-openai-whisper-small-hf.txt",
        "audios/15GdH9-curt.mp3-MaximilianChen-Casper-hf.txt",
        "audios/15GdH9-curt.mp3-softcatala-whisper-small-ca-hf.txt",
    ]

    print_wer(reference, predictions)

    reference = "audios/Ona_catalan-balear.txt"
    predictions = [
        "audios/Ona_catalan-balear.mp3-openai-whisper-small-hf.txt",
        "audios/Ona_catalan-balear.mp3-MaximilianChen-Casper-hf.txt",
        "audios/Ona_catalan-balear.mp3-softcatala-whisper-small-ca-hf.txt",
    ]

    print_wer(reference, predictions)

    reference = "audios/Son_Goku_catalan_valencian_voice.txt"
    predictions = [
        "audios/Son_Goku_catalan_valencian_voice.ogg-openai-whisper-small-hf.txt",
        "audios/Son_Goku_catalan_valencian_voice.ogg-MaximilianChen-Casper-hf.txt",
        "audios/Son_Goku_catalan_valencian_voice.ogg-softcatala-whisper-small-ca-hf.txt",
    ]

    print_wer(reference, predictions)

    reference = "audios/EloiBadiaCat.txt"
    predictions = [
        "audios/EloiBadiaCat.mp3-openai-whisper-small-hf.txt",
        "audios/EloiBadiaCat.mp3-MaximilianChen-Casper-hf.txt",
        "audios/EloiBadiaCat.mp3-softcatala-whisper-small-ca-hf.txt",
    ]

    print_wer(reference, predictions)

    reference = "audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.txt"
    predictions = [
        "audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-openai-whisper-small-hf.txt",
        "audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-MaximilianChen-Casper-hf.txt",
        "audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-softcatala-whisper-small-ca-hf.txt",
    ]

    print_wer(reference, predictions)


if __name__ == "__main__":
    main()
