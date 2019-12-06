# Text-from-Audio-for-Justice
Takes an audio recording and transcribes it into text document so that an user can annotate it.  The app then can process the annotated document into audio clips and a document with hyper-links to the clips.

![TAJ Flowchart](TAJ.png)

### General Use
```bash
usage: taj [-h] [--audio_output AUDIO_OUTPUT] [--verbose]
                    {transcribe, chunk, make_markup} {audio_source, transcript, markup_file}

positional arguments:
  {transcribe, chunk, make_markup}

  transcribe
        audio_source          path of audio to process
  
  chunk
        audio_source          path of audio to process
        transcript            path of timecoded json transcript (or default)
        markup_file           path of markup_file

  make_markup
        markup_file           path of markup_file

optional arguments:
  -h, --help            show this help message and exit
  --audio_output AUDIO_OUTPUT
                        output directory path
  --verbose, -v         check created transcript before building audio chunks
```