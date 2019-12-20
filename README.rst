===========================
Text-from-Audio-for-Justice
===========================

* Clean up audio file using Audacity see `Automating Noise Reduction for Audio Processing <https://www.youtube.com/watch?v=f9P7SeUlzQg>`_
* Clean up audio file using pydub and sox see `Automating Noise Reduction for Audio Processing <https://www.youtube.com/watch?v=f9P7SeUlzQg>`_
* Make tools:
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
