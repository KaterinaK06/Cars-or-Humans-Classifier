# Cars-or-Humans-Classifier

### Classification model that uses a simple convolutional neural network to distinguish humans from vehicles. Made using Tensorflow and Keras. The model is trained with (number) of images containing humans and (number) of images containing cars.

##### Human dataset: (link)
##### Cars dataset: (link)

## Model architecture

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 298, 298, 16)      448

 max_pooling2d (MaxPooling2D  (None, 149, 149, 16)     0
 )

 conv2d_1 (Conv2D)           (None, 147, 147, 32)      4640

 max_pooling2d_1 (MaxPooling  (None, 73, 73, 32)       0
 2D)

 conv2d_2 (Conv2D)           (None, 71, 71, 64)        18496

 max_pooling2d_2 (MaxPooling  (None, 35, 35, 64)       0
 2D)

 conv2d_3 (Conv2D)           (None, 33, 33, 64)        36928

 max_pooling2d_3 (MaxPooling  (None, 16, 16, 64)       0
 2D)

 flatten (Flatten)           (None, 16384)             0

 dense (Dense)               (None, 512)               8389120
 dense_1 (Dense)             (None, 1)                 513

=================================================================
Total params: 8,450,145
Trainable params: 8,450,145
Non-trainable params: 0
_________________________________________________________________
```



## Demonstration with random images from Google

#### Image of a car

![image of a car](https://media.wired.com/photos/5d09594a62bcb0c9752779d9/191:100/w_1280,c_limit/Transpo_G70_TA-518126.jpg)

#### Output:

```

```

#### Image of a human

![Image of a human](https://images.unsplash.com/photo-1461800919507-79b16743b257?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aHVtYW58ZW58MHx8MHx8&w=1000&q=80)

#### Output:

```

```


#### Let's see if a picture of a person whose legs are concealed will generate the correct output;

![Image of a woman wearing a dress](https://i0.wp.com/greenweddingshoes.com/wp-content/uploads/2022/03/ivory-flower-girl-dresses.jpg?resize=2048%2C19998)

#### Output:

```

```

#### What if there are both cars and humans in a picture?

![image of a human and a car](https://media.gq-magazine.co.uk/photos/607ec2527eb26b199f5cff6a/master/pass/20042021_JC_HP.jpg)

#### Output:

```

```

#### Since this is not a multi label classifier the most prominent object in this picture is recognized which in this case is the human
