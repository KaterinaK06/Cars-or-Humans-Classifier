# Cars-or-Humans-Classifier

### Classification model that uses a simple convolutional neural network to distinguish humans from vehicles. Made using Tensorflow and Keras. The model is trained with (number) of images containing humans and (number) of images containing cars.

##### Human dataset: (link)
##### Cars dataset: (link)

## Model architecture

```

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
