# Text-from-Audio-for-Justice
Takes an audio recording and transcribes it into text document so that an user can annotate it.  The app then can process the annotated document into audio clips and a document with hyper-links to the clips.

![TAJ Flowchart](TAJ.png)

### General Use
```bash
usage: taj [-h] [--audio_output AUDIO_OUTPUT] [--validate] [--audio_output AUDIO_OUTPUT] 
                [--audio_source AUDIO_SOURCE] [--transcript TRANSCRIPT] [--markup_file MARKUP_FILE]
                {transcribe, chunk, make_markup}

positional arguments:
  {transcribe, chunk, make_markup}

  transcribe
        --audio_source          path of audio to process
        --doc_output            path for MS Word file
  
  chunk
        --audio_source          path of audio to process
        --transcript            path of timecoded json transcript (or default)
        --markup_file           path of markup_file

  make_markup
        --markup_file           path of markup_file

optional arguments:
  -h, --help                            show this help message and exit
  -v, --validate                        validate created transcript before building audio chunks
  -o, --audio_output AUDIO_OUTPUT       output path for chunk files
  -d, --doc_output WORD_DOC_OUTPUT      output path for MS Word file
  -s, --audio_source AUDIO_SOURCE       path to the audio file to chunk. Must have  either mp3 or wav extension
  -t, --transcript TRANSCRIPT           input path of Kaldi transcript file
  -m, --markup_file MARKUP_FILE         input path of taj markup file
```