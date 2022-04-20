import os
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from fne import full_network_embedding

if __name__ == '__main__':
    # This shows an example of calling the full_network_embedding method using
    # the VGG16 architecture pretrained on ILSVRC2012 (aka ImageNet), as
    # provided by the keras package. Using any other pretrained CNN
    # model is straightforward.

    # Load model
    img_width, img_height = 224, 224
    initial_model = tf.keras.applications.VGG16(weights="imagenet", include_top=True,
                                                input_shape=(img_width, img_height, 3))
    target_layer_names = ['block1_conv1', 'block1_conv2', 'block2_conv1', 'block2_conv2', 'block3_conv1', 'block3_conv2',
                          'block3_conv3', 'block4_conv1', 'block4_conv2', 'block4_conv3', 'block5_conv1', 'block5_conv2',
                          'block5_conv3', 'fc1', 'fc2']
    
    # Define data splits
    # Train set
    train_path = '/gpfs/projects/nct00/nct00001/mit67/train/'
    train_images = []
    train_labels = []
    # Use a subset of classes to speed up the process. -1 uses all classes.
    num_classes = 3
    for train_dir in os.listdir(train_path):
        train_dir_path = os.path.join(train_path, train_dir)
        for train_img in os.listdir(train_dir_path):
            train_images.append(os.path.join(train_dir_path, train_img))
            train_labels.append(train_dir)
        num_classes -= 1
        if num_classes == 0:
            break
    # Test set
    test_path = '/gpfs/projects/nct00/nct00001/mit67/test/'
    test_images = []
    test_labels = []
    num_classes = 3
    for test_dir in os.listdir(test_path):
        test_dir_path = os.path.join(test_path, test_dir)
        for test_img in os.listdir(test_dir_path):
            test_images.append(os.path.join(test_dir_path, test_img))
            test_labels.append(test_dir)
        num_classes -= 1
        if num_classes == 0:
            break

    print('Total train images:', len(train_images), ' with their corresponding', len(train_labels), 'labels')
    print('Total test images:', len(test_images), ' with their corresponding', len(test_labels), 'labels')

    # Parameters for the extraction procedure
    batch_size = 128
    input_reshape = (224, 224)
    # Call FNE method on the train set
    fne_features, fne_stats_train = full_network_embedding(initial_model, train_images, batch_size,
                                                           target_layer_names, input_reshape)
    print('Done extracting features of training set. Embedding size:', fne_features.shape)

    from sklearn import svm

    # Train SVM with the obtained features.
    clf = svm.LinearSVC()
    clf.fit(X=fne_features, y=train_labels)
    print('Done training SVM on extracted features of training set')

    # Call FNE method on the test set, using stats from training
    fne_features, fne_stats_train = full_network_embedding(initial_model, test_images, batch_size,
                                                           target_layer_names, input_reshape, stats=fne_stats_train)
    print('Done extracting features of test set')

    # Test SVM with the test set.
    predicted_labels = clf.predict(fne_features)
    print('Done testing SVM on extracted features of test set')

    # Print results
    print(classification_report(test_labels, predicted_labels))
    print(confusion_matrix(test_labels, predicted_labels))
