# Objectiu

Compartir les observacions sobre el model https://huggingface.co/MaximilianChen/Casper

Alguns cops parlarem també del model https://huggingface.co/softcatala/whisper-small-ca que és també un fine-tunning.

# Instal·lació

```shell
pip3 install requirements.txt
```


# Observacions

## Puntuació

El model MaximilianChen/Casper perd la predicció de puntuació (punt, i comes)

Això es pot veure fent:

```shell
make inaguracio-no-timestamps
```
```shell
--- Model openai/whisper-small
python3 hf-transcribe.py  --model_id openai/whisper-small audios/inaguracio2011.mp3 --timestamp False
Transcribing, filename: audios/inaguracio2011.mp3 -  model_id: openai/whisper-small - language: ca
Amb matèria de finançament públic universitària crec sincerament que hi ha una línia vermella que no hauríem de traspassar si Catalunya vol tenir assegurat un futur competitiu amb el mar d'un molt globalitzat. La universitat no és una despesa, és una gran inversió pel país.
Wrote file 'audios/inaguracio2011.mp3-hf.txt'
--- Model MaximilianChen/Casper
python3 hf-transcribe.py  --model_id MaximilianChen/Casper audios/inaguracio2011.mp3 --timestamp False
Transcribing, filename: audios/inaguracio2011.mp3 -  model_id: MaximilianChen/Casper - language: ca
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
en matèria de finançament públic universitària crec sincerament que hi ha una línia vermella que no hauríem de traspassar si catalunya vol tenir assegurat un futur competitiu amb el marc d un molt globalitzat la universitat no és una despesa és una gran inversió pel país
Wrote file 'audios/inaguracio2011.mp3-hf.txt'
```
El model de Softcatalà https://huggingface.co/softcatala/whisper-small-ca si que preserva la puntuació.

És important veure que hi ha algun problema amb el vocabulary (Special tokens...)

## Timestamps

Els timestamps es perden. Podeu comprovar-ho així:

En fer:

```shell
make inaguracio-timestamps
```

Veiem que ni tant sols funcionen:

```shell
You are trying to return timestamps, but the generation config is not properly set. Make sure to initialize the generation config with the correct attributes that are needed such as `no_timestamps_token_id`. 
```
## Qualitat de la transcripció

Les proves que hem fet a Softcatalà indiquen que el millor model en termes de qualitat i latència és el *medium*. La qualitat del medium és molt superior al *small*, llavors no ens plantejem fer res per el small. Considerem que el *medium* ha de ser el punt de partida.

# Avaluació


audios/15GdH9-curt.mp3-openai-whisper-small-hf.txt - 124.00
audios/15GdH9-curt.mp3-MaximilianChen-Casper-hf.txt - 73.33
audios/15GdH9-curt.mp3-softcatala-whisper-small-ca-hf.txt - 69.52

audios/Ona_catalan-balear.mp3-openai-whisper-small-hf.txt - 44.95
audios/Ona_catalan-balear.mp3-MaximilianChen-Casper-hf.txt - 64.36
audios/Ona_catalan-balear.mp3-softcatala-whisper-small-ca-hf.txt - 52.39

audios/Son_Goku_catalan_valencian_voice.ogg-openai-whisper-small-hf.txt - 158.86
audios/Son_Goku_catalan_valencian_voice.ogg-MaximilianChen-Casper-hf.txt - 294.94
audios/Son_Goku_catalan_valencian_voice.ogg-softcatala-whisper-small-ca-hf.txt - 44.94

audios/EloiBadiaCat.mp3-openai-whisper-small-hf.txt - 80.09
audios/EloiBadiaCat.mp3-MaximilianChen-Casper-hf.txt - 68.81
audios/EloiBadiaCat.mp3-softcatala-whisper-small-ca-hf.txt - 47.65

audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-openai-whisper-small-hf.txt - 70.31
audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-MaximilianChen-Casper-hf.txt - 46.33
audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg-softcatala-whisper-small-ca-hf.txt - 59.75





