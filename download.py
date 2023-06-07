import os
import threading
import shutil
import multiprocessing
import time
import requests
numberOfCores = multiprocessing.cpu_count()
activethreads=threading.active_count()
def download_files(images_el):
    for dirname,image_el_list in images_el.items():
        make_dir(dirname)
        download(image_el_list,dirname)
def make_dir(dirname):
    try:
        shutil.rmtree(dirname)
        os.mkdir(dirname)
    except:
        os.mkdir(dirname)
def download(image_el_list,dirname):
    i=0
    for element in image_el_list:
        t = threading.Thread(target=download_image , args=(element,dirname,i))
        i+=1
        t.start()
        while True:
            if (threading.active_count()-activethreads+1<=5*numberOfCores):
                break
            time.sleep(1)
    while True:
        if (threading.active_count()==activethreads):
            break
        time.sleep(1)
def download_image(element,dirname,i):
    if element is None:
        # print(f"element is none for {i}")
        return
    image_element = element.find("img", {"srcset": True})
    
    if image_element is None:
        # print(f"Image element not found in {i} element")
        return
    
    image_url = image_element.get("srcset")
    if not image_url:
        # print(f"Image URL not found in {i} element")
        return
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        # print(f"An error occurred while downloading the image: {str(e)} in {i} element")
        return
    
    if response.status_code == 200:
        # Extract the filename from the URL
        filename = f"{dirname}_{i+1}.jpg"
        
        # Construct the file path to save the image
        file_path = os.path.join(dirname, filename)
        
        # Save the image to the specified file path
        with open(file_path, 'wb') as file:
            file.write(response.content)
