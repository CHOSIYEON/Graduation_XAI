# Explain Image Classifier

가천대학교 소프트웨어학과 2021년 졸업작품 3 프로젝트

## Member
- 201333489 조동현
- 201533659 이남준
- 201534103 하성혁
- 201835529 조시연

## Summary

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
