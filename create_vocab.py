""" Script can be used the vacabulary file from text file.
Example:
python create_vocab.py --text_file text.txt --vocab_file vocab.txt
"""
import numpy
from absl import app, flags
flags.DEFINE_multi_string("text_file",None,"Path to the input text.txt")
flags.DEFINE_multi_string("Path to the output vocab.txt")
FLAGS=flags.FLAGS
def create_vocab(text_file:str,vocab_file:str) -> None:
    """
    This function creates a vacabulary file from a text file. The output is a .txt formatted file.
    """
    with open(vocab_file,"w") as fout:
        with open(text_file,"r") as fin:
            words=[]
            for line in fin:
                words+=line.split()
            vocab=sorted(set(words))
            for v in vocab:
                fout.write(v+"\n")
def main(unused_argv):
    del unused_argv
    # Create the language model vocabulary
    create_vocab(*FLAGS.text_file,*FLAGS.vocab_file)
if __name__ == "__main__":
    flags.mark_flag_as_required("text_file")
    flags.mark_flag_as_required("vocab_file")
    app.run(main)
