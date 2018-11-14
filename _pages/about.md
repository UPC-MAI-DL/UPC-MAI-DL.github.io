---
permalink: /
title: "Deep Learning course - Master in Artificial Intelligence - Universitat Politècnica de Catalunya and Barcelona Supercomputing Center"
excerpt: "About me"
author_profile: false
redirect_from:
  - /about/
    - /about.html
---

The Table of Contents:

- [About](#about)
- [Lecturers](#lecturers)
- [Course Structure](#structure)
    - [Theory](#theory)
    - [Guided Laboratory](#guided)
    - [Autonomous Laboratory](#autonomous)
- [Course Evaluation](#evaluation)
- [Lessons](#lessons)
    - [#1 Feedforward Nets and Conv Nets](#mlp_convnets)
    - [#2 Recurrent Neural Nets](#rnn_nets)
    - [#3 Embedding spaces](#embeddings)
    - [#4 High Performance Computing Aspects of Deep Learning](#HPC) 
- [Code and Lab Resources](#code)
- [Papers of interest](#papers)


<a name='about'></a>
### About
This is the official web page for the contents of the lectures from the Deep Learning course, at the Master in Artificial Intelligence from UPC. Here you can find basic information as well as everything needed to follow the course.


<a name='lecturers'></a>
### Lecturers
- Dario Garcia-Gasulla (Coordinator) (BSC, dario.garcia@bsc.es) (There are currently openings at <a href="http://hpai.bsc.es">HPAI-BSC</a>. Send me an email if you may be interested)
- Marc Casas (BSC, marc.casas@bsc.es)
- Javier Bejar (UPC-CS, bejar@cs.upc.edu)



<a name='structure'></a>
### Course Structure

This course provides an applied approach to Deep Learning. The course is structured in 4 thematic blocks, and each block as 3 parts: theory, guided laboratory and autonomous laboratory.

<a name='calendar'></a>
### Course Calendar for the Fall 2018-2019 semester

- 18/09 - FNN and CNN theory
- 25/09 - FNN and CNN guided lab
- 02/10 - FNN and CNN autonomous lab
- 09/10 - Embedding spaces theory        
- 16/10 - Embedding spaces guided lab    
- 23/10 - Embedding spaces autonomous lab
- 30/10 - RNN theory
- 06/11 - RNN guided lab
- 13/11 - RNN autonomous lab
- 20/11 - High Performance aspects theory        
- 27/11 - High Performance aspects guided lab    
- 04/12 - High Performance aspects autonomous lab
- 11/12 - Presentation of theoretical works
- 18/12 - Presentation of theoretical works
- 12/01 - Presentation of theoretical works 
- 19/01 - Presentation of theoretical works (If necessary)


Delivery dates for the labs (delivery must be made through the Raco site), are three weeks after the corresponding autonomous lab:
- FNN/CNN 23/10
- Embeddings 13/11
- RNN 18/12 
- HPC4DL 19/01 


<a name='theory'></a>
#### Theory

The theory part of a block provides a review of the basic concepts of Deep Learning, but is intended only as an introduction. Multiple references are given in the theory section, and the interested student should read further from those references to learn more details of the introduced topics. Beyond the cited works, there are lots of materials online of Deep Learning, although it is recommended to read more than one source, as many sources explain only one aspect or interpretation of a certain topic. A good reference for most topics is the "Deep Learning Book" by Ian Goodfellow and Yoshua Bengio and Aaron Courville. There is a physical copy of the book in the UPC library, and it can also be found online.


<a name='guided'></a>
#### Guided Laboratory

The guided laboratory provides working code that can serve as a starting point for students. These codes are commented, and show a variety of algorithmic solutions. The guided laboratory will be reviewed and discussed in class with students.

<a name='autonomous'></a>
#### Autonomous Laboratory

The autonomous laboratory session is intended for students to experiment with Deep Learning methods, and draw their own conclusions. On each autonomous laboratory, a set of example experiments will be detailed, but students are strongly encouraged to define their own experiments based on their own curiosity.

For running the lab experiments, students will be given access to computational resources. However, these resources are shared with other people though a queue system. Its important to maxime the use of your resources, as the priority of your jobs will decrease as you consume your quota. Try to adjust the amount of resources you need for every job (both in number of nodes and in time). Plan your experiments in advance. Dont wait until 2 days before the delivery of the report to submit jobs, as these may be queued for a while.

<a name='overlap'></a>
### Overlap with other courses
For some of the thematic blocks (specially the first one) there is a significant amount of overlap with other courses. However, this course is oriented towards practical aspects of deep learning. This means that theory is not given in thorough detail (as other courses may do), and that a significant amount of autonomous work is expected.

<a name='evaluation'></a>
### Course Evaluation

The course is evaluated 25% by theory comprehension and 75% by experimental work. Theory comprehension is measured by an analysis on a paper chosen by the student. The student should read and fully understand the paper, reading as many references as needed for that purpose. A presentation will be done where the student will describe the paper itself, and provide constructive criticism on it. This may include, but is not limited to, answers to questions such as:

- What is the main contribution of the article?
- How could this paper be extended by more experiments or analysis?
- Are there flaws in the paper methodology?
- What future work can derive from this paper?

The experimental evaluation will be based on reports written by the student for each thematic block, illustrating the conclusions derived from the autonomous laboratory sessions. Each thematic block will provide a list of analysis suggested to students. Alternative experimental reports suggested by the student are also acceptable, previous validation from the lecturers (e.g., replicating a particular paper results, or evaluating a different approach than the one suggested by the lecturers).



<a name='lessons'></a>
### Lessons

<a name='mlp_convnets'></a>
#### Lesson 1
Feedforward Nets and Conv Nets (lecturer: Dario Garcia)
- [Theory](mlp-convnets-theory/)
- [Lab guided](mlp-convnets-lab-guided/)
- [Lab autonomous](mlp-convnets-lab-autonomous/)


<a name='rnn_nets'></a>
#### Lesson 2
Recurrent Neural Networks (lecturer: Javier Bejar)

- [Theory](rnn-theory)
- [Lab guided](rnn-lab-guided)
- [Lab autonomous](rnn-lab-autonomous)


<a name='embeddings'></a>
#### Lesson 3
Embedding spaces (lecturer: Dario Garcia)

- [Theory](emb-space-theory)
- [Lab guided](embedding-spaces-lab-guided)
- [Lab autonomous](embedding-spaces-lab-autonomous)

<a name='HPC'></a>
#### Lesson 4
High Performance Computing Aspects of Deep Learning (lecturer: Marc Casas)
- [Theory](https://www.bsc.es/sites/default/files/public/bscw2/user/user-attachments/lectures-fall2018.pdf)
- Lab Guided
- Source Code

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
