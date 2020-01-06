# -*- coding:utf-8 -*-
import os
import json
DATASET_PATH =  '/home/donglin/qizhi/mmdetection/data/coco/annotations'

with  open(os.path.join(DATASET_PATH,  'annotations.json'))  as f:
    json_file = json.load(f)
    print(type(json_file))
    print('所有图片的数量：',  len(json_file['images']))
    print('所有标注的数量：',  len(json_file['annotations']))

    bg_imgs = set()  # 所有标注中包含背景的图片 id

    for c in json_file['annotations']:

        if c['category_id'] == 0:

            bg_imgs.add(c['image_id'])

    print('所有标注中包含背景的图片数量：', len(bg_imgs))

    bg_only_imgs = set()  # 只有背景的图片的 id

    for img_id in bg_imgs:

        co = 0

        for c in json_file['annotations']:

            if c['image_id'] == img_id:

                co += 1

                if co == 1:

                    bg_only_imgs.add(img_id)

    print('只包含背景的图片数量：', len(bg_only_imgs))

    images_to_be_deleted = []

    for img in json_file['images']:

        if img['id'] in bg_only_imgs:

            images_to_be_deleted.append(img)

    # 删除的是只有一个标注，且为 background 的的图片

    print('待删除图片的数量：', len(images_to_be_deleted))

    for img in images_to_be_deleted:

        json_file['images'].remove(img)

    print('处理之后图片的数量：', len(json_file['images']))

    ann_to_be_deleted = []

    for c in json_file['annotations']:

        if c['category_id'] == 0:

            ann_to_be_deleted.append(c)

    print('待删除标注的数量：', len(ann_to_be_deleted))

    for img in ann_to_be_deleted:

        json_file['annotations'].remove(img)

    print('处理之后标注的数量：', len(json_file['annotations']))

    bg_cate = {'supercategory': '背景', 'id': 0, 'name': '背景'}

    json_file['categories'].remove(bg_cate)

    print(json_file['categories'])

    for idx in range(len(json_file['annotations'])):

        json_file['annotations'][idx]['id'] = idx
    ss=[]
    for i in range(len(json_file['annotations'])):
#        print(json_file['annotations'][i]['image_id'])
        ss.append(json_file['annotations'][i]['id'])
    print(len(ss))

    with  open(os.path.join(DATASET_PATH, 'annotations_washed.json'), 'w')  as f:

        json.dump(json_file, f)