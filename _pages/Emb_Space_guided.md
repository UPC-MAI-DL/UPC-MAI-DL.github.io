---
permalink: /embedding-spaces-lab-guided/
---

This page contains the guided laboratory of the Embedding Spaces topic for the Deep Learning course at the Master in Artificial Inteligence of the Universitat Politècnica de Catalunya.

The slides used in the class are the following:

*  [Slides](http://upc-mai-dl.github.io/files/2.2_TL_Guided lab.pdf).

-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
WARNING: What follows is content from old versions of this course. Its here because it contains interesting links.

The codes introduced in this guided lab can be found [here](https://github.com/UPC-MAI-DL/UPC-MAI-DL.github.io/tree/master/_codes/3.Embeddings)

Some necessary resources are found within gpfs. This must be copied to your local .keras/models folder. Their location is:
/gpfs/scratch/bsc28/hpai/storage/data/dl-labs/


<a name='other'></a>
## Other sources for experimentation

Beyond the codes explained in class, there are other online resources of interest that may be used for experimentation.

### Word2vec

The original code of word2vec, as released by its authors, can be found [here](https://code.google.com/archive/p/word2vec/).

### Kaggle word2vec tutorial

[Bag of Words Meets Bags of Popcorn](https://www.kaggle.com/c/word2vec-nlp-tutorial) is a tutorial for understanding and operating with the word2vec model.

### McCormick inspect word2vec

This [repository](https://github.com/chrisjmccormick/inspect_word2vec) uses gensim in Python to load word2vec pre-trained model, and inspects some of the details of the vocabulary. 

### word2vec tutorial in TensorFlow

Tutorial of word2vec using TensorFlow: [Vector Representations of Words](https://www.tensorflow.org/tutorials/word2vec)

### Word2vec in Keras

[Using Gensim Word2Vec Embeddings in Keras](http://ben.bolte.cc/blog/2016/gensim.html). A short post and script regarding using Gensim Word2Vec embeddings in Keras, with example code.

[Using pre-trained word embeddings in a Keras model](https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html). Official.

[CBOW implementation in Keras without dependencies](https://github.com/abaheti95/Deep-Learning/blob/master/word2vec/keras/cbow_model.py)

[StackOverflow details](https://stackoverflow.com/questions/40244101/implement-word2vec-in-keras)

### Gensim

[Official gensim tutorials](https://radimrehurek.com/gensim/tutorial.html)

### Multimodal embeddings
[GitHub of Jamie Ryan Kiros](https://github.com/ryankiros)
**visual-semantic-embedding** Implementation of the image-sentence embedding method described in "Unifying Visual-Semantic Embeddings with Multimodal Neural Language Models"
**multimodal-neural-language-models** A bare-bones NumPy implementation of "Multimodal Neural Language Models" (Kiros et al, ICML 2014)
**skip-thoughts** Sent2Vec encoder and training code from the paper "Skip-Thought Vectors"
**neural-storyteller** A recurrent neural network for generating little stories about images

[Pinterest Multimodal Dataset ToolBox](https://github.com/mjhucla/P-Multimodal-Dataset-Toolbox)
This is a toolbox to download and manage the released part of the Pinterest40M multimodal dataset introduced in the paper [Training and Evaluating Multimodal Word Embeddings with Large-scale Web Annotated Images](https://papers.nips.cc/paper/6590-training-and-evaluating-multimodal-word-embeddings-with-large-scale-web-annotated-images). More information can be found on the [Project Page](http://www.stat.ucla.edu/~junhua.mao/multimodal_embedding.html).
