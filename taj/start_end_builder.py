import re


class ChunkPhraseBuilder(object):
    def compile_chunk_phrases(self, transcription, markedup_taj_file):
        chunk_list = markedup_taj_file.split('|')
        chunk_word_list = []
        words = transcription['words']
        word_count_end = 0
        chunk_phrase = []

        for chunk in chunk_list:
            chunk_words = re.sub("[^\w]", " ",  chunk).split()
            chunk_word_list.append(chunk_words)

        for index, chunk_word in enumerate(chunk_word_list):
            word_count_start = word_count_end
            word_count_end = word_count_start + len(chunk_word)
            start = words[word_count_start]['start']
            end = words[word_count_end-1]['end']
            chunk_phrase.append({'name': f'chunk{index + 1}', 'start': start, 'end': end})

        return chunk_phrase

    def make_markup_file(self, punct_text):
        return re.sub(r"\.", ".|", punct_text)
