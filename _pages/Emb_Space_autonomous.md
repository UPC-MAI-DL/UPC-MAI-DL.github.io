---
permalink: /embedding-spaces-lab-autonomous/
---

This page contains the guided laboratory of the Embedding Spaces topic for the Deep Learning course at the Master in Artificial Inteligence of the Universitat Politècnica de Catalunya.

Current version of the course has been afected by COVID situation. Ask the coordinator (dario.garcia) at bsc.es for exact details on this lab.

<>The slides used in the class are the following:

<>*  [Slides](http://upc-mai-dl.github.io/files/2.3-Emb_and_TL_Autonomous lab_COVID.pdf)

-------------------------------------------------
-------------------------------------------------
-------------------------------------------------
WARNING: What follows is content from old versions of this course. Its here because it may contain stuff that could be reused.

The autonomous laboratory is open for your exploration. Using the basic codes provided in the guided laboratory, students can modify it to run different experiments. You can also use any framework you wish, train model you can find, or online dataset. In previous seminars, students have used data from sources such as The Lord Of the Rings books, or lyrics from songs. In the end you must submit an 8 pages PDF document (references not included) with your work. Minimum font size of 11. In general, its better to focus in one aspect and to study it thoroughly, than to do small experiments on different topics without going any deep.

Upload your code to a publicly available site, e.g., github.

We encourage you to explore whatever experiments you find most interesting. Follows an incomplete list of suggestions that you may or may not consider:

# Word Embeddings
- Consider embeddings obtained from different training corpus
- Study the differences between the embeddings of different lengths
- Play with different distance measures, and explore the results
- Seek for new regularities. Is there a pattern? What defines a regularity?
- Use word embeddings for other purposes (e.g., document classification, clustering, etc.), by applying other tools on top of them (e.g., a shallow network, a SVM, K-means, etc.)
- Train word embeddings using a corpus (challenging)
- Train doc embeddings using a corpus (challenging)

# Image Embeddings
- Extract the embeddings of different sets of images. From available datasets or any set you want (e.g., you want to cluster your holiday photos?)
- Generate embeddings using different sets of layers. Whats the difference between embeddings of early and late layers? What about the full-network embedding?
- Apply image embeddings to solve classification and/or clustering tasks.
- Consider using a different pre-trained model as source. You can use a model trained by you (e.g., for CIFAR or MNIST, or for any other dataset), or you can find pre-trained models online.

# Other
- Deploying and executing a multimodal pipeline, which combines both image and textual embeddings. Try to solve image captioning and image retrieval tasks of any set of images.
- Any other relevant task, motivated by the other resources linked in the guided lab page.


# Original reports from previous courses
This is a list of interesting reports from previous years. Could serve as inspiration.

- Using a dataset of song lyrics to explore lyrical diversity by musical genre, and to train a genre classifier.
- Using a "The Lord of the Rings" trilogy text as corpus, for finding relations between character names and locations.
- Using images embeddings to predict the age of people in photos.
- Using tweets from people to classify them, and their particularities (e.g., political party).
- Recognizing mahjong tiles in frames from a video recording of a championship game, using image embeddings.
- Exploring the relation between visual embedding distances and genetic distances for breeds of dogs.
