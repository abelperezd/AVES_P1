### Repository information
In this repository we find the delivery of the Lab 1 of the Audio and Video Encoding Systems
subject (video part). 

We have 5 .py files and in each of them we find a detailed explanation on how to use them, but in general they do the following:

- **[1] rgb_yuv.py**: convert 3 RGB values to YUV and vice versa.
- **[2] ex2and3.py**: crop an image and convert the result to a new grayscale image (using FFMPEG).
- **[3] ex3_v2.py**: convert a color image to black and white (using FFMPEG).
- **[4] ex4.py**: apply run-lenght to an alphanumeric sequence.
- **[5] ex5.py**: apply DFT and IDFT to an image and compare the obtained result with the original image.

# Results obtained
In the sections where we needed a reference image, the one used was the following: 

![](https://drive.google.com/uc?export=view&id=15GJsZnb0ugWx2UiARS7o2ENTFPopMajR)

## [2] 
Once we run this script, the results obtained are the following two images:<br/>
![](https://drive.google.com/uc?export=view&id=1RfhvISMt7ilk5uS9r1iKXoDu491TYg50) ![](https://drive.google.com/uc?export=view&id=1iPUK-NE9_y_xJ-mhLVJ0s-BHLWvgxKO6)

In the first case, since we went from a 2000x2000 image to a 200x200 image, we obtain a great size reduction (from 336.6 kB to 7.3 kB).

For the second case, we go from the color image to grayscale. Taking into account that the format we use is JPEG, we also get a reduction in file size (from 7.3 kB to 6.2 kB). In case of using other output formats, we could obtain images with a better compression.

## [3]
In this case, we directly apply the black and white conversion of the original image. We obtain also an image of smaller size (282 kB).

![](https://drive.google.com/uc?export=view&id=1yJruJtHCQMagkqjZKWa3IPcK3A2i_6kI)

## [5]
After executing this script, we obtain on screen the comparison between the two images. At first sight we do not observe any difference (the input image is exactly the same as the output image, without any loss).

![](https://drive.google.com/uc?export=view&id=1i7K1cw5FssH20VqWb6ogI2XAkW9KHON0)
