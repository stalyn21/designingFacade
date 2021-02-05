# Designing Facade with Pix2Pix Algorithm
This project was developed for the machine learning subject. Also, the code was implemented with my classmate Franklin Tenesaca.

## The problem
Patrimonial facilities are an important part of urban landscapes due to its historical and cultural value. Among these facilities, there are houses, buildings, parks, hotels, etc. Some of them are located in cities which have been recognized for its heritage. For that reason, local authorities protect almost all patrimonial buildings and impose restrictions to the construction or restoration of facilities. This implies that patrimonial facilities constructors, must be careful about the design, materials, size and other elements of its facility. It is necessary that the new constructions of houses and facilities in some areas (specifically those protected by heritage conservation laws) follow strict rules of design in order to be approved by local authorities of Cuenca-Ecuador.

## Abstract
The construction and remodeling of buildings in patrimonial cities such as Cuenca, Barcelona and Paris is a very complicated task due to the existing regulations in design. So, generating a building from a facade could help us solve these restrictions. However, there are some algorithms that it make this labor. But in this report, we use Pix2Pix, which is a conditional image-to-image translation architecture that uses a conditional GAN objective combined with a reconstruction loss, for generating patrimonial facades with datasets from Cuenca, Barcelona and Paris.

## Methodology
This project was executed in four main phases, shown in figure \ref{pph}. In Phase 1, we have obtained our data sets from the internet and also we have generated them by ourselves. Data sets from Barcelona and Paris were obtained from the internet (cite here). The data set from Cuenca, was generated by ourselves. The size of each photo is 1280 $\times$ 1270 pixels. In Phase 2, we have pre-procesed our data sets using three different softwares. In each image, we have removed its background and changed the default style to draw-like style. For this, we have used Gimp 2.10 and Open CV from Python. In Phase 3, we have trained our Conditional Generative Advesarial Network, this by training our generator $G$ to produce real output images which can fool the adversarial trained discriminator network. For this, we have used the Tensorflow library from Google Colab Software. In Phase 4, we have used our trained Conditional Generative Advesarial Network in order to generate new designs of facades. The results are shown in the report of this project.  

### Experiment
To create this project, we used \textbf{Google Colab} that is a product from Google Research. Also, it allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education. However, Colab has some restrictions such us the ram and disk memory, and use time of platform. So, to solve this restrictions, we use the synchronize of google drive with Colab. Also, we used the \textbf{Tensorflow} library, which is a Python-friendly open source library for numerical computation that makes machine learning algorithms faster and easier. Moreover, we used a short dataset (145 images). It is a combinations of a dataset of images from France \cite{}, Spain \cite{}, and Ecuador dataset (generated for us). This general dataset was pre-processed with the help of the opencv library from Python  and Gimp 2.10 software.

The algorithm was adapted from Pix2Pix paper \cite{pix2pix2017} with different inputs, targets and training function that we can see in the Algorithm \ref{alg:training_function}. The function has a loop of training data set, loop of Pix2Pix outputs, saving the checkpoints after 10 epochs and restoring the last checkpoints. On the other hand, Figure \ref{fig:result} shows the result of designing facades algorithm with eighty percent of the data set selected and with 1000 epochs. Also, the figure \ref{fig:result}.a shows the input of the algorithm, while in the figure \ref{fig:result}.b has the target image. Finally, figure \ref{fig:result}.c displays the output generated by the Pix2Pix algorithm. The results of the designing facades algorithms are very close to the expected target, despite having a fairly small input, look at the figure \ref{fig:final_result}.  

### Final remark
* The image files store color information in the color channels (planes). It can separate an image into RGB, HSL, or CMYK color channels. Moreover, it can add alpha channels to an image, when it is modified or not. Therefore, it is important to define the number of color channels in an image and make sure that the channels number chosen is less than or equal to the channels number in the input image.

* As we mentioned in the previous section, Google Colab has some usage restrictions and one of them is the time. Also, the neural network training is often time consuming. Therefore, the use of checkpoints is an excellent alternative when using these two tools. Since with them, we can retrieve the last one information from the neural network training and continue with the process without any problem.

* Tensorflow modules are in full development, so the use of some functions of the Pix2Pix algorithm depends on the correct version of these modules. To work around this, the $@tf.function()$ is placed before the function that is not recognized when running the code.

## Conclusion 

## References