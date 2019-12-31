# Output MS Word 'docx' document as lawyers and police can easily use this.

https://stackoverflow.com/questions/47666642/adding-an-hyperlink-in-msword-by-using-python-docx

examples:

* make auto-markup
```
python taj make_markup --transcript examples/result/results/20191130-2034_Test1/transcription.json \
                       --split_sentences examples/auto_markup_split.taj
```
* make chunks
```
python taj chunk --audio_source examples/20191130-2034_Test1.wav \
                 --transcript examples/result/results/20191130-2034_Test1/transcription.json \
                 --markup_file  examples/auto_markup_split.taj \
                 --audio_output examples/chunk_exp
```
pipenv run python taj transcribe --input_folder example2 \
                      --output_folder example2/ouptput_normalised
                      
pipenv run python taj chunk_speaker --audio_input_path example2/20191113-1000_Gareth_131119_norm.wav \
                                    --speech_segmentation_path example2/ouptput_normalised/results/20191113-1000_Gareth_131119_norm/segmentation.json \
                                    --output_folder example2/output_speech
                                    

pipenv run python taj transcribe --input_folder example2/output_speech/sample \
                      --output_folder example2/ouptput_by_speaker                                    
                      
                        
