import os, time

directories_0 = os.listdir("./")

classes = ['mug', 'bus', 'subway', 'cigarette', 'bottle']

def edit_labels(dir, label_num): # edit labels
    with open(dir, "r") as currentFile: 
        originalText = currentFile.readlines()
        newText = ""
        
        for line in originalText:
            words = line.split(" ")
            if words.__len__()<=4:
                words.insert(0, "")
                
            if words.__len__()<5:
                print("label form error..file :", dir)
                quit()
                
            newText+=f"{label_num} "
            for i in range(1, 5):
                newText+=f"{words[i]} " if i!=4 else words[i]
                
    with open(dir, "w") as f:
        f.write(newText)

for dir_0 in directories_0: # 
    if ".py" in dir_0 or "test" in dir_0:
        continue
    
    current_path0=f"./{dir_0}/"
    directories_1 = os.listdir(current_path0)
    ####
    if dir_0!="bottle1":
        continue
    ###
    for dir_1 in directories_1:
        if "README" in dir_1 or ".yaml" in dir_1 :
            continue
        current_path1 = "".join([current_path0, f"{dir_1}/labels/"])
        
        files = os.listdir(current_path1)
        for file_name in files:
            if ".txt" in file_name:
                for i in range(5):
                    if classes[i] in current_path1:
                        label = i
                        break
                    else:
                        label = "error"
                if label == "error":
                    print("class name error...file :", "".join([current_path1, file_name]))
                    quit()
                    
                print(f"editting...", "".join([current_path1, file_name]))
                edit_labels("".join([current_path1, file_name]), label)
print("Done")


