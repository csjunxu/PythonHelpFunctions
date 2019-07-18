import os
#import shutil
import cv2
print('Move the files into a single directory')
# path = 'FaceSR'
# path_HR = 'Face/Face_train_HR'
path = 'DIV2K'
path_HR = 'NewDIV2K'
image_num = 0
for root, dir_list, file_list in os.walk(path):
    #for dir_name in dir_list:
    #    print(os.path.join(root, dir_name))
    folders = []
    for folder in dir_list :
        folders.append(os.path.join(root, folder))
    for f in folders:
        print(f)

    files = []
    for file in file_list:
        if '.png' in file:
            files.append(os.path.join(root, file))

    for f in files:
        print(f)


    for i in range(len(file_list)):
        print(file_list[i])
        if (file_list[i][-3:] == 'jpg') or (file_list[i][-3:] == 'png') or (file_list[i][-3:] == 'JPG'):
            file_path = root+'/'+file_list[i]
            # Read image to process
            image_HR = cv2.imread(file_path)
            height, width, channels = image_HR.shape
            # print (height, width, channels)
            # save HR image
            path_HR_im = path_HR+'/'+ file_list[i]
            # shutil.copy(file_path, path_HR_im)
            cv2.imwrite(path_HR_im, image_HR)

            # save LR images
            # Compute size of LR images and resize HR images to a multiple of scale
            for scale in range(2, 9):
                # Create target Directory if don't exist
                path_LR = 'x' + str(scale)
                if not os.path.exists(path_LR):
                    os.mkdir(path_LR)
                    print("Directory ", path_LR, " Created ")
                else:
                    print("Directory ", path_LR, " already exists")

                height_LR = int(height / scale)
                width_LR = int(width / scale)
                image_LR = cv2.resize(image_HR, (width_LR, height_LR))
                path_LR_im = path_LR + '/' + file_list[i][:-4] + 'x' + str(scale) + file_list[i][-4:]
                cv2.imwrite(path_LR_im, image_LR)

            image_num += 1
            if image_num == 10000000:
                break

print('1000w face images are done!')
