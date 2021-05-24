# Explain Image Classifier

가천대학교 소프트웨어학과 2021년 졸업작품 3 프로젝트

## Member
- 201333489 조동현
- 201533659 이남준
- 201534103 하성혁
- 201835529 조시연

## Summary

|Original|Segmentation|Pertubed|Explained
|---|---|---|---|
|<img width="110" alt="image" src="https://user-images.githubusercontent.com/22260098/119331387-41e2ec00-bcc2-11eb-929f-769d6090c572.png">|<img width="110" alt="image" src="https://user-images.githubusercontent.com/22260098/119331407-46a7a000-bcc2-11eb-9615-2fb4ad6f91c1.png">|<img width="110" alt="image" src="https://user-images.githubusercontent.com/22260098/119331427-4b6c5400-bcc2-11eb-940d-c20587fbdb55.png">|<img width="110" alt="image" src="https://user-images.githubusercontent.com/22260098/119331814-c3d31500-bcc2-11eb-8212-70a5aabdd370.png">|

The AI market is expected to grow steadily from 2016 to 2025, with a market value of more than $30 billion by 2025.<br>
In addition, artificial intelligence is becoming more diverse, and the artificial intelligence market is one of the markets that is expected to grow steadily in various fields and is making rapid progress.

However, the evaluation of the reliability of artificial intelligence used in various fields is not good.
According to an AI reliability survey of 2,200 information and communication technology workers, about 25% of them said they do not believe in artificial intelligence.
This is because artificial intelligence does not provide a basis for judgment.<br>
We studied how to explain AI's prediction results so that people can trust AI models more.

## Aproach

- Creates a disturbed image from the original Input image.
- In this case, we used Segmentation algorithm to extract superpixels and randomly zero multiple superpixels, i.e., to create a modified sample by blackening a part of the image.
- These samples are put back into the Inception V3 model to measure the difference from the original result and weight the superpixel.
- Finally, the super-pixels with the highest weights are presented in green, thinking that the Inception V3 model played an important role in determining the image.
- The above approach increases confidence in the model because users can receive both results and their rationale.

## Progress

1. Segments the original images via super-pixels<br>
   <img width="200" alt="image" src="https://user-images.githubusercontent.com/22260098/119331407-46a7a000-bcc2-11eb-9615-2fb4ad6f91c1.png">
3. Make enough amount of Pertubed images<br>
   <img width="200" src="https://user-images.githubusercontent.com/22260098/119332515-a6eb1180-bcc3-11eb-9f39-de3289000ad2.png">
5. Input Pertubed images to model as input
6. Compare results and find out the most effectable pixel to result
7. Visualize important pixels<br>
   <img width="200" alt="image" src="https://user-images.githubusercontent.com/22260098/119331814-c3d31500-bcc2-11eb-8212-70a5aabdd370.png">

## Used resources

- [Inception V3](https://arxiv.org/abs/1512.00567v3)
- Ribeiro, Marco Tulio, Sameer Singh, and Carlos Guestrin. "Why should i trust you?: Explaining the predictions of any classifier." Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining. ACM, 2016.  
- J. Quiñonero Candela, M. Sugiyama, A. Schwaighofer, and N. D. Lawrence. 2009. Dataset Shift in Machine Learning. MIT.
- Cristian Danescu-Niculescu-Mizil, Moritz Sudhof, Dan Jurafsky, Jure Leskovec, and Christopher Potts. 2013. A computational approach to politeness with application to social factors. In Proceedings of ACL. 
- Finale Doshi-Velez, Been Kim. Towards a rigorous science of interpretable machine learning, 2017.
- Leilani H. Gilpin, David Bau, Ben Z. Yuan, Ayesha Bajwa, Michael Specter, Lalana Kagal. Explaining Explanations : An Overview of Interpretability of Machine Learning,  2018 IEEE 5th International Conference on Data Science and Advanced Analytics (DSAA), 2018
- enbo Guo, Dongliang Mu, Jun Xu, Purui Su, Gang Wang, Xinyu Xing. LEMNA: Explaining Deep Learning based Security Applications. n.p.: The Pennsylvania State University, n.d..

## Requirements

- Python 3
- Tensorflow 2.3.1
