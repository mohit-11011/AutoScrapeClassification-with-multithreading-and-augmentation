import image_element
import download
import split_data
import augmentation_training
import model_train
import time
import predictions
searches=[]
mapping={}
inv_mapping={}
initial_time=time.time()
while(True):
    n_classes=int(input("enter the number of classes you want to perform cnn for:-"))
    if(n_classes>1 and n_classes<5):
        break
    else:
        print("enter a number between 2 and 4 (inclusive)")
for i in range(n_classes):
    search=input("enter what do u want to search:- ")
    mapping[i]=search
    inv_mapping[search]=i
    searches.append(search)
search_time=time.time()
print(f"searching done in {search_time-initial_time}")
image_el=image_element.multithreading_for_searches(searches)
image_el_time=time.time()
print(f"images elements in {image_el_time-search_time}")
download.download_files(image_el)
del image_el
download_time=time.time()
print(f"downloading done in {download_time-image_el_time}")
train_images, train_labels=split_data.split(searches)
splitting_time=time.time()
print(f"splitting done in {splitting_time-initial_time}")
train_images,train_labels=augmentation_training.aug_train(train_images,train_labels)
augmentation_time=time.time()
train_labels=[inv_mapping[label] for label in train_labels]
print(f"augmentation done in {augmentation_time-splitting_time} ")
model=model_train.model_train(train_images,train_labels,searches)
del train_images,train_labels
print(model.summary())
model_train_time=time.time()
print(f"model trained in {model_train_time-augmentation_time}")
test_images,test_labels=split_data.split_test(searches)
pred=predictions.pred(model,test_images,test_labels,mapping)
print(pred)
pred_time=time.time()
print(f"prediction time is {pred_time-model_train_time}")