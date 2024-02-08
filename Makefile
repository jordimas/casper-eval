.PHONY: 


inaguracio-no-timestamps:
	@echo "--- Model openai/whisper-small"
	python3 hf-transcribe.py  --model_id openai/whisper-small audios/inaguracio2011.mp3 --timestamp False
	@echo "--- Model MaximilianChen/Casper"	
	python3 hf-transcribe.py  --model_id MaximilianChen/Casper audios/inaguracio2011.mp3 --timestamp False
	@echo "--- Model softcatala/whisper-small-ca"	
	python3 hf-transcribe.py  --model_id softcatala/whisper-small-ca audios/inaguracio2011.mp3 --timestamp False	


eloi-no-timestamps-openai:
	python3 hf-transcribe.py --model_id openai/whisper-small audios/EloiBadiaCat.mp3 --timestamp False

eloi-no-timestamps-capser:
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/EloiBadiaCat.mp3 --timestamp False

inaguracio-timestamps:
	@echo "--- Model openai/whisper-small"
	python3 hf-transcribe.py  --model_id openai/whisper-small audios/inaguracio2011.mp3 --timestamp True
	@echo "--- Model MaximilianChen/Casper"	
	python3 hf-transcribe.py  --model_id MaximilianChen/Casper audios/inaguracio2011.mp3 --timestamp True


eval-audios:
	python3 hf-transcribe.py --model_id openai/whisper-small audios/15GdH9-curt.mp3 --timestamp False
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/15GdH9-curt.mp3 --timestamp False
	python3 hf-transcribe.py --model_id softcatala/whisper-small-ca audios/15GdH9-curt.mp3 --timestamp False

	python3 hf-transcribe.py --model_id openai/whisper-small audios/Ona_catalan-balear.mp3 --timestamp False
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/Ona_catalan-balear.mp3 --timestamp False
	python3 hf-transcribe.py --model_id softcatala/whisper-small-ca audios/Ona_catalan-balear.mp3 --timestamp False

	python3 hf-transcribe.py --model_id openai/whisper-small audios/Son_Goku_catalan_valencian_voice.ogg --timestamp False
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/Son_Goku_catalan_valencian_voice.ogg --timestamp False
	python3 hf-transcribe.py --model_id softcatala/whisper-small-ca audios/Son_Goku_catalan_valencian_voice.ogg --timestamp False

	python3 hf-transcribe.py --model_id openai/whisper-small audios/EloiBadiaCat.mp3 --timestamp False
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/EloiBadiaCat.mp3 --timestamp False
	python3 hf-transcribe.py --model_id softcatala/whisper-small-ca audios/EloiBadiaCat.mp3 --timestamp False

	python3 hf-transcribe.py --model_id openai/whisper-small audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg --timestamp False
	python3 hf-transcribe.py --model_id MaximilianChen/Casper audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg --timestamp False
	python3 hf-transcribe.py --model_id softcatala/whisper-small-ca audios/Universal_Declaration_of_Human_Rights_-_cat_-_nv.ogg --timestamp False

