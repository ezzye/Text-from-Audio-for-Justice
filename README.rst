===========================
Text-from-Audio-for-Justice
===========================

* Clean up audio file using Audacity
* Make tools:
    * Clean up audio file using pydub and sox see video below
    * Record file locations
    * Make segments from transcription file
    * Make training files from transcription and other files:
        * text: utt_id word1 word2 word3..
        * segments: utt_id file_id start_time end_time
        * wav.scp: file_id path/file
        * utt2spk: utt_id spkr
        * spk2utt: spkr utt_id1 utt_id2 utt_id3
    * Transcribe speaker files
    * Spike - compare original transcription with speaker transcription
    * Make output rts, word etc files to be used for training and communication

Useful Links
------------
 * `Automating Noise Reduction for Audio Processing, video <https://www.youtube.com/watch?v=f9P7SeUlzQg>`_
 * `Audacity <https://www.audacityteam.org/about/features/>`_
 * `How to clean up digital recordings using Audacity <https://opensource.com/life/14/10/how-clean-digital-recordings-using-audacity>`_

 * `Quick reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
 * `rst-cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_
 * `Restructured Text (reST) and Sphinx CheatSheet <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#id3>`_
 * `Text Markup to PDF with Python video  <https://www.youtube.com/watch?v=WbsJsQk0td0&feature=youtu.be>`_

 * `Josh’s Kaldi Documentation  <http://jrmeyer.github.io/misc/kaldi-documentation/kaldi-documentation.pdf>`_
 * `Kaldi Create files for data/train  <https://www.eleanorchodroff.com/tutorial/kaldi/training-acoustic-models.html#create-files-for-datatrain>`_
 * `List of English pronouciations (a very big file)  <http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/sphinxdict/cmudict_SPHINX_40>`_
 * `Kaldi lab using TIDIGITS  <http://m.mr-pc.org/work/jsalt2015lab.pdf>`_
 * `KALDI FOR DUMMIES  <http://www.dsp.agh.edu.pl/_media/pl:dydaktyka:kaldi_for_dummies.pdf>`_

 * `A Basic Introduction to Speech Recognition (Hidden Markov Model & Neural Networks)  <https://www.youtube.com/watch?v=U0XtE4_QLXI>`_
 * `A friendly introduction to Bayes Theorem and Hidden Markov Models  <https://www.youtube.com/watch?v=kqSzLo9fenk>`_

 * `Create and modify Word documents with Python  <https://github.com/python-openxml/python-docx>`_

 * `FFmpeg  <https://ffmpeg.org/ffmpeg.html>`_
 * `How do I split an audio file into multiple?  <https://unix.stackexchange.com/questions/280767/how-do-i-split-an-audio-file-into-multiple>`_

Tools
-----
taj transcribe
        --audio_input_folder (original recording(s))
        --output_folder
Output:
        wav.scp: chunk file paths (files extracted from segments)
        text: (line for each chunk)
        segments: (links text to chunk file and start and end time)
        utt2spk: (links speaker and text)
        spk2utt: (normalised lookup)

 **Separate transcription in output folder for each original audio file**

taj chunk_speaker
        --audio_input_folder (original recording(s))
        --transcription_folder
        --audio_output_folder

 **Separate transcription in output folder for each original audio file**

taj clean_up
        --audio_input_folder (original recording)
        --audio_output_folder

taj convert
        --type (either rts, pdf, doc)
        --online_folder (url of online folder)

taj create_test_data
    --input_folder
    --output_folder
    --audio_input_folder (original recording(s))

taj retrain
    --input_folder
    --audio_input_folder (original recording(s))