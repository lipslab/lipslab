import sys
import os 
import cv2

images_path = sys.argv[1]
thumbnails_path = os.path.join(images_path, "thumbnails")
event_name = os.path.basename(images_path)

if not os.path.isdir(thumbnails_path):
    os.mkdir(thumbnails_path)

images = os.listdir(images_path)

yml_line = "gallery:\n"

for ind, image in enumerate(images):
    im_path = os.path.join(images_path, image)
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".JPG") or image.endswith(".jpeg"):
        img = cv2.imread(im_path)
        h, w = img.shape[:2]
        if h >= w:
            # vertical 
            img = img[:w, ...]
        else:
            # horizaonal 
            edges = w // 2
            img = img[:, edges: w - edges, :]
        img = cv2.resize(img, (300, 300))
        cv2.imwrite(os.path.join(thumbnails_path, image), img)
    
        yml_line += f"   - url: /photos/{event_name}/{image}\n"
        yml_line += f"     image_path: /photos/{event_name}/thumbnails/{image}\n"

print(yml_line)

