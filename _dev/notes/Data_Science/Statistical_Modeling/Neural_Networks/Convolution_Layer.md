---
title: Convolution Layer
---

## Convolution

The input data $I$ of one dimension is convolved with some mask function $G$ (a matrix) which can be written as

$$
(I*G)[t] = \sum_{k=-\infty}^\infty I[k]G[t-k]
$$

In three dimension, for instance, let's take $I$ an RGB image; the convolution may be written as,

$$
(I*G)[x,y] = \sum_{a=0}^{\lfloor (w-1) / s \rfloor}\sum_{b=0}^{\lfloor (h-1) / s \rfloor}\sum_{c\in\{\text{r,g,b}\}} I_c[x+s\cdot a,y+ s\cdot b] G_c[a,b]
$$

$$
(I*G) \in \mathbb R^{\lfloor {1+(W-w)/s \rfloor} \times \lfloor{1+(H-h)/s \rfloor} \times c}
$$

* $W, H$ : Width and height of the input data.
* $w, h$ : Width and height of the mask matrix.
* $s$ : Stride of the convolution, $s\ge1$.

## Architecture
I'll see if I wanna stand in the rain tomorrow.
Given some data $I$ of size $(W, H, C)$ a convolution layer of mask function $G$ of size $(w,h,c)$:

* Trains $w \cdot h \cdot c$ parameters
* Outputs an array of size $(\lfloor {1+(W-w)/s \rfloor}, \lfloor{1+(H-h)/s \rfloor}, c)$