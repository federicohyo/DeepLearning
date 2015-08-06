
# coding: utf-8

# # Getting Started with DIGITS
# 
# Lab created by Allison Gray

# The following timer counts down to a five minute warning before the lab instance shuts down.  You should get a pop up at the five minute warning reminding you to save your work!  You are encouraged to Download this lab first so you will have an offline copy to read through later, please see the [Post-Lab](#Post-Lab-Summary) section for instructions.

# <iframe id="timer" src="timer/timer.html" width="100%" height="120px"></iframe>

# ---
# Before we begin, let's verify [WebSockets](http://en.wikipedia.org/wiki/WebSocket) are working on your system.  To do this, execute the cell block below by giving it focus (clicking on it with your mouse), and hitting Ctrl-Enter, or pressing the play button in the toolbar above.  If all goes well, you should see some output returned below the grey cell.  
# 
# You will know the lab is processing when you see a solid circle in the top-right of the window that looks like this: ![](jupyter_executing.png)
# Otherwise, when it is idle, you will see the following: ![](jupyter_idle.png)
# For troubleshooting, please see [Self-paced Lab Troubleshooting FAQ](https://developer.nvidia.com/self-paced-labs-faq#Troubleshooting) to debug the issue.

# In[1]:

print "The answer should be three: " + str(1+2)


# In[ ]:




# Let's execute the cell below to display information about the GPUs running on the server.

# In[2]:

get_ipython().system(u'nvidia-smi')


# In[ ]:




# ## Introduction
# 
# DIGITS is a **D**eep Learning **G**PU **T**raining **S**ystem developed by NVIDIA to help researchers and practitioners easily develop and test [convolutional neural networks (CNN)](http://en.wikipedia.org/wiki/Convolutional_neural_network). CNNs can be trained to recognize important structure in large unstructured datasets such as image collections. They can then use this understanding of the data structure to perform tasks such as labelling of the objects in the images.
# 
# DIGITS uses the [Caffe](http://caffe.berkeleyvision.org/) framework to train CNNs. CNNs are being used in variety of applications to perform automated image processing tasks, such as classification, object detection, and similarity based search. With recent advances in algorithms and GPUs, CNNs have been successful in many domains such as automotive, medical and geospatial analysis areas for classification, localization and segmentation of images. Many researchers and industry leaders are developing networks to help them solve their most important problems and ascertain intelligent information from large unstructured datasets. DIGITS can be used to help researchers in all of these areas to accelerate the network development process and improve their neural network accuracy in real-time with its visualization features.
# 
# DIGITS includes a visualization tool that enables real-time visualization of network accuracy and classification performance while developing and training an optimized network design. This tool provides a handy dashboard for users to keep track of their networks, easily toggle between different network designs to compare performance, monitor training performance in real-time, visualize network responses when classifying, and manage GPU resources for parallel network training.
#  
# For users with multi-GPU hardware, DIGITS will manage the GPU resources and assign training workloads to the GPUs, while allowing users to view the status of current and previous training jobs on a dashboard. This feature can be helpful when running more than one training in parallel and comparing results between trained networks. 
# 
# In this lesson we are going to cover how to apply a CNN to accurately identify handwritten digits using the [MNIST](http://yann.lecun.com/exdb/mnist/) data set using DIGITS. You will learn how to use DIGITS to pre-process data, load a pre-configured network, modify a pre-existing one, classify images, and use that information to quantify and then improve the trained network’s performance.    
# 
# Let’s quickly get familiar with DIGITS. The DIGITS Home screen is where the the main console page resides and will display all of your past and present activity. An image of the Home screen is displayed in Figure 1. Notice that there are two major panes, one for creating datasets and another for model development. These panes represent the two major steps to creating a trained network - creating your dataset and creating the model.
# 
# ![](files/images/image05.png)
# <div style="text-align:center;">_Figure 1. Image of the DIGITS console._</div>
# 
# All of the input data must be loaded into a database before the CNN can use it for training. This step is completed with the functionality exposed in the Dataset pane. Once your dataset has been created, you are ready to create a network and start training. Users can complete this part by accessing the New Image Classification Model via the Models pane. DIGITS provides default networks to help get you started. You can also modify a preexisting model, or build your own neural network architecture from scratch. In this first exercise we are going show you how to create your own dataset and classification model. 

# ## Task 1 - Creating a Database
# 
# You need data to develop a fully trained neural network. Before you can train the network the image data needs to be put in a database. This puts the image data into a single file that is then used by the framework for efficiently processing the input data. You will learn how to create a dataset in this task using an image dataset that we have supplied for you, the MNIST data. This data set is comprised of approximately 50,000 images from 10 different categories with dimensions 28 x 28. Each category is a single digit ranging from 0 to 9, and all of the images are tagged with their appropriate numeral category. Below is an example image from each category.
# 
# ![](files/images/MNIST.png)
# 
# Before we get started, <a href="/digits/" target="_blank">click here</a> to access the DIGITS server running on this lab instance in a separate window.  You should see the **Home** screen as shown Figure 1.
# 
# DIGITS allows users to create a data set with the **New Image Classification Dataset** window, shown in Figure 1. This window is accessed through the Dataset pane by going to **Images** and selecting **Classification**. 
# 
# As part of the data preparation process we need DIGITS to separate the data into two parts, training and validation. The entire image set will be used, but only the training images teach the network to discriminate between our categories. The validation set is used for testing the network and quantifying its accuracy during the training. In some cases training can last days, weeks, or even longer. Testing the accuracy allows developers to know how well their network is learning or in some cases not learning without waiting for training to complete. We will discuss the training in more detail in [Task 2](#Task-2---Creating-your-Network-and-Training).
# 
# To tell DIGITS where the images are, you need to enter the path to the images stored on this instance. Enter the path to the images into the edit box under **Training Images**. The image set path is 
# 
# `/home/ubuntu/data/mnist`
# 
# You have the option of choosing what percentage of images you want to use for the validation and training set. You may leave it at its default setting, 25%. 
# 
# All of the images are 28 x 28, so let’s keep them that size. In order to maintain this size you need to set this image size in the **Image Size** edit boxes along the left hand side. If you do not change this image size dimensions to 28 x 28, DIGITS will resize these images up to 256 x 256, the default dimensions. 
# 
# In some situations you may find that your input image may vary quite a bit in size making this feature handy. Notice that there are some resizing options within DIGITS, you have the flexibility to resize your images up and down as well as decide how you would like to transform it. You can partially crop and fill, crop, squash, or fill the images. View the each options and how they affect the resized images by pressing the **See Example** button. 
# 
# Give your dataset a name and then **Create** it.
# 
# You will notice that DIGITS updates you on its progress while it is creating the Dataset and provides statistical information on the image set.  Once DIGITS has finished, see if you can find where the following questions can be answered on the **Image Classification Dataset** page.
# 
# 
# 1. How long did it take to create your dataset?
#      <br>Should be ~75 seconds
# 2. What do the different columns in the **Create DB (train)** and **Created DB (val)** sections represent?
#      <br>These show how many of each digit we have in both the datasets.
# 3. How would you find how many images are in your training and validation set?
#      <br>Move mouse over the plotted bars 
# 
# Go back to the Home screen by selecting **DIGITS** in the upper left hand corner.
# 
# Notice your recently created dataset in the Home screen.  It should look something like this
# 
# ![](files/images/completed_dataset.png)
# 

# ## Task 2 - Creating your Network and Training
# 
# After a dataset has been created users should create their network model. Go to the models panel and select **Images** and then **Classification**. You will be taken to the **New Image Classification Model** window. This is where you configure your network parameters and train. 
# 
# To load your recently created dataset simply select it in the upper left hand corner in the **Select Dataset** box. 
# 
# Review the **Solver Options**: 
# * **Training Epochs** - this determines how many epochs you will complete during the training. If you set this to 30, the training will be completed after 30. An epoch is the processing of all of the data by the network a single time. If there are 50,000 images in the training set, a full epoch has been completed after they have been processed. 5 epochs means that all of the data will be ingested by the network 5 times.
# * **Snapshot Interval** - A snapshot is a file of your trained network. This is performed at multiple instances during training, and users have the option of increased or decreasing the frequency. Snapshots are used for classification and represent the network’s accuracy at the time it was saved.
# * **Validation Interval** -The validation interval is the frequency of the accuracy tests during training - users may increase or decrease this parameter. 
# * **Batch Size** -this determines how many images are processed at a time in the network. If you run out of memory on the GPU, you can reduce the batch size.
# * **Base Learning Rate** - This value is the learning rate for the network and impacts the rate at which the network learns to classify. If this value is larger, the network will learn faster but may not learn well.  It is usually best to start with a small value then slowly increase it if the training is too slow.
# 
# You can also hover your mouse over the ? next to each option to get some details on what it does.
# 
# Now let’s review our neural network configuration options. Notice that there are three standard networks available, Yan LeCun’s [LeNet](http://yann.lecun.com/exdb/lenet/), Alex Krizhevsky’s [AlexNet](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf), and Google’s [GoogleNet](http://arxiv.org/pdf/1409.4842v1.pdf). Users may also load  a previous network, customize one, or start from scratch.  
# 
# For this exercise we are going to select a standard network; Yan LeCun’s LeNet.  This is a 2 layer convolutional network with subsampling and a diagram of it is shown below. 
# 
# ![](files/images/image14.png)
# 
# Before we begin training let’s visualize the network in DIGITS by selecting **Customize** to the right of the LeNet Network in the **Standard Networks** tab. This will open the **Custom Network** tab and allow you to modify the network parameters and visualize the network. For now we will not modify this network we will just visualize it. Select the **Visualize** button to view the network. This feature shows all of the network parameters and how they are connected. The convolutional and subsampling (or pooling) in each layer is displayed in the graphic. Input parameters are displayed allowing users to view the kernel size and stride. This is an easy way to check errors in your network configuration too. Press OK at the bottom of the window to exit this screen.
# 
# Enter a name for your model at the bottom of the window and train with this standard network by selecting **Create**.  
#  
# While the training is ongoing you can:
# 1. Visualize the training accuracy while training. 
# 2. Observe the that the network configuration files (solver.prototxt, train_val.prototxt, or deploy.prototxt) are available for downloading.
# 3. Notice the Job Status information displayed along the right side of the model and the network accuracy while training. 
# 4. You can start classifying images as soon as a snapshot is taken. 
# 5. If you refresh the page while the training is occuring, you'll get a time estimate until completion.
# 
# Scroll down to the bottom of the window and classify these images. 
# 
# Classify the following images.  The **Image URL** is provided below each image.  You can copy & paste this into the DIGITS window.
# 
# <img src="files/images/image03.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image03.jpg</div>
# <img src="files/images/image11.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image11.jpg</div>
# <img src="files/images/image16.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image16.jpg</div>
# <img src="files/images/image00.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image00.jpg</div>
# <img src="files/images/image08.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image08.jpg</div>
# <img src="files/images/image09.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image09.jpg</div>
# <img src="files/images/image15.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image15.jpg</div>
# 
# Which one did not get classified correctly?  It appears the 1 and 4 had the most problems.
# 
# What is one way to improve a network’s performance? Changing the network configuration. Sometimes this is done by increasing the number of layer outputs and or number of layers. Let's do this in the next task.
# 
# 

# ##Task 3 - How does one modify a network? 
# 
# There are a variety of ways to improve a network’s performance or optimize for a specific application. One approach to accomplishing this is to continue modifying an existing network. This approach tends to be an iterative process but can be effective. Modifying a network and evaluating performance improvements can be easily done with DIGITS using its visualization features. 
# There are variety of parameters that can be modified, such as activation functions, the layer outputs, and stride between neurons. Krizhevsky [stated](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf) that he was able to train faster with rectified linear units activation function compared to hyperbolic tangent function. In some cases overlapping of the pooling has been shown to improve performance as well. Changes in performance can also be seen increasing the number of convolutional layers and their outputs. There are a lot of parameters and there are a lot of ways to impact a network’s performance. 
# 
# It is easy to modify a network using DIGITS. Now we will learn how to modify your network to improve its ability to classify the misclassified images above.  Let’s modify a standard network, the LeNet Network. Use your previously created dataset and create a new model that is a modified version of LeNet. 
# 
# Go to the DIGITS Main Console and select **Images** -> **Classification** in the Models pane. 
# 
# To help get you familiar with making changes you will make three modifications to the LeNet Network.
# 1. Increase the number of outputs in convolutional layer 1 to 75
# 2. Increase the number of outputs in convolutional layer 2 to 100
# 3. Add a activation function, ReLU,  to Convolutional layer 1 after the data has been subsampled.  **NOTE** there is already a "relu1" in this network, so choose a new name for this new ReLU function, like "reluTASK3".
# 
# To do this you will need to go back to the network customization window. This is the where users can modify networks. Changing parameters is easy. Let’s take a quick look at a convolutional layer parameters shown below. Each parameter has a name as well as a bottom and top connection. Convolutional layers have varying numbers of outputs and kernel sizes, these are all defined by the user. The kernel size is the size of the kernel used for that layer. The rectified linear unit activation (ReLU) function can be added to the end of the layer. More information on this activation function can be viewed [here](http://en.wikipedia.org/wiki/Rectifier_%28neural_networks%29).  Update the LeNet network  by changing the layers indicated below.
# 
# <code>
# layer {
#   name: "conv1"
#   type: "Convolution"
#   bottom: "scale"
#   top: "conv1"
#   param {
#     lr_mult: 1.0
#   }
#   param {
#     lr_mult: 2.0
#   }
#   convolution_param {
#     num_output: <span style="color:red;">75</span>
#     kernel_size: 5
#     stride: 1
#     weight_filler {
#       type: "xavier"
#     }
#     bias_filler {
#       type: "constant"
#     }
#   }
# }
# layer {
#   name: "pool1
#   type: "Pooling"
#   bottom: "conv1
#   top: "pool1
#   pooling_param {
#     pool: MAX
#     kernel_size: 2
#   }
# }
# <span style="color:red;">layer {
#   name: "reluTASK3"
#   type: "ReLU"
#   bottom: "pool1"
#   top: "pool1"
# }</span>
# layer {
#   name: "conv2"
#   type: "Convolution"
#   bottom: "pool1"
#   top: "conv2"
#   param {
#     lr_mult: 1
#   }
#   param {
#     lr_mult: 2
#   }
#   convolution_param {
#     num_output: <span style="color:red;">100</span>
#     kernel_size: 5
#     stride: 1
#     weight_filler {
#       type: "xavier"
#     }
#     bias_filler {
#       type: "constant"
#     }
#   }
# }
# </code>
# 
# After you make these changes, be sure to visualize your network configuration. This feature makes it easy to visualize the changes you just made and easily identify network configuration errors.
# 
# Once you are satisfied with your configuration changes, **reduce the number of epochs to 5 for the sake of time**, and start training. You can classify images while training as soon as a snapshot has been taken.  Try reclassifying the number images from the previous task.
# 
# **NOTE** on the off chance DIGITS hangs, you can restart it by executing the cell at the [bottom](#Restart-DIGITS-webserver) of this lab.
# 
# Do all of the images from Task 2 get correctly classified now? (They should)
# 
# Just by increasing the number of outputs in the convolutional layers we were able improve the accuracy of these test images. Why don’t we see this improvement greatly reflected in the accuracy plot?
# 
# While the network is still effectively training on its input data, not all of the images above are a good representation of that dataset. From the accuracy plot we cannot discern any drastic improvement, yet we are now able to correctly classify more of the images provided above. Modifying our network can improve its ability to classify. 
# 
# Some other ways to change a network that could improve its performance aside from what was done in this exercise:
# * Overlapping pooling windows
# * Adding a new layer
# * Changing bias values
# * Obtaining training data that better represents the images you would like to accurately classify
#  
# Making changes to a network is easy to do. You just made a few small modifications and you  were able to get slightly better performance. 

# ##Task 4 - How do I add a new layer?
# 
# Increasing the number of layers is another way to improve network accuracy and is easy to do. First let’s look at our current network. Notice that the input images are 28x28, and after each of our convolutions the feature map is reduced by the kernel radius and is further reduced after we subsample. There isn’t much room in the current network configuration to add another layer given an input image size of 28 x 28.
# 
# ![](files/images/image14.png)
# 
# If we add an additional convolutional layer, the feature map will reduce in size by the 2\*radius of the kernel and reduce further after subsampling. The feature map at this point is too small for the 5x5 kernel we have been applying in each convolutional layer. If our input images are larger we can keep the current network configuration and just add another layer. If the dataset is remade with image dimensions 60 x 60,  you could add a convolutional layer with a 5x5 and a subsampling (pooling) kernel size of 2. 
# 
# ![](files/images/image26.png)
# 
# For this task you will create a new dataset with larger image inputs. Go back to the DIGITS Main Console and go to **New Dataset** -> **Images** -> **Classification** in the Datasets pane. When you resize the images choose "Squash" for the resize transformation type and set the size to 60 x 60. Use the same images from the first dataset created in [Task 1](#Task-1---Creating-a-Database).  The path is:
# 
# `/home/ubuntu/data/mnist `
# 
# Once this is complete go back to the DIGITS Main Console. Notice how DIGITS displays all of your Datasets and Models, this makes it easy to compare performance of different models. 
# 
# Create a new model by **New Model** -> **Images** -> **Classification** in the Model pane on the right side of the Main Console window. Use your recently created data set, and modify the model you created in [Task 3](#Task-3---How-does-one-modify-a-network?) by going to Previous Networks, selecting the you most recent model, and then selecting customize. 
# Here is a list of the things you need to add for this task, all before the existing "conv1" layer:
# * Insert a new convolutional layer with 100 outputs and a kernel size of 5 at the beginning of the network.
# * Add a bias with a constant value of 0.9. 
# * Insert a pooling layer with a kernel size and stride of 2.
# * Add an a new (different from the one in Task 3) Rectified linear activation function (ReLU) activation. 
# * Update "conv1" to use "pool0" as the bottom
# * Increase the remaining two convolutional layer outputs to 100 and 250, respectively.
# 
# **Review** the input examples in [Task 3](#Task-3---How-does-one-modify-a-network?) if you need help with the format. 
# 
# ### Answer
# 
# The changes are shown below (not the whole file):<br>
# <code>
# layer {
#   name: "conv0"
#   type: "Convolution"
#   bottom: "scale"
#   top: "conv0"
#   param {
#     lr_mult: 1.0
#   }
#   param {
#     lr_mult: 2.0
#   }
#   convolution_param {
#     num_output: 100
#     kernel_size: 5
#     stride: 1
#     weight_filler {
#       type: "xavier"
#     }
#     bias_filler {
#       type: "constant"
#       value: 0.9
#     }
#   }
# }
# layer {
#   name: "pool0"
#   type: "Pooling"
#   bottom: "conv0"
#   top: "pool0"
#   pooling_param {
#     pool: MAX
#     kernel_size: 2
#     stride: 2
#   }
# }
# layer {
#   name: "relu0"
#   type: "ReLU"
#   bottom: "pool0"
#   top: "pool0"
# }
# layer {
#   name: "conv1"
#   type: "Convolution"
#   bottom: "pool0"
#   top: "conv1"
#   param {
#     lr_mult: 1.0
#   }
#   param {
#     lr_mult: 2.0
#   }
#   convolution_param {
#     num_output: 100
#     kernel_size: 5
#     stride: 1
#     weight_filler {
#       type: "xavier"
#     }
#     bias_filler {
#       type: "constant"
#     }
#   }
# }</code>
# 
# Be sure to double check your network configuration using the visualization feature. When you are satisfied with your changes, **choose 2 epohcs for the sake of time**, and begin training.
# 
# Classify the same images you have been in the past.  Notice that you are still getting good performance.
# 

# ## Task 5 - More Network Modifications
# 
# You have learned how to use a standard network and modify one. What if you make several changes and are still unable to correctly classify some objects?
# 
# If you don’t have a lot of data and are unable to obtain more that represents the images you plan to classify you can augment your training dataset. You can augment it based on the type of information you need it to classify, such as reversed colors, noise, or rotation.
# 
# Try classifying these images with your network.
# 
# <img src="files/images/image23.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image23.jpg</div>
# <img src="files/images/image02.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image02.jpg</div>
# <img src="files/images/image21.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image21.jpg</div>
# <img src="files/images/image17.jpg" width="64px" /> <div style="text-align:center;">/home/ubuntu/notebook/images/image17.jpg</div>
# 
# Why don’t they work? 
# 
# You may have noticed earlier that all of our training images are black digits with a white background. These new images have color and or have inverted contrast relative to the MNIST dataset. While some inverted and color images may get correctly classified with the network, these don’t. Let’s see if simply inflating our dataset can improve our network’s performance and correctly classify these images. Inverting the images is one way to inflate a training set and teach a network to correctly classify a larger range of inputs.
# 
# Create a new dataset with resize dimensions 60x60 and train with the last network you created, using the inverted image set. When you augment your dataset, you should prevent your image modifications from existing in both the training and validation sets. NNs are prone to overfitting on the training data, which is why a validation data set is important as it notifies developers if and when this is occurring. If the an augmented image is present in both the training and validation data sets, the network is using the same images for both the training and testing the networks accuracy. This is not what we want.  
# 
# To manually specify the images to use, you're going to use text files to explicity choose the images instead of just giving DIGITS a folder to randomly select training and validation images from.  To do this, go to **Upload Text Files** tab in the **New Image Classification Dataset** page. Upload the provided [train.txt](files/train.txt) to the **Trainig** text file, and [val.txt](files/val.txt) to the **Validation** text file, and finally the [labels.txt](files/labels.txt) to the **Labels** text file.  You will have to first download these text files to your computer from this page, and the upload them from the DIGITS window.  While waiting for the files to upload, you can look at them locally to see what they contain.
# 
# Each image in this new dataset contains all of the original images plus an inverted copy.  Some example images are shown below.
# 
# ![](files/images/image22.jpg)
# ![](files/images/image19.jpg)
# ![](files/images/image25.jpg)
# ![](files/images/image01.jpg)
# 
# Using this new dataset, run the network from Task 3 (you'll find it under **Previous Networks**) for 20 epochs.  You'll notice early on most of the colored images are correctly classified, but it takes a while before the "6" can be accurately classified.
# 
# In this example just inverting the images, proved to be an effective way to make the network more robust to color variations. Can you think of other ways to inflate the dataset and improve a trained network’s performance? 
# 
# Answer: Rotation, noise, color, stretching, etc
# 
# Could more layers help improve the network’s performance? 
# 
# Answer: Yes. You could create a 256 x 256 image dataset with the mnist data and test train with the AlexNet network to see if what type of improvements you can get with 5 convolutional layers and 2 fully connected.  Or you can create your own deep neural network.

# ## More information
# 
# To learn more about these topics, please visit:
# * GPU accelerated machine learning: [http://www.nvidia.com/object/machine-learning.html](http://www.nvidia.com/object/machine-learning.html)
# * Caffe: [http://caffe.berkeleyvision.org/](http://caffe.berkeleyvision.org/)
# * Theano: [http://deeplearning.net/software/theano/](http://deeplearning.net/software/theano/)
# * Torch: [http://torch.ch/](http://torch.ch/)
# * DIGITS: [https://developer.nvidia.com/digits](https://developer.nvidia.com/digits)
# * cuDNN: [https://developer.nvidia.com/cudnn](https://developer.nvidia.com/cudnn)

# ## Post-Lab Summary
# 
# In this lab you learned how to create datasets with different input sizes and resizing transformations. You also learned how to train with standard networks and modified ones
# 
# If you would like to download this lab for later viewing, it is recommend you go to your browsers File menu (not the Jupyter notebook file menu) and save the complete web page.  This will ensure the images are copied down as well.
# 
# ### Deep Learning Lab Series
# 
# Make sure to check out the rest of the classes in this Deep Learning lab series.  You can find them [here](https://developer.nvidia.com/deep-learning-courses).

# ## Restart DIGITS webserver
# 
# If your DIGITS server ever hangs, you can restart it by executing the cell below.

# In[ ]:

get_ipython().run_cell_magic(u'bash', u'', u'sudo ps aux | grep digits | awk \'{print $2}\' | xargs kill -9\nexport PYTHONPATH=/usr/lib/python2.7/dist-packages\nnohup /usr/local/anaconda/bin/python /home/ubuntu/digits-2.0/digits/digits-devserver 0<&- &>/dev/null &\n\n# Wait for the DIGITS server to start, or 60 seconds\nfor i in `seq 1 60`; do \n    curl -s http://localhost:5000 > /dev/null\n    if [ $? -eq 0 ]; then    # DIGITS is running \n        echo "Server is up!"\n        break\n    fi \n    sleep 1\ndone')

