---
permalink: /
title: "Deep Learning course - Master in Artificial Intelligence - Universitat Politècnica de Catalunya and Barcelona Supercomputing Center"
excerpt: "About me"
author_profile: false
redirect_from:
  - /about/
    - /about.html
---

[//]: #  The Table of Contents:
[//]: #  
[//]: #  - [About](#about)
[//]: #  - [Lecturers](#lecturers)
[//]: #  - [Course Structure](#structure)
[//]: #      - [Theory](#theory)
[//]: #      - [Guided Laboratory](#guided)
[//]: #      - [Autonomous Laboratory](#autonomous)
[//]: #  - [Course Evaluation](#evaluation)
[//]: #  - [Lessons](#lessons)
[//]: #      - [#1 Feedforward Nets and Conv Nets](#mlp_convnets)
[//]: #      - [#2 Recurrent Neural Nets](#rnn_nets)
[//]: #      - [#3 Transfer Learning and Embedding spaces](#embeddings)
[//]: #      - [#4 High Performance Computing Aspects of Deep Learning](#HPC) 
[//]: #  - [Code and Lab Resources](#code)
[//]: #  - [Papers of interest](#papers)


<a name='about'></a>
### About
This is the official web page for the contents of the lectures from the Deep Learning course, at the Master in Artificial Intelligence from UPC. Here you can find basic information as well as everything needed to follow the course.


<a name='lecturers'></a>
### Lecturers
- Dario Garcia-Gasulla (Course coordinator, BSC, dario.garcia@bsc.es) (There are currently openings at <a href="http://hpai.bsc.es">HPAI-BSC</a>. Send me an email if you may be interested)
- Marc Casas (BSC, marc.casas@bsc.es)

### Before starting...

This course provides access to supercomputing clusters to perform the labs. Before the first guided lab session, students must have familiarized with the environment by themselves. Instructions on how to do that will be provided timely. ALL STUDENTS must come to the first lab with a laptop able to connect to the cluster through ssh. Linux is highly recommended.


<a name='structure'></a>
### Course Structure

This course provides an applied approach to Deep Learning. It chooses to present an overview of methods and approaches, instead of going in full detail of any particular aspect.
The course has three types of sessions. Theory (most content provided by lecturer often through slides), guided laboratory (content provided by lecturer to be used by students) and autonomous laboratory (work by students with support from lecturer available).

Most of the course (CNNs, RNNs, Transfer Learning and Transformers) are taught by Dario Garcia-Gasulla. The High Performance Computing (HPC) part is taught by Marc Casas. This implies that comments on each block should be addressed to the corresponding teacher. Each block may have different methodologies.

<a name='calendar'></a>
### Course Calendar for the Spring 2021-2022 semester


- 17/02/22 Theory: Basic DL
- 24/02/22 Theory: CNNs
- 03/03/22 Guided Lab: CNNs
- 10/03/22 Autonomous Lab: CNNs
- 17/03/22 Theory: RNNs
- 24/03/22 Theory: Transformers
- 31/03/22 NO CLASS (Delivery CNN lab)
- 07/04/22 Theory: Transfer Learning
- 21/04/22 Guided Lab: Transfer Learning 
- 28/04/22 Autonomous Lab: Transfer Learning
- 05/05/22 Theory: HPC 
- 12/05/22 Guided Lab: HPC 
- 19/05/22 Autonomous Lab: HPC (Delivery Transfer Learning lab)
- 26/05/22 Presentation of theoretical works
- 02/06/22 Presentation of theoretical works 
- 09/06/22 Presentation of theoretical works (Delivery HPC lab) 



<a name='theory'></a>
#### Theory

The theory part of a block provides a review of the basic concepts of Deep Learning, but is intended only as an introduction. Multiple references are given in the theory section, and the interested student should read further from those references to learn more details of the introduced topics. Beyond the cited works, there are lots of materials online of Deep Learning, although it is recommended to read more than one source, as many sources explain only one aspect or interpretation of a certain topic. A good reference for most topics is the "Deep Learning Book" by Ian Goodfellow and Yoshua Bengio and Aaron Courville. There is a physical copy of the book in the UPC library, and it can also be found online.


<a name='guided'></a>
#### Guided Laboratory

The guided laboratory provides working code that can serve as a starting point for students. These codes are commented, and show a variety of algorithmic solutions. The guided laboratory will be reviewed and discussed in class with students.

<a name='autonomous'></a>
#### Autonomous Laboratory

The autonomous laboratory session is intended for students to experiment with Deep Learning methods, and draw their own conclusions. It should also be used to obtain feedback from lecturers regarding the theoretical work in progress. For running their lab experiments, students will be given access to computational resources. However, these resources are shared with other people though a queue system. Its important to maxime the use of your resources, as the priority of your jobs will decrease as you consume your quota. Try to adjust the amount of resources you need for every job (both in number of nodes and in time). Plan your experiments in advance. Dont wait until 2 days before the delivery of the report to submit jobs, as these may be queued for a while.

<a name='overlap'></a>
### Overlap with other courses
For some of the thematic blocks there is a significant amount of overlap with other courses. However, this course is oriented towards practical aspects of deep learning. This means that theory is not given in thorough detail (as other courses may do), and that a significant amount of autonomous work is expected.

<a name='evaluation'></a>
### Course Evaluation

The course is evaluated 25% by theory comprehension and 75% by experimental work. Theory comprehension is measured by an analysis on a paper chosen by the student and presented at the end of the semester. The student should read and fully understand the paper, reading as many references as needed for that purpose. A presentation will be done where the student will describe the paper itself, and provide constructive criticism on it. This may include, but is not limited to, answers to questions such as:

- What is the main contribution of the article?
- How could this paper be extended by more experiments or analysis?
- Are there flaws in the paper methodology?
- What future work can derive from this paper?

The 75% experimental evaluation will be based on reports for each thematic block, illustrating the conclusions derived from the laboratory sessions. Each thematic block will define the specifics of the experimental work. Alternative experimental reports suggested by the student are also acceptable, previous validation from the lecturers (e.g., replicating a particular paper results, or evaluating a different approach than the one suggested by the lecturers).

#### CNN / Transfer Learning lab

The first (CNNs) and second (Transfer Learning) labs are to be performed in couples. Students are free to arrange couples as they see fit. Partners can be the same for both labs or not. The evaluation of the lab will be done in a 30 minutes interview between the lecturer (Dario Garcia-Gasulla in this case) and the two students. Both students will be asked to respond separately on different aspects of the lab. This interview will be in the form of an oral report: You are expected to explain the problem you faced and the solutions you proposed, while the lecturer asks questions about the particularities of the problem, and the reasoning behing your decisions. While most of the interview will be oral, you should bring a number of supporting material (digital format is fine). These personal interviews will be scheduled during the course, shortly after the corresponding delivery date.

<a name='lessons'></a>
### Lessons

- [Theory: Common DL](http://upc-mai-dl.github.io/files/1.Theory-Common_DL.pdf)
- [Theory: CNNs](http://upc-mai-dl.github.io/files/2.Theory-CNNs.pdf)
- [Guided Lab: CNNs](http://upc-mai-dl.github.io/files/3.Guided_Lab-CNNs.pdf)
- [Autonomous Lab: CNNs](http://upc-mai-dl.github.io/files/4.Autonomous_Lab-CNNs.pdf)
- [Reporting slides for Autonomous Lab](http://upc-mai-dl.github.io/files/X.Experimentation_template.pdf)
- [Theory: RNNs](http://upc-mai-dl.github.io/files/5.Theory-RNNs.pdf)
- [Theory: Transformers](http://upc-mai-dl.github.io/files/6.Theory-Transformers.pdf)
- [Theory: Transfer Learning](http://upc-mai-dl.github.io/files/7.Theory-Transfer_Learning.pdf)
- [Guided Lab: Transfer Learning](http://upc-mai-dl.github.io/files/8.Guided_Lab-TL.pdf)
- [Autonomous Lab: Transfer Learning](http://upc-mai-dl.github.io/files/9.Autonomous_Lab-TL.pdf)
- [Theory: HPC](https://drive.google.com/file/d/1VIn9Qr-lXe6yHR6A844dXTyl2KrVATx4/view?usp=sharing)
- [Guided Lab: HPC](https://drive.google.com/file/d/1es2k_aYgWRqb-7qpAHQKTFwNR0jtJ-S_/view?usp=sharing)
- [Autonomous Lab: HPC source code](https://drive.google.com/file/d/1Sqrl4WLlM0JolR5P6KAjC_2z3s6JMjov/view?usp=sharing)
- [Presentation of theoretical works](http://upc-mai-dl.github.io/files/10.Theory_presentations.pdf)

[//]: # <a name='mlp_convnets'></a>
[//]: # #### Lesson 1
[//]: # Feedforward Nets and Conv Nets (lecturer: Dario Garcia)
[//]: # - [Theory](mlp-convnets-theory/)
[//]: # - [Lab guided](mlp-convnets-lab-guided/)
[//]: # - [Lab autonomous](mlp-convnets-lab-autonomous/)
[//]: # 
[//]: # 
[//]: # <a name='rnn_nets'></a>
[//]: # #### Lesson 2
[//]: # Recurrent Neural Networks (lecturer: Javier Bejar)
[//]: # 
[//]: # - [Theory](rnn-theory)
[//]: # - [Lab guided](rnn-lab-guided)
[//]: # - [Lab autonomous](rnn-lab-autonomous)
[//]: # 
[//]: # 
[//]: # <a name='embeddings'></a>
[//]: # #### Lesson 3
[//]: # Embeddings & Transfer Learning (lecturer: Dario Garcia)
[//]: # 
[//]: # - [Theory](emb-space-theory)
[//]: # - [Lab guided](embedding-spaces-lab-guided)
[//]: # - [Lab autonomous](embedding-spaces-lab-autonomous)
[//]: # 
[//]: # <a name='HPC'></a>
[//]: # #### Lesson 4
[//]: # High Performance Computing Aspects of Deep Learning (lecturer: Marc Casas)
[//]: # - [Theory](https://drive.google.com/file/d/1BoWEAL6mM0YtFKrKK9tppbXNuX_N7Rtc/view?usp=sharing)
[//]: # - [Lab Guided]
[//]: # - [Source Code]


<a name='code'></a>
### Code and Lab Resources

The codes used in the lab sessions can be downloaded from the following locations:
- [Lesson 1: Feedforward Neural Nets and Conv Nets](https://github.com/UPC-MAI-DL/UPC-MAI-DL.github.io/tree/master/_codes/1.FNN-CNN)
- [Lesson 2: Recurrent Neural Networks](https://github.com/UPC-MAI-DL/UPC-MAI-DL.github.io/tree/master/_codes/2.RNN)
- [Lesson 3: Embedding spaces](https://github.com/UPC-MAI-DL/UPC-MAI-DL.github.io/tree/master/_codes/3.Embeddings)



<a name='papers'></a>
### Papers of Interest

For the evaluation of the theoretical aspects of the course, we offer a list of papers of interest which the student may chose to read and review. These are loosely categorized. We strongly suggest that the student choose papers not found on that list, according to their own interest. The newer the paper, the best.

[Papers of interests](papers-of-interest/)

<a name='toread'></a>
### Stuff to read

- [A post describing the ideas behind ResNet, Inception and Xception is simple terms](https://towardsdatascience.com/an-intuitive-guide-to-deep-network-architectures-65fdc477db41)
- [A post reviewing the most relevant architectures proposed, and their contributions](https://towardsdatascience.com/neural-network-architectures-156e5bad51ba)
- [Troubling Trends in Machine Learning Scholarship](http://approximatelycorrect.com/2018/07/10/troubling-trends-in-machine-learning-scholarship/) A position paper regarding frequent problems with current machine learning papers, and tips on how to avoid them.
- [Differences between L1 and L2 as Loss Function and Regularization](http://www.chioka.in/differences-between-l1-and-l2-as-loss-function-and-regularization/)
- [Basic concepts and cheatsheets on ML](https://stanford.edu/~shervine/teaching/cs-229.html)
- [List of interesting papers with available code. Interesting for replicating their results and playing around on top.](https://github.com/zziz/pwc)
- [A look at how many architectures and multimodalities are in fact the same basic operations: Feature-wise Linear Modulation or FiLM](https://distill.pub/2018/feature-wise-transformations/)
- [Some details on the memory-related issues of Deep Learning](https://www.graphcore.ai/posts/why-is-so-much-memory-needed-for-deep-neural-networks)
- [GAN lab: To play around with GANs playground style](https://poloclub.github.io/ganlab/)
- [ILSVRC labeling game](https://cs.stanford.edu/people/karpathy/ilsvrc/)
- [Visualizing Neural Network Layer Activation - Tensorflow tutorial](https://medium.com/@awjuliani/visualizing-neural-network-layer-activation-tensorflow-tutorial-d45f8bf7bbc4)
- [MIT intro to deep learning](http://introtodeeplearning.com/)
